import threading
#import controller.adxl355  #import libary for various sensors and functions.
#import controller.mapping #i.e. a library that provides geodetic functionality to spatial information.

class MPS(threading.Thread):

	def __init__(self,MODEL):
		threading.Thread.__init__()
		self.num=1
		self.parent="None"
		self.model=MODEL
