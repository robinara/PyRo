class arm:
	def __init__(self):
		self.motor0_power	= 0
		self.motor1_power	= 0
		self.motor2_power	= 0
		self.motor0_dir		= 0
		self.motor1_dir		= 0
		self.motor2_dir		= 0
		self.motor0_position	= 0
		self.motor1_pin_INA	= 1
		self.motor1_pin_INB	= 3
		self.motor1_pin_PWM	= 2
		self.motor2_pin_INA	= 4
		self.motor2_pin_INB	= 5
		self.motor2_pin_PWM	= 6
		self.state		= "off"
		self.delay		=0.1
		self.motor0_ID		=0
		self.isRunning		=True
		self.maxPower		=1
		self.step		=0.1
