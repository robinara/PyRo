import threading
import time
class speed(threading.Thread):

	def __init__(self,MODEL):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.isRunning 		= True
		self.model		= MODEL
	
	def run(self):
		while self.model.isRunning:
			if self.model.motor0_power >= 0:
				self.model.motor0_dir = 1
				#self.model.motor0_PWM = abs(self.model.motor0_power)
			elif self.model.motor0_power < 0:
				self.model.motor0_dir = -1
				#self.model.motor0_PWM = abs(self.model.motor0_power)			
			if self.model.motor1_power >= 0:
				self.model.motor1_dir = 1
				#self.model.motor1_PWM = abs(self.model.motor1_power)
			elif self.model.motor1_power < 0:
				self.model.motor1_dir = -1
				#self.model.motor1_PWM = abs(self.model.motor1_power)
			if self.model.motor2_power >= 0:
				self.model.motor2_dir = 1
				#self.model.motor2_PWM = abs(self.model.motor2_power)
			elif self.model.motor2_power < 0:
				self.model.motor2_dir = -1
				#self.model.motor2_PWM = abs(self.model.motor2_power)

			#Safety Checks
			if (self.model.motor2_power >= self.model.maxPower):
				self.model.motor2_power =   self.model.maxPower
			if (self.model.motor2_power <= -self.model.maxPower):
				self.model.motor2_power =   -self.model.maxPower
			if (self.model.motor1_power >= self.model.maxPower):
				self.model.motor1_power =   self.model.maxPower
			if (self.model.motor1_power <= -self.model.maxPower):
				self.model.motor1_power =   -self.model.maxPower
			#State Check
			if self.model.state == "stop":
				self.model.motor0_power = 0
				self.model.motor1_power = 0
				self.model.motor2_power = 0

			time.sleep(self.model.delay)
