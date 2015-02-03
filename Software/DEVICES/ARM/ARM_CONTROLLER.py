import driver.DRIVER_CORE
import threading
import MOTOR_CORE
import time
class arm(threading.Thread):
	
	def __init__(self,MODEL,I2C):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.isRunning 		= True
		self.driver1		= driver.DRIVER_CORE.PCA9865(0)
		self.model 		= MODEL
		self.motor0	 	= MOTOR_CORE.DC(I2C)
		self.motor1	 	= MOTOR_CORE.DC(I2C)
		self.motor2	 	= MOTOR_CORE.DC(I2C)

		self.driver1.setFreq(330)
		self.motor0.setUpServo(self.model.motor0_ID)
		self.motor1.setPololuVNH5019(self.model.motor1_pin_INA,self.model.motor1_pin_INB,self.model.motor1_pin_PWM)
		self.motor2.setPololuVNH5019(self.model.motor2_pin_INA,self.model.motor2_pin_INB,self.model.motor2_pin_PWM)
	
	def run(self):
		while self.model.isRunning:
			self.mgr(self.model.state)
			#print self.model.motor0_power, self.model.motor1_power, self.model.motor2_power			
			self.motor0.setServoPower(self.model.motor0_position)
			self.motor1.setMotorPower(abs(self.model.motor1_power),self.model.motor1_dir)
			self.motor2.setMotorPower(abs(self.model.motor2_power),self.model.motor2_dir)
			time.sleep(self.model.delay)

	def mgr(self,input):
		step=0.1		
		if input=="q":
			self.model.motor0_power +=self.model.step
		if input=="a":
			self.model.motor0_power -=self.model.step
		if input=="w":
			self.model.motor1_power +=self.model.step
		if input=="s":
			self.model.motor1_power -=self.model.step
		if input=="e":
			self.model.motor2_power +=self.model.step
		if input=="d":
			self.model.motor2_power -=self.model.step

		#if input==" ":
		self.model.state=" "
		#print self.model.motor0_power
		#print self.model.motor1_power
		#print self.model.motor2_power

		return
