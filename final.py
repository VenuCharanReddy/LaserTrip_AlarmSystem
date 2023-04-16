from gpiozero import LightSensor, Buzzer, LED
from picamera import PiCamera
from time import sleep
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib
import datetime
import time

ld = LightSensor(4)  
buzzer = Buzzer(17)  
led = LED(18)
camera = PiCamera()

smtpUser = 'sender_mail@gmail.com'
smtpPass= 'sender pass'
toAdd='receiver mail'
fromAdd= smtpUser



while True:
    sleep(0.1)
    led.off()
    if ld.value < 0.65:  
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

   
        msg=MIMEMultipart()
        msg['subject'] = 'Intruder Alert..!!'
        msg['content'] = time.ctime()
        msg['From'] = fromAdd
        msg['To'] = toAdd
        
        # Add text to the email
        body = "Use the link below \n\n"
        msg.attach(MIMEText(body, 'plain'))
        
        # Add links to the email
        links = [
            'rtsp://raspberrypi:8080/'
            ]
        for link in links:
            msg.attach(MIMEText(f"- {link}\n", 'plain'))
            print(msg['From'] + '\n' + msg['To'] + '\n' + body + '\n' + msg['content'])

        File = open(Captured1,'rb')
        img1 = MIMEImage(File.read())
        File.close()
        msg.attach(img1)
        File = open(Captured2,'rb')
        img2 = MIMEImage(File.read())
        File.close()
        msg.attach(img2)

            #send Mail
        server = smtplib.SMTP('mail.csestudent.in',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtpUser,smtpPass)
        print("Login Successfull")
        server.sendmail(fromAdd,toAdd,msg.as_string())
        server.quit()
        print('Email sent')
    
    else:
        buzzer.off()
        led.off()
