from gpiozero import LightSensor, Buzzer, LED
from picamera import PiCamera
from time import sleep
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib
import datetime
import time

ldr = LightSensor(4)  # alter if using a different pin
buzzer = Buzzer(17)  # alter if using a different pin
led = LED(18)
camera = PiCamera()

while True:
    sleep(0.1)
    led.off()
    if ldr.value < 0.5:  # adjust this to make the circuit more or less sensitive
        buzzer.on()
        led.on()
          
        camera.resolution = (2592,1944)
        camera.framerate = 15
        Captured1='/home/pi/Desktop/image'+datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png'
        camera.rotation = 180
        camera.capture(Captured1)
        
        buzzer.off()
        led.off()

        Captured2='/home/pi/Desktop/image'+datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png'
        camera.rotation = 180
        camera.capture(Captured2)
        print('Image Captured')
    else:
        buzzer.off()
        led.off()
     
