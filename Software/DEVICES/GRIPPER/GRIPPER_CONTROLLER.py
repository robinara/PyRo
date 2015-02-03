import driver.DRIVER_CORE
import threading
import interface.MOTOR_CORE
import time
class gripper(threading.Thread):
	
	def __init__(self,MODEL,I2C):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.isRunning 		= True
		self.driver1		= driver.DRIVER_CORE.PCA9865(0)
		self.model 		= MODEL
		self.left_servo 	= interface.MOTOR_CORE.DC(I2C)
		self.right_servo 	= interface.MOTOR_CORE.DC(I2C)
		self.roll_servo 	= interface.MOTOR_CORE.DC(I2C)
		self.roll2_servo 	= interface.MOTOR_CORE.DC(I2C)

		self.driver1.setFreq(330)
		self.left_servo.setUpServo(self.model.left_servo_ID)
		self.right_servo.setUpServo(self.model.right_servo_ID)
		self.roll_servo.setUpServo(self.model.roll_servo_ID)
		self.roll2_servo.setUpServo(self.model.roll2_servo_ID)
	
	def run(self):
		while self.isRunning:
			self.mgr(self.model.mode)			
			self.left_servo.setServoPower(self.model.left_position)
			self.right_servo.setServoPower(self.model.left_position)
			self.roll_servo.setServoPower(self.model.left_position)
			self.roll2_servo.setServoPower(self.model.left_position)
			time.sleep(self.model.delay)
			print self.model.left_position

	def mgr(self,input):
		self.model.delay =0.03	

		if input=="quad":
			self.quadscan()	
		if input=="open":
			self.gopen()
		if input=="close":
			self.gclose()
		if input=="":
			self.stop()
			
		if input=="rollLeft":
			self.ccw()
		if input=="pokh":
			print "pokhing"
			self.model.delay=1
			if self.model.pokhing=="off":
				self.model.left_position = self.model.left_max
				self.model.right_position = self.model.right_max
				self.model.pokhing = "on"
				print "first move"

			if self.model.pokhing=="on":
				if self.model.left_position==self.model.left_min:
					self.model.left_position = self.model.left_max
					self.model.right_position = self.model.right_max
					print "first move"
				elif self.model.left_position==self.model.left_max:
					self.model.left_position = self.model.left_min
					self.model.right_position = self.model.right_min
					print "second move"	
		
		if input=="demo":
			if self.model.demo=="off":
				self.model.delta=0.0005
				self.model.demo="on"
				self.model.right_position = self.model.right_max
				self.model.left_positGRIPPER_CONTROLLERion = self.model.left_min
				self.model.roll_position = self.model.roll_max
				print "demo"
		
				
			if self.model.demo=="on":
				self.demo()
		

		if input=="twistOpenDemo":
			
			if self.model.twistOpenDemo=="off":
				self.model.delta=0.008

				self.model.twistOpenDemo="on"
				self.model.right_position = self.model.right_max
				self.model.left_position = self.model.left_min
				self.model.roll_position = self.model.roll_min
				print "loaded"

			if self.model.twistOpenDemo=="on":
				self.twistOpenDemo()
				print "twisty"
		
		if self.model.twist=="on":
			delay=0.3
			if self.model.twist_step == 0:
				self.model.mode="open"
				time.sleep(delay)
				self.model.twist_step = 1
			elif self.model.twist_step == 1:
				self.model.mode="rollRight"
				time.sleep(delay)
				self.model.twist_step = 2
			elif self.model.twist_step == 2:
				self.model.mode="close"
				time.sleep(delay)
				self.model.twist_step = 3
			elif self.model.twist_step == 3:
				self.model.mode="rollLeft"
				time.sleep(delay)
				self.model.twist_step = 0
		
                    

			
	def stop(self):
		self.model.left_position = 0
		print "stop"
		return

	def ccw(self):
		self.model.roll_position = self.model.roll_max

	def gopen(self):
		#self.model.right_position = self.model.right_max
		self.model.left_position += 0.001
		self.model.mode="none"

	def gclose(self):
		#self.model.right_position = self.model.right_min
		self.model.left_position -= 0.001
		self.model.mode="none"
	def demo(self):
		delta = self.model.delta
		self.model.left_position  += delta
		self.model.right_position += -delta
		self.model.roll_position += delta
		if self.model.left_position < self.model.left_max:
			self.model.delta = -self.model.delta
                if self.model.left_position > self.model.left_min:
                        self.model.delta = -self.model.delta

		time.sleep(0.02)
		#print "position right,left,roll: ", self.model.right_position, self.model.left_position, self.model.roll_position
		return
	
	def twistOpenDemo(self):
		delta = self.model.delta
		self.model.left_position +=self.model.delta
		self.model.right_position +=-self.model.delta
		self.model.roll_position +=self.model.delta
		if self.model.left_position < self.model.left_max:
			self.model.delta = -self.model.delta
                if self.model.left_position > self.model.left_min:
                        self.model.delta = -self.model.delta
		time.sleep(0.00001)
		print "twisting"
			
	def quadscan(self):
		self.model.left_position +=self.model.delta
		if self.model.left_position < self.model.left_max:
			self.model.delta = -self.model.delta
                if self.model.left_position > self.model.left_min:
                        self.model.delta = -self.model.delta
		time.sleep(0.001)
		print self.model.left_position
		self.model.mode="none"
