# Code source https://gitee.com/weidongshan/pico-micropython/new/master/buzzer

from machine import Pin
import utime

buzzer = Pin(1, Pin.OUT)

while True:
    utime.sleep(1)
    buzzer.value(1)
    utime.sleep(1)
    buzzer.value(0)
