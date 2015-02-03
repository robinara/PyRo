import sys
import time
import threading
import pygame
from pygame.locals import *

class LogitechGamepadModel:
	def __init__(self):
		self.name 			= 'LogitechGamepad'
		self.axisLX 		= 0
		self.axisLY 		= 0
		self.axisRX 		= 0
		self.axisRY 		= 0
		self.buttonA 		= 0
		self.buttonB 		= 0
		self.buttonX 		= 0
		self.buttonY 		= 0
		self.buttonLB 		= 0
		self.buttonRB 		= 0
		self.buttonLT 		= 0
		self.buttonRT 		= 0
		self.buttonBack 	= 0
		self.buttonStart	= 0
		self.dPadLeft 		= 0
		self.dPadRight 		= 0
		self.dPadUp 		= 0
		self.dPadDown 		= 0
		self.gamepad 		= 0
		self.isRunning		= True
		print 'created LogitechGamepadModel'
