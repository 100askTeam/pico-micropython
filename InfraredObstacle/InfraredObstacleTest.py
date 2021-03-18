# 树莓派Pico开发板外接红外避障模块测试程序
# 
# Pico GPIO 26 ADC0 - Pin 32

import machine
import utime

TRIGGER_LEVEL = 2000
potentiometer = machine.ADC(26)


while True:
    data = potentiometer.read_u16()
    print("data is ",data)
    
    if data >= TRIGGER_LEVEL:
        print("Far")
        utime.sleep(0.5)
    if data < TRIGGER_LEVEL:
        print("Near")
        utime.sleep(0.5)
