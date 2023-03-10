import time

#GPIO initialize
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#PIN settting
SW_PIN=    #Q2 pin number
LED_PIN=   #Q3 pin number

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
        GPIO.output(,1)  #Q3  hint, pinset
    else:
        print("OFF")
                         


    #wait for 0.5 sec
    time.sleep(0.5)        
