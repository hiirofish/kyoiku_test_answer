import time

#GPIO initialize
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#PIN settting
SW_PIN=21
LED_PIN=20

#switch input gpio setting
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#led output gpiot setting
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    #get sw status
    sw_status = GPIO.input(SW_PIN)

    #display 
    if sw_status == 0:
        print("ON")
        GPIO.output(LED_PIN,1) 
    else:
        print("OFF")
        GPIO.output(LED_PIN,0)


    #wait for 0.5 sec
    time.sleep(0.5)        
