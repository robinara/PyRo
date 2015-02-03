import driver.DRIVER_CORE
import threading
import interface.MOTOR_CORE
import time

class quad(threading.Thread):
	
	def __init__(self,MODEL,I2C):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.isRunning 		= True
		self.driver1		= driver.DRIVER_CORE.PCA9865(0)
		self.model 		= MODEL
		self.m1 		= interface.MOTOR_CORE.DC(I2C)
		self.m2 		= interface.MOTOR_CORE.DC(I2C)
		self.m3 		= interface.MOTOR_CORE.DC(I2C)
		self.m4 		= interface.MOTOR_CORE.DC(I2C)

		self.driver1.setFreq(330)
		self.m1.setUpServo(self.model.m1_ID)
		self.m2.setUpServo(self.model.m2_ID)
		self.m3.setUpServo(self.model.m3_ID)
		self.m4.setUpServo(self.model.m4_ID)
	
	def run(self):
		while self.isRunning:
			self.mgr(self.model.mode)			
			self.m1.setServoPower(self.model.m1_power)
			self.m2.setServoPower(self.model.m2_power)
			self.m3.setServoPower(self.model.m3_power)
			self.m4.setServoPower(self.model.m4_power)
			time.sleep(self.model.refresh_rate)
		print "Controller off"

	def mgr(self,input):

		#UAV.stabilize(self.model.attitude)	
		return

