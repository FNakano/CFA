# **How to access your ESP32's AP alongside your main internet connection**

You might want to connect to your ESP32's AP without losing your main
internet connection. Here's a few methods to do that.

These instructions assume a Linux environment running `systemd`.

# Method 1: Use you phone as a WiFi interface

TLDR: Connect your phone to the ESP's AP, share the phone's connection
to your computer via USB thetering, route requests for `192.168.4.1` to
your phone.

Dependencies: an Android phone.

1.  Configure `systemd-networkd` to support Android USB thetering:

    (Alternatively, follow the instructions on the Arch wiki:
    <https://wiki.archlinux.org/title/Android_tethering#USB_tethering>.)

    Create a file at
    `/etc/systemd/network/40-usb-android-thetering.network` with the
    following content:

    ``` ini
    [Match]
    Property="ID_MODEL=<YOUR_ID_MODEL>" "ID_USB_DRIVER=<YOUR_ID_USB_DRIVER>"

    [Network]
    DHCP=ipv4

    [DHCPv4]
    # Default metric is 1024, setting a value lower makes this the default route
    RouteMetric=1024
    ```

    The values for `<YOUR_ID_MODEL>` and `<YOUR_ID_USB_DRIVER>` can be
    obtained with:

    ``` sh
    udevadm info /sys/class/net/<YOUR_INTERFACE_NAME>/
    ```

    Where `<YOUR_INTERFACE_NAME>` is the interface of the USB thetering
    connection.

2.  Find the IP address of your USB thetering connection:

    Look for `inet` in the output of the command below. Ignore the `/24`
    suffix if any. For example, if the output is
    `inet 192.168.8.18/24 metric ...`, the IP address is `192.168.8.18`.

    ``` sh
    ip address show <USB_THETERING_INTERFACE_NAME>
    ```

    Where `<USB_THETERING_INTERFACE_NAME>` is the name of the interface
    of your USB thetering connection.

3.  Configure routing:

    Add a route to the ESP32's AP through the USB thetering connection
    IP address obtained before.

    ``` sh
    sudo ip route add 192.168.4.0/24 via <USB_THETERING_IP_ADDRESS> dev <USB_THETERING_INTERFACE_NAME>
    ```

    Now, requests for `192.168.4.1` on your computer should go through
    your phone, which is in the same network as the ESP's AP.

    To remove the route, run:

    ``` sh
    sudo ip route delete 192.168.4.0/24 via <USB_THETERING_IP_ADDRESS> dev <USB_THETERING_INTERFACE_NAME>
    ```

# Method 2: Ethernet for main connection, WiFi for ESP's AP

TLDR: keep your main connection via ethernet, connect your WiFi
interface to the ESP's AP, route requests for `192.168.4.1` to the WiFi
interface.

Dependencies: separate ethernet and WiFi interfaces.

This method uses iwd's `iwctl` tool for managing WiFi connections. Adapt
as necessary for other tools such as NetworkManager's `nmcli`.

1.  Find out the name of your WiFi interface:

    Check the output the command below for names starting with `wl`
    (usually `wlan0`, but can be different).

    ``` sh
    ip link
    ```

2.  Connect the WiFi interface to the ESP's AP:

    ``` sh
    iwctl station <WIFI_INTERFACE_NAME> connect <AP_SSID>
    ```

    Where `<WIFI_INTERFACE_NAME>` is the name of your WiFi interface,
    and `<AP_SSID>` is the SSID of your ESP's AP. For example:
    `iwctl station wlan0 connect esp32`.

3.  Configure routing:

    Add a route to the ESP32's AP through the WiFi interface.

    ``` sh
    sudo ip route add 192.168.4.1 dev <WIFI_INTERFACE_NAME>
    ```

    Now, requests for `192.168.4.1` on your computer should go through
    your WiFi interface, which is connected to the ESP's AP.

    To remove the route, run:

    ``` sh
    sudo ip route delete 192.168.4.1 dev <WIFI_INTERFACE_NAME>
    ```

# Method 3: Buy an external WiFi adapter

TLDR: connect the external WiFi adapter's interface to the ESP's AP,
route requests for `192.168.4.1` to the external interface.

Dependencies: an external USB WiFi adapter.

Tip: don't buy too cheap.

1.  Find out the name of your WiFi interface:

    Check the output the command below for names starting with `wl`.
    Usually it's something like `wlan1` if your builtin WiFi interface
    is `wlan0`.

    ``` sh
    ip link
    ```

2.  Connect the external WiFi interface to the ESP's AP:

    ``` sh
    iwctl station <EXTERNAL_WIFI_INTERFACE_NAME> connect <AP_SSID>
    ```

    Where `<EXTERNAL_WIFI_INTERFACE_NAME>` is the name of your external
    WiFi adapter's interface, and `<AP_SSID>` is the SSID of your ESP's
    AP. For example: `iwctl station wlan1 connect esp32`.

3.  Configure routing:

    Add a route to the ESP32's AP through the external WiFi adapter's
    interface.

    ``` sh
    sudo ip route add 192.168.4.1 dev <EXTERNAL_WIFI_INTERFACE_NAME>
    ```

    Now, requests for `192.168.4.1` on your computer should go through
    your external WiFi interface, which is connected to the ESP's AP.

    To remove the route, run:

    ``` sh
    sudo ip route delete 192.168.4.1 dev <EXTERNAL_WIFI_INTERFACE_NAME>
    ```
