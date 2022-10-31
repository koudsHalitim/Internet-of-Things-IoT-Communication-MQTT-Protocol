import RPi.GPIO as GPIO
import time
#import paho.mqtt.client as mqttc

import paho.mqtt.publish as publish

hostname = "test.mosquitto.org"
port = 1883
topic_state = "PC000/traffic_light/state"

GPIO.setmode(GPIO.BCM)#BCM
#GPIO.setwarnings(False)

red_led=12
green_led=24
btn1=14
btn2=26
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, GPIO.PUD_UP)

def light_on(red_on, green_on):
        GPIO.output(red_led, red_on)
        GPIO.output(green_led, green_on)
#       publish.single(topic_state,payload= "3", qos=0,hostname=hostname,port=port)  # State 1

btn_state= GPIO.input(btn1)
GPIO.output(green_led,False)
GPIO.output(red_led,False)
'''light_on(False,True)
time.sleep(1)
light_on(False,False)
time.sleep(1)
light_on(False,True)
time.sleep(1)
light_on(False,False)
time.sleep(1)'''
#GPIO.output(green_led,False)
print(btn_state)
try:
                while True:
                        btn_state= GPIO.input(btn1)
                        if btn_state== 0:
                                        print('Start Blinking! .. ')
                                        while True:
                                                btn_emrg= GPIO.input(btn2)
                                                if btn_emrg== 0:
                                                        print('Umergency Btn Clicked!')
                                                        publish.single(topic_state,payload= "True", qos=0,hostname=hostname,port=port)

#                                               publish.single(topic_state,payload= "3", qos=0,hostname=hostname,port=port)  # State 1
                                                GPIO.output(red_led,GPIO.LOW)
                                                GPIO.output(green_led,GPIO.HIGH)
                                                publish.single(topic_state,payload= "1", qos=0,hostname=hostname,port=port)  # State 1
                                                print("F,T")
                                                time.sleep( 5 )

                                                publish.single(topic_state,payload= "2", qos=0,hostname=hostname,port=port)
                                                GPIO.output(green_led,GPIO.LOW)
                                                print("F,F")
                                                time.sleep( 1 )
                                                GPIO.output(green_led,GPIO.HIGH)
                                                print("F,T")
                                                time.sleep( 1 )
                                                GPIO.output(green_led,GPIO.LOW)
                                                print("F,F")
                                                time.sleep( 1 )
                                                GPIO.output(green_led,GPIO.HIGH)
                                                print("F,T")
                                                time.sleep( 1 )
                                                GPIO.output(green_led,GPIO.LOW)
                                                print("F,F")
                                                GPIO.output(red_led,GPIO.HIGH)
                                                publish.single(topic_state,payload= "3", qos=0,hostname=hostname,port=port)  # State 3
                                                print("T,F")
                                                time.sleep( 5 )
                                                GPIO.output(red_led,GPIO.LOW)
                                                print("F,F")
except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
finally:
        print("Cleaning up GPIO...")
        GPIO.cleanup()




