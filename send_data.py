#!/usr/bin/python

import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket

###

def generateData(priority, command):
	genData = []
	genData.append(priority)
	genData.append(command)
	genData.append(0x02)
	genData.append(0xa6)

	'''
		0 <= x < 20
		    Gehäusebeleuchtung (TODO: Details?) 
		20 <= x < 123
		    Östlicher LED-Stripe 
		123 <= x < 226
		    Westlicher LED-Stripe

		(wiki.c3d2.de/led-stripe)
	'''

	for i in range(0,225): #Repeat for LEDs 1-226

		''' generate funny random colors '''

		colorR = random.randrange(0x55, 0xff)
		colorG = random.randrange(0x55, 0xff)
		colorB = random.randrange(0x55, 0xff)


		''' only for debug'''

		# print ("random color R = " + str(colorR))
		# print ("random color G = " + str(colorG))
		# print ("random color B = " + str(colorB))

		if i in range(0,225):
			genData.append(colorR) #red
			genData.append(colorG) #green
			genData.append(colorB) #blue


	print(genData)
	return genData

###

CONNECT_TO = "172.22.99.206"
PORT = 2342

priority = 0xff
command = 0x00

udp_data = generateData(priority, command)

### SEND DATA ###

while priority != 0xff:
	sock.sendto(udp_data, (CONNECT_TO, PORT))
	print ("send data to : " + sock.getfqdn(CONNECT_TO))