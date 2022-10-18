# External module imp
import RPi.GPIO as GPIO
import datetime
import time
from weather import *
from temp_hum import *
from w_to_csv import *
from mail import *

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
#     print(GPIO.input(channel))
#     return GPIO.input(channel)
    temp, humidity = get_final()
    if GPIO.input(channel):
        print('No water detected')
        print('Checking watering time....')
        if check_time():
            print('Checking weather...')
            if not itw_rain():
                pump_on(temp, humidity)
                print('Plant Watered!')
            else:
                print('It will rain in the future')
        else:
            print('Watered less than 3 hrs ago.')
        
    else:
        print('Water Detected!')
    
    if temp > 40 and humidity < 25:
        pump_on(temp, humidity)
        print('Temp more, hence watered')

    if check_time():
        pump_on(temp, humidity)
        print('Watered more than 3hrs ago, so watered.')

        

def get_status(): 
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
    print('Checking...')
    # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)
    print('...now')# assign function to GPIO PIN, Run function on change
    # infinite loop
    while True:
        time.sleep(10)


def pump_on(temp, humidity):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)

    time.sleep(20)

    GPIO.output(17, GPIO.HIGH)
    GPIO.cleanup()
    wr_to_csv(temp, humidity)
    send_mail()


if __name__ == "__main__":
    get_status()