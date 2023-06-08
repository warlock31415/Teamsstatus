import supervisor
from time import sleep
import board

import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

value = "\0"

while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()

    if value == "online":
        led.value = True
    else:
        led.value = False
        