#import driver
import time
import threading
import driver.LSM303
import driver.BMP085
import driver.L3GD20

class imu(threading.Thread):

	def __init__(self,MODEL):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 2
		self.model		= MODEL
		self.isRunning 		= True
		#self.i2c 		= network.I2C.i2c(self.i2cAddr)
		self.lsm		= driver.LSM303.Adafruit_LSM303()
		self.BMP085		= driver.BMP085.BMP085()
		self.lg3d20		= driver.L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

	def run(self):
		self.calibrate()
		while self.isRunning:
			self.mgr(self.model.mode)			
			self.model.temperature =  self.BMP085.readTemperature()
			self.model.imu	=	self.lsm.read()
			self.model.gyro	= 	self.l3gd20.Get_CalOut_Value()
			time.sleep(self.model.refresh_rate)
		print "10DOF controller off"

	def calibrate(self):
		# Preconfiguration
		self.l3gd20.Set_PowerMode("Normal")
		self.l3gd20.Set_FullScale_Value("250dps")
		self.l3gd20.Set_AxisX_Enabled(True)
		self.l3gd20.Set_AxisY_Enabled(True)
		self.l3gd20.Set_AxisZ_Enabled(True)

		# Print current configuration
		self.l3gd20.Init()
		self.l3gd20.Calibrate()

