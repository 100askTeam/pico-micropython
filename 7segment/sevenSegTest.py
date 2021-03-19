# 树莓派Pico开发板外接七位共阳数码管测试程序
# Code source  https://gitee.com/weidongshan/pico-micropython/blob/master/7segment/sevenSegTest.py
# 7segment a = Pico GP2 - Pin 4
# 7segment b = Pico GP3 - Pin 5
# 7segment c = Pico GP4 - Pin 6
# 7segment d = Pico GP5 - Pin 7
# 7segment e = Pico GP6 - Pin 9
# 7segment f = Pico GP7 - Pin 10
# 7segment g = Pico GP8 - Pin 11


from machine import Pin, Timer
from time import sleep

timer = Timer()
seg1_count = 0;


segment_one = [
    Pin(2, Pin.OUT), 
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(6, Pin.OUT),
    Pin(7, Pin.OUT),
    Pin(8, Pin.OUT)]


def display_num(number, segments):
    numbers = {
        0: lambda segments : turn_on(segments[0:6]),
        1: lambda segments : turn_on(segments[1:3]),
        2: lambda segments : turn_on([segments[0]] + [segments[1]] + [segments[3]] + [segments[4]] + [segments[6]]), 
        3: lambda segments : turn_on(segments[0:4] + [segments[6]] ),        
        4: lambda segments : turn_on([segments[1]] + [segments[2]] + [segments[5]] + [segments[6]] ),
        5: lambda segments : turn_on([segments[0]] + [segments[2]] + [segments[3]] + [segments[5]] + [segments[6]]),
        6: lambda segments : turn_on([segments[0]] + segments[2:7]),
        7: lambda segments : turn_on(segments[0:3]),
        8: lambda segments : turn_on(segments),
        9: lambda segments : turn_on((segments[0:4] + [segments[5]] + [segments[6]]))
    }
    numbers[number](segments)

def shut_off(segments):
    for segment in segments:
        segment.value(1)
        
def turn_on(segments):
    for segment in segments:
        segment.value(0)
 
def segment_on(timer):
    global seg1_count
    if seg1_count < 7:
        segment_one[seg1_count].value(0)
        seg1_count += 1
    else:
        seg1_count = 0
        shut_off(segment_one)

# 循环显示1-9    
display_test = 0
num_test = True
while num_test:
    display_num(display_test, segment_one)
    sleep(1)
    shut_off(segment_one)
    sleep(1)
    display_test += 1
    if display_test > 9:
        display_test = 0

