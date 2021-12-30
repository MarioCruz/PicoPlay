
from machine import Pin, PWM
from time import sleep

buzzerPIN=15
BuzzerObj = PWM(Pin(buzzerPIN))

def buzzer(buzzerPinObject,frequency,note_duration,rest_duration):

    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.1))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(note_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(rest_duration)
    print(frequency)


#NoteLength 
#0.0625 sixtenth 
#0.125 eighth 
#0.25 Quarter
#0.5  Half
#1	  Whole	

#set translation table from note to frequency
#Starts at C5
c=523  #c
cc=554 #c#
d=587  #d
dd=622 ## 
e=659  #e 
f=698  #f
ff=739 ##
g=784 #g
gg=830 ##
a=880  #a
aa=932 ##
b=987  #b
c2=1046  #c6


#Play Scales Quarter notes 

buzzer(BuzzerObj,g,0.38,0.1) # Doted quarter
buzzer(BuzzerObj,g,0.0625,0.1)
buzzer(BuzzerObj,a,0.333,0.1) # Trying for Triplet feel went to 3333
buzzer(BuzzerObj,g,0.333,0.1)
buzzer(BuzzerObj,f,0.333,0.1)
buzzer(BuzzerObj,d,0.6,0.1)
buzzer(BuzzerObj,d,0.6,0.2)



#Deactivates the buzzer
BuzzerObj.deinit()

