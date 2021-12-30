#********************Mario The Maker 2022********************
#************************** Pico Fun ************************


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

buzzer(BuzzerObj,c,0.25,0.1)
buzzer(BuzzerObj,d,0.25,0.1)
buzzer(BuzzerObj,e,0.25,0.1)
buzzer(BuzzerObj,f,0.25,0.1)
buzzer(BuzzerObj,g,0.25,0.1)
buzzer(BuzzerObj,a,0.25,0.1)
buzzer(BuzzerObj,b,0.25,0.1)
buzzer(BuzzerObj,c2,0.25,1)#last one rest for 1 whole 


#Play Scales half notes 

buzzer(BuzzerObj,c,0.5,0.1)
buzzer(BuzzerObj,d,0.5,0.1)
buzzer(BuzzerObj,e,0.5,0.1)
buzzer(BuzzerObj,f,0.5,0.1)
buzzer(BuzzerObj,g,0.5,0.1)
buzzer(BuzzerObj,a,0.5,0.1)
buzzer(BuzzerObj,b,0.5,0.1)
buzzer(BuzzerObj,c2,0.5,1)


#Play Scales whole notes 

buzzer(BuzzerObj,c,1,0.1)
buzzer(BuzzerObj,d,1,0.1)
buzzer(BuzzerObj,e,1,0.1)
buzzer(BuzzerObj,f,1,0.1)
buzzer(BuzzerObj,g,1,0.1)
buzzer(BuzzerObj,a,1,0.1)
buzzer(BuzzerObj,b,1,0.1)
buzzer(BuzzerObj,c2,1,1)



#Deactivates the buzzer
BuzzerObj.deinit()



#*********************** Notes to frequency ********************************* 
#Octave1 Notes:      c1      d1      e1      f1      g1      a1      b1
#/* 1st octave */   {32.703, 36.708, 41.203, 43.654, 48.990, 55.000, 61.735},

#/Octave2 Notes:      c2      d2      e2      f2      g2       a2       b2
#/* 2nd octave */   {65.406, 73.416, 82.407, 87.307, 97.999, 110.000, 123.470},  

#/Octave3 Notes:       c3       d3       e3       f3       g3       a3       b3 
#/* 3rd octave */   {130.810, 146.830, 164.810, 174.610, 196.000, 220.000, 246.940},
    
#/Octave4 Notes:       c4       d4       e4       f4       g4       a4       b4
#/* 4th octave */   {261.630, 293.660, 329.630, 349.230, 392.000, 440.000, 493.880},
   
#/Octave5 Notes:       c5       d5       e5       f5       g5       a5       b5
#/* 5th octave */   {523.250, 587.330, 659.250, 698.460, 783.990, 880.000, 987.770},
 
#/Octave6 Notes:        c6        d6        e6        f6        g6        a6        b6  
#/* 6th octave */   {1046.500, 1174.700, 1318.500, 1396.900, 1568.000, 1760.000, 1979.500},
 
#/Octave7 Notes:        c7        d7        e7        f7        g7        a7        b7  
#/* 7th octave */   {2093.000, 2349.300, 2637.000, 2793.800, 3136.000, 3520.000, 3951.100}

#Notes to frequency Sharps

#/Octave1 Sharps:     C1      D1      F1      G1      A1 
#/* 1st octave */   {34.648, 38.891, 46.249, 51.913, 58.270},
  
#/Octave2 Sharps:     C2      D2      F2       G2       A2 
#/* 2nd octave */   {69.296, 77.782, 92.499, 103.830, 116.540},
  
#/Octave3 Sharps:      C3       D3       F3       G3       A3 
#/* 3rd octave */   {138.590, 155.560, 185.000, 207.650, 233.080},
   
#/Octave4 Sharps:      C4       D4       F4       G4       A4 
#/* 4th octave */   {277.184, 311.130, 369.990, 415.300, 466.160},
  
#/Octave5 Sharps:      C5       D5       F5       G5       A5 
#/* 5th octave */   {554.370, 622.250, 739.990, 830.610, 932.330},
  
#/Octave6 Sharps:       C6        D6        F6        G6        A6 
#/* 6th octave */   {1108.700, 1244.500, 1480.000, 1661.200, 1864.700},
  
#/Octave7 Sharps:       C7        D7        F7        G7        A7 
#/* 7th octave */   {2217.500, 2489.000, 2960.000, 3322.400, 3729.300}  
