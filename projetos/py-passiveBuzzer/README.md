# Passive buzzer tone player and its compatibility with asyncio

## Motivation

Someone reported to me that merging a passive buzzer tone player froze his/her webserver (written using Microdot).

I guessed there might be a hardware timer issue, since hardware timers are relatively scarce (a microcontroller usually have 2 or 3) and they are used to generate PWM signals. My guess is probably wrong.

Micropython `asyncio` do not rely on hardware timers (`asyncio` is not preemptive). 

I will try to implement a simple webserver (using microdot) which plays one tone.


https://www.google.com/search?q=micropython+asyncio+use+hardware+timers&oq=micropython+asyncio+use+hardware+timers&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBNIBCTI0MTMyajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8
https://forum.micropython.org/viewtopic.php?t=9449
https://github.com/orgs/micropython/discussions/12598
https://stackoverflow.com/questions/77579445/python-async-with-timer-and-endless-loop
https://www.google.com/search?q=micropython+tone+library+use+timers&oq=micropython+tone+library+use+timers&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBNIBCTE0MzI4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://forum.arduino.cc/t/timerfreetone-library-v1-5-play-tones-without-timers-and-therefore-no-conflicts/229448
https://forum.micropython.org/viewtopic.php?t=659
https://docs.micropython.org/en/latest/library/machine.html
https://docs.micropython.org/en/latest/library/machine.html#machine.lightsleep
https://www.google.com/search?q=esp32+wifi+uses+adc&oq=esp32+wifi+uses+adc&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRifBTIHCAMQIRifBTIHCAQQIRifBTIHCAUQIRifBTIHCAYQIRifBTIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCTExMzk4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://www.google.com/search?q=micropython+asyncio+tone+library&oq=micropython+asyncio+tone+library&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBNIBCTExNTQ5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://docs.micropython.org/en/latest/library/machine.I2S.html
https://github.com/mcauser/awesome-micropython
https://www.google.com/search?q=esp32+i2s+commands&oq=esp32+i2s+commands&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigAdIBCTE1MDQzajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8
https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/i2s.html
https://www.google.com/search?q=micropython+i2s&oq=micropython+i2s&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgTGIAEMggIAhAAGBMYHjIICAMQABgTGB4yCAgEEAAYExgeMgoIBRAAGAUYExgeMgYIBhBFGDwyBggHEEUYPNIBCTExMzg1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://docs.micropython.org/en/latest/library/machine.I2S.html
https://github.com/miketeachman/micropython-i2s-examples
https://www.google.com/search?q=does+micropython+asyncio+interfere+with+tone+generation&sca_esv=06c568487881745e&sca_upv=1&ei=QXztZqbGFMy55OUPjJmT8QE&ved=0ahUKEwjm6u_p09GIAxXMHLkGHYzMJB4Q4dUDCA8&uact=5&oq=does+micropython+asyncio+interfere+with+tone+generation&gs_lp=Egxnd3Mtd2l6LXNlcnAiN2RvZXMgbWljcm9weXRob24gYXN5bmNpbyBpbnRlcmZlcmUgd2l0aCB0b25lIGdlbmVyYXRpb24yBxAhGKABGAoyBBAhGBVIhJYBUPwZWJyTAXABeAGQAQCYAa4BoAH2K6oBBDAuNDC4AQPIAQD4AQGYAiWgAokpwgIKEAAYsAMY1gQYR8ICBRAhGKABwgIFECEYnwWYAwCIBgGQBgiSBwQxLjM2oAe-ogE&sclient=gws-wiz-serp
https://www.coderdojotc.org/micropython/advanced-labs/13-timers/
https://forum.micropython.org/viewtopic.php?t=4003
https://www.google.com/search?q=%22micropython%22+playing+tones&sca_esv=06c568487881745e&sca_upv=1&biw=1850&bih=932&ei=UX7tZpCMEq7b1sQP5oa7iA8&ved=0ahUKEwjQ-M_l1dGIAxWurZUCHWbDDvEQ4dUDCA8&uact=5&oq=%22micropython%22+playing+tones&gs_lp=Egxnd3Mtd2l6LXNlcnAiGyJtaWNyb3B5dGhvbiIgcGxheWluZyB0b25lczIFECEYoAEyBRAhGKABSMqWBlDVwgVY9ZMGcAJ4AZABAJgBoAGgAfkTqgEEMC4xOLgBA8gBAPgBAZgCD6AC5A7CAgoQABiwAxjWBBhHwgIEECEYFcICBRAhGJ8FwgIHECEYoAEYCsICBhAAGBYYHsICCBAAGIAEGKIEwgIEEAAYHsICCBAhGKABGMMEwgIKECEYoAEYwwQYCpgDAIgGAZAGCJIHBDIuMTOgB84-&sclient=gws-wiz-serp
https://www.coderdojotc.org/micropython/sound/02-play-tone/
https://forum.micropython.org/viewtopic.php?t=12003
https://forum.micropython.org/viewtopic.php?t=5819
https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html#beepers
https://github.com/mcauser/awesome-micropython
https://docs.sunfounder.com/projects/esp32-starter-kit/en/latest/micropython/basic_projects/py_pa_buz.html


