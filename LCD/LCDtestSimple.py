#LCDtestSimple.py
#Mario The Maker
from pico_i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin
import utime as time
LCD_SDA_PIN = 16 # update this
LCD_SCL_PIN = 17 # update this

 
i2c = I2C(id=0,scl=Pin(LCD_SCL_PIN),sda=Pin(LCD_SDA_PIN),freq=90000)
lcd = I2cLcd(i2c, 0x27, LCD_SCL_PIN, LCD_SDA_PIN)
 
while True:
      lcd.move_to(6,0)
      lcd.putstr('Hello')
      lcd.move_to(6,1)
      lcd.putstr('World')
