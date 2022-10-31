import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)#BCM
#GPIO.setwarnings(False)

red_led=12
green_led=24
btn1=14
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN, GPIO.PUD_UP)

def light_on(red_on, green_on):
        GPIO.output(red_led, red_on)
        GPIO.output(green_led, green_on)

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

                                                GPIO.output(red_led,GPIO.LOW)
                                                GPIO.output(green_led,GPIO.HIGH)
                                                print("F,T")
                                                time.sleep( 5 )
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
                                                print("T,F")
except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
finally:
        print("Cleaning up GPIO...")
        GPIO.cleanup()



