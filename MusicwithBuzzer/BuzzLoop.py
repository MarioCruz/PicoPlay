from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
n=3000

while n > 2:
    print(n) # print 
    buzzer.freq(n)
    n = n-75
    buzzer.duty_u16(1000)
    sleep(0.5)

buzzer.duty_u16(0)
