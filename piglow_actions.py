from morse_code import play_code
from piglow import PiGlow
from time import sleep


piglow = PiGlow()
piglow.all(0)


def demo_all():
	indiv_sweep()
	color_sweep()
	sleep(1)
	blink(10)
	sleep(1)
	lightup()
	lightdown()
	lightup()
	lightdown()
	sleep(1)
	pinwheel(8)
	play_code("Hello World!")

def indiv_sweep():
    leds = range(1, 19)
    for led in leds:
        piglow.led(led, 50)
        sleep(.4)
        piglow.led(led, 0)
    sleep(.4)
    piglow.all(0)

def blink(how_many = 1):
    times = range(0, how_many)
    for time in times:
        piglow.all(100)
        sleep(.05)
        piglow.all(0)
        sleep(.05)
        
def lightup():
    brights = range(5,100,5)
    for bright in brights:
        leds = range(1,19)
        for led in leds:
            piglow.led(led,bright)
            sleep(.003)

def lightdown():
    brights = range(5, 100, 5)
    for bright in brights:
        leds = range(1, 19)
        for led in leds:
            piglow.led(19-led, 100-bright)
            sleep(.003)
    piglow.all(0)

def pinwheel(repeats):
	arms = [1,2,3]
	for turn in range(0,repeats):
		for arm in arms:
			piglow.arm(arm,20)
			sleep(.12)
			piglow.arm(arm,0)
	piglow.all(0)

def color_sweep():
	colors = range(1,7)
	for color in colors:
		piglow.colour(color,50)
		sleep(.3)
		piglow.colour(color,0)








demo_all()
