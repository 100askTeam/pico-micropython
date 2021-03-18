# 树莓派Pico开发板外接10K滑动变阻器ADC输入测试示例
# 
# Pico GPIO 26 ADC0 - Pin 32

import machine
import utime

potentiometer = machine.ADC(26)

while True:
    print(potentiometer.read_u16())
    utime.sleep(1)
