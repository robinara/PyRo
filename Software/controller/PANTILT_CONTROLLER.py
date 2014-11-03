import controller.DC
import driver.PWM
import 
import threading

class pantilt(threading.Thread):
	
	def __init__(self,MODEL,I2C):
		threading.Thread.__init__()
		self.parent 		= "None"
		self.num 			= 1
		self.isRunning 		= True
		self.driver1		= driver.PWM.PCA9865()
		self.model 			= MODEL
		self.tilt_servo 	= controller.DRIVER_CORE.DC(I2C)
		self.pan_servo 		= controller.DRIVER_CORE.DC(I2C)

		driver1.setFreq(330,I2C)
		tilt_servo.setUpServo(model.tilt_servo_ID)
		pan_servo.setUpServo(model.pan_servo_ID)
	
	def run(self):
	
		while self.isRunning:

			tilt_servo.setServo(model.tilt_angle)
			pan_servo.setServo(model.pan_angle)
		
