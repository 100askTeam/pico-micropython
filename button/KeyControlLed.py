# Code source https://gitee.com/weidongshan/pico-micropython/blob/master/button/KeyControlLed.py

from machine import Pin
import utime

button = button_black = Pin(2, Pin.IN, Pin.PULL_UP)
led = Pin(14, Pin.OUT)

while True:
    if button.value() == 0:
        led.value(1)
        print("Key press")
        utime.sleep(0.1)
        
    if button.value() == 1:
        led.value(0)
        print("Key release")
        utime.sleep(0.1)