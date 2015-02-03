import time
import QUAD_MODEL
import QUAD_CONTROLLER
import network.I2C
import threading
import DOF10IMU
import UAV


class quad(threading.Thread):
	i2cAddr = 0x40

	def __init__(self):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.model		= QUAD_MODEL.quad()
		self.isRunning 		= True
		self.i2c 		= network.I2C.i2c(self.i2cAddr)
		self.motors		= QUAD_CONTROLLER.quad(self.model,self.i2cAddr)
		self.dof10		= DOF10IMU.imu(self.model)
		self.avionics		=UAV.uav(self.model)


	def run(self):
		self.motors.start()
		self.dof10.start()
		self.model.start()
		print "Initializing System"
		time.sleep(3)
		
		self.avionics.start()
		while self.isRunning:
			#time.sleep(0.5)
			print self.model.x_accel,self.model.y_accel,self.model.z_accel,self.model.m1_power,self.model.m2_power,self.model.m3_power,self.model.m4_power
		
			#print self.model.temperature,self.model.imu[0],self.model.x_accel,self.model.gyro,self.model.m1_power
			if self.motors.isRunning==False:
				self.isRunning=False
				self.dof10.isRunning=False
				self.model.isRunning=False
				self.avionics.isRunning=False

	def act(self):
		input = raw_input()

		if input=="quad":
			self.model.mode="quad"
		return

	
 
			
if __name__ == "__main__":

	device = quad()
	device2 = quad()
	device.start()
	
	try:
		while True:
			device.act()
			print device.model.mode

	except KeyboardInterrupt:
		device.isRunning = False
		device.motors.isRunning=False
		device.dof10.isRunning=False
		print "Device Terminated"



		
