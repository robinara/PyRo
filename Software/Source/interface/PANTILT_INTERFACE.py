import time
import model.PANTILT_MODEL
import network.I2C
import threading

class pantilt(threading.Thread):
	self.i2cAddr = 0x40

	def __init__(self):
		threading.Thread.__init__()
		self.parent 	= "None"
		self.num 		= 1
		self.model		= model.PANTILT_MODEL.pantilt()
		self.isRunning = True
		self.i2c = network.I2c.i2c(self.i2cAddr)
		self.controller	= controller.PANTILT_CONTROLLER.pantilt(model,i2c)
		self.model.pan_min=0.12
		self.model.pan_max=0.47
		self.model.tilt_min=0.26
		self.model.tilt_max=0.45


	def run(self):
		controller.start()
		#while self.isRunning:
			#have some check on pantilt behaviour like switching between manual and scan mode
			
