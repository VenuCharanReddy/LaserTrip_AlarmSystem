from gpiozero import LightSensor, Buzzer, LED
from picamera import PiCamera
from time import sleep


ldr = LightSensor(4) 
led = LED(18)
buzzer = Buzzer(17)
camera = PiCamera()
