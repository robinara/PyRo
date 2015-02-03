CHANNEL_AMOUNT = 10

class AstronautModel(object):
	"""docstring for AstronautModel"""
	def __init__(self, number):
		super(AstronautModel, self).__init__()
		self.number = number
		self.temperature = 0 # celcius
		self.power = 0 # Battery life percent remaining
		self.link_quality = 0 # ping time (millisecond)
		self.oxygen = 0 # oxygen level(liters)
		self.body_temperature = 0 # celcius
		self.heart_rate = 0 # beats per minute
		self.co2_level = 0 # CO2 PPM
		self.heading = 0 # 0 = North, clockwise
		self.waypoint_heading = 0 # 0 = North, clockwise
		self.gps = float[]{0.0, 0.0} # [lati, long]
		self.distance_waypoint = 0 # meters
		self.channel_listen = range(CHANNEL_AMOUNT) # channel to broadcast to
		self.channel_send   = range(CHANNEL_AMOUNT)