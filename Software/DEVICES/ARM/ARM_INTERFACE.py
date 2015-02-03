import time
import ARM_MODEL
import ARM_CONTROLLER
import network.I2C
import threading
from speed import speed
import sys
import select

class arm(threading.Thread):
	i2cAddr = 0x40

	def __init__(self):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.model		= ARM_MODEL.arm()
		self.isRunning 		= True
		self.i2c 		= network.I2C.i2c(self.i2cAddr)
		self.deviceController	= ARM_CONTROLLER.arm(self.model,self.i2cAddr)
		self.speedController    = speed(self.model)


	def run(self):
		self.deviceController.start()
		self.speedController.start()
		while self.model.isRunning:
		#have some check on pantilt behaviour like switching between manual and scan mode
			#print "running"
			time.sleep(1)

	def act(self):
		#self.model.state = sys.stdin

		i, o, e = select.select( [sys.stdin], [], [], 10 )

		if (i):
			self.model.state=sys.stdin.readline().strip()
		else:
			self.model.state=""	
 
			
if __name__ == "__main__":

	device = arm()
	device.start()
	
	try:
		while True:
			#device.act()
			#print device.model.motor0_power, device.model.motor1_power, device.model.motor2_power
			i, o, e = select.select( [sys.stdin], [], [], 10 )

			if (i):
				device.model.state=sys.stdin.readline().strip()
			else:
				device.model.state=""	

	except KeyboardInterrupt:
		device.model.isRunning = False
		print "Device Terminated"



		
