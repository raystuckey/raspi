# email from http://stackoverflow.com/questions/920910/python-sending-multipart-html-emails-which-contain-embedded-images
import picamera
from time import sleep
from time import time
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import pibrella
import os
import signal

def email_pic(picname):
	# Define these once; use them twice!
	strFrom = 'sender@email.address.com'
	strTo = 'receiver@email.address.com'

	# Create the root message and fill in the from, to, and subject headers
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = picname
	msgRoot['From'] = strFrom
	msgRoot['To'] = strTo
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	msgText = MIMEText('A picture.')
	msgAlternative.attach(msgText)

	# We reference the image in the IMG SRC attribute by the ID we give it below
	msgText = MIMEText('<img src="cid:image1">', 'html') # <b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!
	msgAlternative.attach(msgText)

	# This example assumes the image is in the current directory
	fp = open(picname, 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()

	# Define the image's ID as referenced above
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	# Send the email (this example assumes SMTP authentication is required)
	import smtplib
	smtp = smtplib.SMTP_SSL()
	smtp.connect('smtp.gmail.com', 465) # put your email server here, or just use gmail
	smtp.login('login@email.com', 'password')
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()

	os.remove(picname)

	print('Picture posted to http://a.great.website.com/')


def take_picture(filename):
    pibrella.light.red.on()
    pibrella.buzzer.buzz(200)
    sleep(.2)
    pibrella.light.red.off()
    pibrella.buzzer.off()
    sleep(.1)
    pibrella.light.yellow.on()
    pibrella.buzzer.buzz(200)
    sleep(.2)
    pibrella.light.yellow.off()
    pibrella.buzzer.off()
    sleep(.1)
    pibrella.light.green.on()
    pibrella.buzzer.buzz(800)
    sleep(.2)
    pibrella.light.green.off()
    pibrella.buzzer.off()
 
    camera = picamera.PiCamera()
    camera.hflip = 1
    camera.vflip = 1
    camera.capture(filename)
    camera.close()



def snap_and_post_pic(whatever):
    pic_name=datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H.%M.%S')+".jpg"
    take_picture(pic_name)
    email_pic(pic_name)





pibrella.button.pressed(snap_and_post_pic)

signal.pause()


