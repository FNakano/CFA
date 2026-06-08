"""Local simulation harness for the MicroPython project.

Run with:
    python simulate.py

This script injects lightweight mocks for hardware/network modules so the
existing project code can be exercised on a regular desktop Python runtime.
"""

from __future__ import annotations

import argparse
import json
import sys
import types
from datetime import datetime, timezone
from pathlib import Path
from urllib import error, request
from urllib.parse import parse_qs, urlparse


SIM_STATE = {
    "last_display_lines": [],
    "last_http_payload": None,
}


def log(level: str, message: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] [{level}] {message}")


class Response:
    def __init__(self, status_code: int, text: str):
        self.status_code = status_code
        self.text = text

    def close(self):
        return None


def install_requests_mock() -> None:
    requests = types.ModuleType("requests")

    def get(url):
        query = parse_qs(urlparse(url).query)
        payload = {
            "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "field1": query.get("field1", ["n/a"])[0],
            "field2": query.get("field2", ["n/a"])[0],
            "field3": query.get("field3", ["n/a"])[0],
        }
        SIM_STATE["last_http_payload"] = payload
        log(
            "SIM",
            (
                "HTTP MOCK /update.json "
                f"field1={payload['field1']} field2={payload['field2']} field3={payload['field3']}"
            ),
        )
        return Response(200, json.dumps(payload))

    requests.get = get
    sys.modules["requests"] = requests


def install_requests_real() -> None:
    requests = types.ModuleType("requests")

    def get(url):
        log("INFO", f"HTTP REAL GET: {url}")
        try:
            with request.urlopen(url, timeout=15) as resp:
                text = resp.read().decode("utf-8", errors="replace")
                status = int(resp.getcode() or 200)
                log("INFO", f"HTTP REAL status: {status}")
                try:
                    SIM_STATE["last_http_payload"] = json.loads(text)
                except Exception:
                    SIM_STATE["last_http_payload"] = {"raw": text}
                return Response(status, text)
        except error.HTTPError as e:
            text = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else str(e)
            log("ERR", f"HTTP REAL ERROR status={int(e.code)} body={text}")
            return Response(int(e.code), text)
        except Exception as e:
            log("ERR", f"HTTP REAL exception={type(e).__name__}: {e}")

            return Response(599, str(e))

    requests.get = get
    sys.modules["requests"] = requests


def install_mocks(real_http: bool = False) -> None:
    """Register fake modules used by the project code."""

    log("INFO", "Installing simulation mocks")

    # machine -----------------------------------------------------------------
    machine = types.ModuleType("machine")

    class Pin:
        IN = 0
        OUT = 1
        PULL_UP = 2

        def __init__(self, pin, mode=None, pull=None):
            self.pin = pin
            self.mode = mode
            self.pull = pull
            self.state = 0

        def on(self):
            self.state = 1

        def off(self):
            self.state = 0

        def value(self, v=None):
            if v is None:
                return self.state
            self.state = int(v)

    class I2C:
        def __init__(self, bus, sda=None, scl=None):
            self.bus = bus
            self.sda = sda
            self.scl = scl

        def scan(self):
            # 0x3C (OLED), 0x76 (BME280)
            return [60, 118]

        def readfrom_mem(self, *_args, **_kwargs):
            return b"\x00"

        def writeto_mem(self, *_args, **_kwargs):
            return None

        def readfrom_mem_into(self, *_args, **_kwargs):
            return None

    class ADC:
        def __init__(self, *_args, **_kwargs):
            pass

    def deepsleep(ms=None):
        log("SIM", f"deepsleep called: {ms} ms")

    machine.Pin = Pin
    machine.I2C = I2C
    machine.ADC = ADC
    machine.DEEPSLEEP_RESET = 5
    machine.wake_reason = lambda: 0
    machine.deepsleep = deepsleep
    sys.modules["machine"] = machine

    # network -----------------------------------------------------------------
    network = types.ModuleType("network")
    network.STA_IF = 0

    class WLAN:
        def __init__(self, _if_type):
            self.connected = False
            self.hostname = "device001"
            self._ifconfig = (
                "192.168.0.111",
                "255.255.255.0",
                "192.168.0.1",
                "8.8.8.8",
            )

        def active(self, _is_active):
            return None

        def config(self, hostname=None):
            if hostname:
                self.hostname = hostname

        def connect(self, ssid, _password):
            self.connected = bool(ssid)

        def isconnected(self):
            return self.connected

        def ifconfig(self):
            return self._ifconfig

    network.WLAN = WLAN
    sys.modules["network"] = network

    # sh1106 ------------------------------------------------------------------
    sh1106 = types.ModuleType("sh1106")

    class SH1106_I2C:
        def __init__(self, width, height, _i2c):
            self.width = width
            self.height = height
            self._lines = {}

        def fill(self, _color):
            self._lines = {}

        def text(self, txt, _x, y, _color):
            self._lines[y] = txt

        def show(self):
            ordered = [self._lines[k] for k in sorted(self._lines.keys())]
            SIM_STATE["last_display_lines"] = ordered
            log("SIM", "display refresh")
            for idx, line in enumerate(ordered, start=1):
                print(f"  L{idx}: {line}")

    sh1106.SH1106_I2C = SH1106_I2C
    sys.modules["sh1106"] = sh1106

    # bme280_float ------------------------------------------------------------
    bme280_float = types.ModuleType("bme280_float")

    class BME280:
        def __init__(self, i2c=None):
            self.i2c = i2c

        def read_compensated_data(self):
            # temperature (C), pressure (Pa), humidity (%)
            return (32.7, 101325.0, 52.3)

        @property
        def values(self):
            t, p, h = self.read_compensated_data()
            return (f"{t:.2f}C", f"{p/100:.2f}hPa", f"{h:.2f}%")

    bme280_float.BME280 = BME280
    sys.modules["bme280_float"] = bme280_float

    # requests ----------------------------------------------------------------
    if real_http:
        log("INFO", "Requests module in REAL mode (publishes to ThingSpeak)")
        install_requests_real()
    else:
        log("INFO", "Requests module in MOCK mode (no external publish)")
        install_requests_mock()


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Run project simulation with optional real HTTP publishing")
    parser.add_argument(
        "--real-http",
        action="store_true",
        help="Use real HTTP requests so ThingSpeak receives data",
    )
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    project_root = Path(__file__).resolve().parent
    pyboard_dir = project_root / "pyboard"
    if str(pyboard_dir) not in sys.path:
        sys.path.insert(0, str(pyboard_dir))

    log("INFO", f"Project root: {project_root}")
    log("INFO", f"Using pyboard dir: {pyboard_dir}")

    install_mocks(real_http=args.real_http)

    # Importing these modules executes the same startup path used on device.
    log("INFO", "Running startup path: import btest, import main")
    import btest  # noqa: F401
    import main as board_main  # noqa: F401

    payload = SIM_STATE.get("last_http_payload")
    disp_lines = SIM_STATE.get("last_display_lines") or []
    ok = bool(payload and isinstance(payload, dict) and payload.get("created_at"))
    if payload:
        if payload.get("created_at"):
            log("OK", f"HTTP payload timestamp: {payload['created_at']}")
        else:
            log("WARN", f"HTTP payload without created_at: {payload}")
    else:
        log("WARN", f"No HTTP payload captured - publish likely failed")

    log("OK", f"Display lines rendered: {len(disp_lines)}")
    if ok:
        log("OK", "Simulation finished successfully")
    else:
        log("ERR", "Simulation finished with publish failure")


if __name__ == "__main__":
    main()
