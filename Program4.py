# Blinking program

#incorporate modules 
import machine #module
import Time

#make object
#GPIO Pin 0
led=machine.Pin(0,machine.Pin.OUT)

# infinite loop
while true:
  led.value(1) # turn on led
  time.sleep(0.25) #Blink 
  led.value(0) # turn off led
  time.sleep(0.25) # delay again