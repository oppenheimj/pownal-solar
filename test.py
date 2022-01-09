import lib8relay
import time
import RPi.GPIO as GPIO
switch = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
input=GPIO.input(switch)

while not (GPIO.input(switch)):
	lib8relay.get_all(0)
	print('Switch status =',GPIO.input(switch))	
	
	lib8relay.set(0,1,GPIO.input(switch))
	time.sleep(.1)
else:
	print('Switch status =',GPIO.input(switch))	
	lib8relay.set(0,1,GPIO.input(switch))
	time.sleep(.1)
	lib8relay.set(0,1,0)

		

		


