from machine import Pin, PWM
from utime import sleep

# PWM is Pulse-width modulation (PWM)
# Pulse width modulation, allows you to give analogue behaviours to digital devices
# such as LEDs. This means that rather than an LED being simply on or off, you can
# control its brightness.
buzzer = PWM(Pin(15))

buzzer.freq(50) #Play a Frequency on the buzzer range (25-3500)
buzzer.duty_u16(200) #Think of this as volume range (0 - 4500)
sleep(1) #Sleep
buzzer.duty_u16(0) # turn it off 
