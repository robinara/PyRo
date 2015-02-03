
class MPS:
	"""docstring for Martian Personal Simulator Model"""
	def __init__(self):
		self.name 				= "ASTRONAUT"
		self.temperature 		= 0 # body
		self.power 				= 0 # Battery life percent remaining
		self.link_delay 		= 0 # ping time (millisecond)
		self.O2		 			= 0 # oxygen level(liters)
		self.body_temperature 	= 0 # celcius
		self.heart_rate 		= 0 # beats per minute
		self.co2_level 			= 0 # CO2 PPM
		self.heading 			= 0 # 0 = North, clockwise
		self.waypoint_heading 	= 0 # 0 = North, clockwise
		self.gps 				= 0 # [lat, long]
		self.distance_waypoint 	= 0 # meters
		self.channel_listen 	= 0 # channel to broadcast to
		self.channel_send   	= 0
		self.heading_current	= 0
		self.heading_wpt		= 0
		self.lat				= 0
		self.long				= 0
		self.WPdistance			= 0 #measured to current waypoint 
