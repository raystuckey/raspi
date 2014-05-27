import picamera
from piglow import PiGlow
from time import sleep
from time import time
import datetime


def take_picture(filename):
    camera = picamera.PiCamera()
    camera.hflip = 1
    camera.vflip = 1
    camera.capture(filename)

piglow = PiGlow()
piglow.all(0)

def indiv_sweep():
    leds = range(1, 19)
    for led in leds:
        piglow.led(led, 30)
        sleep(.5)
    sleep(5)
    piglow.all(0)

def blink(how_many):
    times = range(0, how_many)
    for time in times:
        piglow.all(100)
        sleep(.05)
        piglow.all(0)
        sleep(.05)
        
def lightup():
    brights = range(5,45,5)
    for bright in brights:
        leds = range(1,19)
        for led in leds:
            piglow.led(led,bright)
            sleep(.005)

def lightdown():
    brights = range(5, 45, 5)
    for bright in brights:
        leds = range(1, 19)
        for led in leds:
            piglow.led(19-led, 50-bright)
            sleep(.005)
    piglow.all(0)

def count_down(seconds):
    for second in range(0,seconds):
        lightdown()
        sleep(.4)
    piglow.all(0)

def snap_pic():
    count_down(3)
    take_picture(datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H.%M.%S')+".jpg")
    blink(2)

snap_pic()
