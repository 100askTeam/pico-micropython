from machine import Pin, PWM
from time import sleep

#初始化GP0脚为PWM功能
mtr0 = PWM(Pin(0))

#初始化GP1脚为GPIO输出
mtr1 = Pin(1,Pin.OUT)

#设置时钟频率为1khz
mtr0.freq(1000)

#设置GP1引脚输出为低电平
mtr1.value(0)


while True:
    for duty in range(65025):
        mtr0.duty_u16(duty)
        sleep(0.0001)
