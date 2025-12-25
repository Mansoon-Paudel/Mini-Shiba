#!/usr/bin/env python3
from gpiozero import Button
import uinput
import time
from mapping import MAPPING

buttons = {}

with uinput.Device(MAPPING.values()) as device:
    for io, key_event in MAPPING.items():
        button = Button(io, bounce_time=0.05)
        button.when_pressed = lambda event=key_event: device.emit(event, 1)
        button.when_released = lambda event=key_event: device.emit(event, 0)
        buttons[io] = button

    while True:
        time.sleep(1)