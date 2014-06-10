import RPi.GPIO as gpio # import the GPIO module so that we can access the GPIO ports
from time import sleep # import the time module, we will use this for the sleep command
import threading
from threading import Thread
 


 
A440 = (440./(2**5))
C = A440 * (2 ** (1/12.)) ** 3 #A4 = 440 Hz
Db = A440 * (2 ** (1/12.)) ** 4
D = A440 * (2 ** (1/12.)) ** 5
Eb = A440 * (2 ** (1/12.)) ** 6
E = A440 * (2 ** (1/12.)) ** 7
F = A440 * (2 ** (1/12.)) ** 8
Gb = A440 * (2 ** (1/12.)) ** 9
G = A440 * (2 ** (1/12.)) ** 10
Ab = A440 * (2 ** (1/12.)) ** 11
A = A440 * (2 ** (1/12.)) ** 12
Bb = A440 * (2 ** (1/12.)) ** 13
B = A440 * (2 ** (1/12.)) ** 14


class Pibrella():
	gpio.setmode(gpio.BCM) # use the broadcom pin numbering for the GPIO port
	gpio.setwarnings(True) # make sure that warnings are switched on

	def exit(self):
		gpio.cleanup()

class Lights(Pibrella):
	if gpio.RPI_REVISION == 1:
		REDLED = 21 # 21 on Rev 1
	else:
		REDLED = 27
	GREENLED = 4
	AMBERLED = 17
	
	# set the Red LED pin for output.
	gpio.setup(REDLED,gpio.OUT)
	gpio.setup(AMBERLED,gpio.OUT)
	gpio.setup(GREENLED,gpio.OUT)
 
# set the Red LED pin to high, we could use the value 1 here
# or True (as I have here) or gpio.HIGH

	def redlight(self, OnOrOff=1):
		gpio.output(self.REDLED,OnOrOff)

	def yellowlight(self, OnOrOff=1):
		gpio.output(self.AMBERLED,OnOrOff)

	def greenlight(self, OnOrOff=1):
		gpio.output(self.GREENLED,OnOrOff)

	def alllights(self, OnOrOff=1):
		self.redlight(OnOrOff)
		self.yellowlight(OnOrOff)
		self.greenlight(OnOrOff)

	def blink(self):
		while 1:
			self.alllights(1)
			sleep(.5)
			self.alllights(0)
			sleep(.5)

class Music(Pibrella):
	PIEZOSPEAKER = 18 # lets define some pins to use on the pibrella
	gpio.setup(PIEZOSPEAKER,gpio.OUT) # set the PIEZO SPEAKER pin for output.



	p = gpio.PWM(PIEZOSPEAKER,300)

	def __init__(self, melody, tempo=120):
		self.melody = melody
		self.tempo = tempo

	def play_note(self, name, octive=4, length=4., tempo=120.):
		#print name*2**(octive)
		if name == 0:
			self.p.stop()
		else:
			self.p.start(1)
			self.p.ChangeFrequency(name*2**octive)
			#pibrella.buzzer.buzz(name*2**octive)
			leds.alllights()
		sleep(60./tempo*length/2)
		leds.alllights(0)
		sleep(60./tempo*length/2)

	def play_melody(self):
		#print 'melody', self.melody
		for note in self.melody:
			self.play_note(note[0], note[1], note[2], self.tempo)
		self.p.stop()
		self.exit()
		



chorus = [[F, 4, 1],
		  [Gb, 4, 1],
		  [G, 4, 1],
		  [Gb, 4, 1],
		  [F, 4, 1],
		  [Gb, 4, 1],
		  [G, 4, 2],
		  [F, 4, 1.5],
		  [F, 4, .5],
		  [G, 4, 1],
		  [A, 4, 1],
		  [Bb, 4, 1],
		  [D, 5, 3], #
		  [Bb, 4, 1.5],
		  [A, 4, .5],
		  [Bb, 4, 1],
		  [G, 4, 1],
		  [F, 4, 1],
		  [G, 4, 1],
		  [A, 4, 1],
		  [Bb, 4, 1],
		  [C, 5, 1],
		  [G, 4, 1],
		  [A, 4, 1],
		  [Bb, 4, 1],
		  [C, 5, .5],
		  [0, 0 , .5],
		  [A, 4, .5],
		  [0, 0 , .5],		  
		  [G, 4, .5],
		  [0, 0 , .5],		  
		  [F, 4, .5],
		  [0, 0 , .5],		  
		  [F, 4, 1],
		  [Gb, 4, 1],
		  [G, 4, 1],
		  [Gb, 4, 1],
		  [F, 4, 1],
		  [Gb, 4, 1],
		  [G, 4, 1],
		  [0, 0, .5],
		  [D, 4, .5],
		  [G, 4, .5],
		  [G, 4, 1],
		  [A, 4, .5],
		  [Bb, 4, 1],
		  [C, 5, 1],
		  [D, 5, 2],
		  [0, 0, 2],
		  [Bb, 4, 1],
		  [0, 0, 1],
		  [Bb, 4, 1],
		  [0, 0 , 1],
		  [Bb, 4, .5],
		  [0, 0 , .5],		  
		  [Bb, 4, .5],
		  [0, 0 , .5],		  
		  [Bb, 4, .5],
		  [0, 0 , .5],
		  [0, 0 , 1],
		  [G, 4, .5],
		  [Gb, 4, .5],
		  [G, 4, .5],
		  [Ab, 4, .5],
		  [A, 4, 1],
		  [F, 4, 1],
		  [Bb, 4, 4]		  
		 ] 

star_wars = [[D, 4, 1./3-1./30], [0, 0, 1./30],
			[D, 4, 1./3], [0, 0, 1./30],
			[D, 4, 1./3], [0, 0, 1./30],
			[G, 4, 2],
			[D, 5, 2],
			[C, 5, 1./3],
			[B, 4, 1./3],
			[A, 4, 1./3],
			[G, 5, 2],
			[D, 5, 1],
			[C, 5, 1./3],
			[B, 4, 1./3],
			[A, 4, 1./3],
			[G, 5, 2],
			[D, 5, 1],
			[C, 5, 1./3],
			[B, 4, 1./3],
			[C, 5, 1./3],
			[A, 4, 2]
			]

leds = Lights()
#sw = Music(star_wars, 120)
#sw.play_melody()


fightsong = Music(chorus, 200)
fightsong.play_melody()

#leds.blink()
leds.exit()




