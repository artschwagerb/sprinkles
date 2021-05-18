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
                #print("{} {}".format(self.name, self.status())
                msg = i2c_msg.write(DEVICE_ADDRESS, [self.number, 1])
                bus.i2c_rdwr(msg)
                #print("{} {}".format(self.name, self.status())
                self.log("ON")

        def turn_off(self):
                #print("{} {}".format(self.name, self.status())
                msg = i2c_msg.write(DEVICE_ADDRESS, [self.number, 0])
                bus.i2c_rdwr(msg)
                #print("{} {}".format(self.name, self.status())
                self.log("OFF")

        def status(self):
                msg = bus.read_byte_data(DEVICE_ADDRESS, self.number, force=None)
                if msg == 0:
                        return False
                else:
                        return True

        def log(self, message):
                print("{:5} (Zone {}) {} - {}".format(self.name, self.number, self.status(), message))

z1 = sprinkler_zone('Front', 1)
z2 = sprinkler_zone('Road', 2)
z3 = sprinkler_zone('Left', 3)
z4 = sprinkler_zone('Right', 4)

sprinklers = [z1, z2, z3, z4]

# for testing, why not turn on all the values?
#for z in sprinklers:
#       z.turn_on()

# Seconds are hard
# 1 min = 60 sec
# 2 min = 120 sec
# 3 min = 180 sec
# 4 min = 240
# 5 min = 300 sec
# 7 min = 420 sec
# 10 min = 600 sec
# 12 min = 720 sec
# 15 min = 900 sec

# Zone 1
# 05/17/21 -- 420 -> 600 sec, still crispy
z1.turn_on()
time.sleep(600)
z1.turn_off()

time.sleep(10)

# Zone 2
# 05/17/21 -- 300 -> 600 sec, still crispy
z2.turn_on()
time.sleep(600)
z2.turn_off()

time.sleep(10)

# Zone 3
# 05/17/21 -- 120 -> 300 sec, still crispy
z3.turn_on()
time.sleep(300)
z3.turn_off()

time.sleep(10)

# Zone 4
# 05/17/21 -- 180 -> 600 sec, rose and blueberry bush need more water, side gets a lot of sun
z4.turn_on()
time.sleep(600)
z4.turn_off()

time.sleep(10)

# Fail safe, shut off all relays
for z in sprinklers:
        z.turn_off()
        time.sleep(5)
