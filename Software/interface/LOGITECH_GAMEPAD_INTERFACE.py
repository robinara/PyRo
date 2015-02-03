import sys
import time
import threading
import pygame
from pygame.locals import *
import LOGITECH_GAMEPAD_DRIVER
import LOGITECH_GAMEPAD_MODEL

class LogitechGamepadInterface(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.isRunning=True
		self.num=1
		self.parent=None
		self.model=LOGITECH_GAMEPAD_MODEL.LogitechGamepadModel() 
		print 'created LogitechGamepadInterface'	

	def run(self):
		driver  = LOGITECH_GAMEPAD_DRIVER(self.model)
		while isRunning:
			if self.model.axisLX > 0.5:
				driver.endThreads()
				self.model.isRunning = False
				self.isRunning = False
				print "Error Condition Reached. Device Terminated"
			else:
				pass

				
			
