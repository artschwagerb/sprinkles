#!/usr/bin/python3

import time
from smbus2 import SMBus, i2c_msg

bus = SMBus(1)

DEVICE_ADDRESS = 0x10

#bus.write_byte_data(DEVICE_ADDRESS, 1, 1)
#msg = i2c_msg.write(DEVICE_ADDRESS, [0x01,0x01])
#bus.i2c_rdwr(msg)

class sprinkler_zone(object):
	def __init__(self, name, number):
		self.name = name
		self.number = number

	def turn_on(self):
		msg = i2c_msg.write(DEVICE_ADDRESS, [self.number, 1])
		bus.i2c_rdwr(msg)
		self.log("ON")

	def turn_off(self):
		msg = i2c_msg.write(DEVICE_ADDRESS, [self.number, 0])
		bus.i2c_rdwr(msg)
		self.log("OFF")

	def log(self, message):
		print("{:5} (Zone {}) - {}".format(self.name, self.number, message))

z1 = sprinkler_zone('Front', 1)
z2 = sprinkler_zone('Road', 2)
z3 = sprinkler_zone('Left', 3)
z4 = sprinkler_zone('Right', 4)

sprinklers = [z1, z2, z3, z4]

#for z in sprinklers:
#	z.turn_on()

z1.turn_on()
z4.turn_on()
time.sleep(2)
z2.turn_on()
z1.turn_off()
time.sleep(2)
z3.turn_on()
z2.turn_off()
time.sleep(2)
z4.turn_on()
z3.turn_off()
time.sleep(4)

for z in sprinklers:
	z.turn_off()

