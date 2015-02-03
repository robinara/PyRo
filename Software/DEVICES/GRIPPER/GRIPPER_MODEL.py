
#import model.model as MODEL

class gripper():

	def __init__(self):
		self.left_position 	= 0.28
		self.right_position	= 0 
		self.roll_position 	= 0
		self.roll_min		= 0.29
		self.roll_max		= 0.5
		self.left_min		= 0.3
		self.left_max		= 0.4
		self.right_min		= 0.33	
		self.right_max		= 0.38
		self.left_servo_ID	= 0
		self.right_servo_ID	= 1
		self.roll_servo_ID	= 2
		self.roll2_servo_ID	= 3 
		self.mode 		= 0
		self.demo		= "off"
		self.delta		= 0.002
		self.twist_step		= 0
		self.twist		="off"
		self.twist_done		= 0
		self.twistOpenDemo	="off"
		self.delay	=0.3
		self.pokhing		= "off"
		

