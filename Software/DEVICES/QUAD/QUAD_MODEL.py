import threading

class quad(threading.Thread):

	imu			= [(1,1,1),(1,1,1)]
	accel			= imu[0]
	mag			= imu[1]
	gyro			= [(0,0,0),(0,0,0),(0,0,0)]
	m1_power 		= 0.0
	m2_power 		= 0.0
	m3_power 		= 0.0
	m4_power 		= 0.0
	m_min			= 0.3
	m_max			= 0.37
	m1_ID			= 0
	m2_ID			= 2
	m3_ID			= 1
	m4_ID			= 3
	mode 			= 0
	refresh_rate		= 0.002
	isRunning		= True
	x_accel			= imu[0][0]
	y_accel			= imu[0][1]
	z_accel			= imu[0][2]
	x_mag			= imu[1][0]
	y_mag			= imu[1][1]
	z_mag			= imu[1][2]
	x_gyro			= gyro[0]
	y_gyro			= gyro[1]
	z_gyro			= gyro[2]
	x_position		= 0
	y_position		= 0
	z_position		= 0
	temperature		= 0
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.parent 		= "None"
		self.num 		= 1
		self.isRunning 	= True
		print "Quad Model ready"

	def run(self):

		while self.isRunning:
			self.accel			= self.imu[0]
			self.mag			= self.imu[1]
			self.x_accel			= self.imu[0][0]
			self.y_accel			= self.imu[0][1]
			self.z_accel			= self.imu[0][2]
			self.x_mag			= self.imu[1][0]
			self.y_mag			= self.imu[1][1]
			self.z_mag			= self.imu[1][2]
			self.x_gyro			= self.gyro[0]
			self.y_gyro			= self.gyro[1]
			self.z_gyro			= self.gyro[2]

