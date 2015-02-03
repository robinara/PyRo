import sys
import time
import threading
import pygame
from pygame.locals import *

class LogitechGamepadDriver:

	def __init__(self, MODEL,gamepad=0):
		self.model=MODEL
		pygame.init()
		print 'joystick:',pygame.joystick.get_count()
		if pygame.joystick.get_count() > 0:
			self.gamepad = gamepad
			driver.init_joystick()
			self.isRunning = True
			self.thread = self.GamepadThread(self, 1, self.doStuff, 0.001)
		else:
			print 'no gamepad detected!'
		print 'created LogitechGamepadDriver'

	def startThreads(self):
		if pygame.joystick.get_count() > 0:
			self.thread.start()

	def endThreads(self):
		self.isRunning = False

	# Set joystick information.
	# The joystick needs to be plugged in before this method is called (see main() method)
	def init_joystick(self):
		joystick = pygame.joystick.Joystick(self.gamepad)# num = ID
		joystick.init()
		self.joystick = joystick
		self.joystick_name = joystick.get_name()
		self.numAxis = self.joystick.get_numaxes()
		self.numBalls = self.joystick.get_numballs()
		self.numButtons = self.joystick.get_numbuttons()
		self.numHats = self.joystick.get_numhats()
		print 'name    :',self.joystick_name
		print 'axis    :',self.numAxis
		print 'balls   :',self.numBalls
		print 'buttons :',self.numButtons
		print 'hats    :',self.numHats
		self.prevAxis = list()
		for i in range(self.numAxis):
			self.prevAxis.append(0)
		self.prevBalls = list()
		for i in range(self.numBalls):
			self.prevBalls.append(0)
		self.prevButtonsUp = list()
		for i in range(self.numButtons):
			self.prevButtonsUp.append(0)
		self.prevButtonsDown = list()
		for i in range(self.numButtons):
			self.prevButtonsDown.append(0)
		self.prevHats = list()
		for i in range(self.numHats):
			self.prevHats.append(0)
		
	def doStuff(self):
		for event in pygame.event.get():
			eventType = event.type
			if eventType == JOYAXISMOTION:
				for i in range(self.numAxis):
					axis = self.joystick.get_axis(i)
					if self.prevAxis[i] != axis:
						self.prevAxis[i] = axis
						self.axisEvent(i, axis)
			elif eventType == JOYBALLMOTION:
				for i in range(self.numBalls):
					ball = self.joystick.get_ball(i)
					if self.prevBalls[i] != ball:
						self.prevBalls[i] = ball
						self.ballEvent(i, ball)
			elif eventType == JOYHATMOTION:
				for i in range(self.numHats):
					hat = self.joystick.get_hat(i)
					if self.prevHats[i] != hat:
						self.prevHats[i] = hat
						self.hatEvent(i, hat)
			elif eventType == JOYBUTTONUP:
				for i in range(self.numButtons):
					button = self.joystick.get_button(i)
					if self.prevButtonsUp[i] != button:
						self.prevButtonsUp[i] = button
						self.buttonUpEvent(i, button)
			elif eventType == JOYBUTTONDOWN:
				for i in range(self.numButtons):
					button = self.joystick.get_button(i)
					if self.prevButtonsUp[i] != button:
						self.prevButtonsUp[i] = button
						self.buttonDownEvent(i, button)

	def axisEvent(self, num, axis):
		if num == 0:
			self.model.axisLX = axis
		elif num == 1:
			self.model.axisLY = axis
		elif num == 2:
			self.model.axisRX = axis
		elif num == 3:
			self.model.axisRY = axis

	def ballEvent(self, num, ball):
		pass

	def hatEvent(self, num, hat):
		pass

	def buttonUpEvent(self, num, button):
		if num == 0:
			self.model.buttonA = button
		elif num == 1:
			self.model.buttonB = button
		elif num == 2:
			self.model.buttonX = button
		elif num == 3:
			self.model.buttonY = button
		elif num == 4:
			self.model.buttonLB = button
		elif num == 5:
			self.model.buttonRB = button
		elif num == 6:
			self.model.buttonLT = button
		elif num == 7:
			self.model.buttonRT = button
		elif num == 8:
			self.model.buttonBack = button
		elif num == 9:
			self.model.buttonStart = button

	def buttonDownEvent(self, num, button):
		if num == 0:
			self.model.buttonA = button
		elif num == 1:
			self.model.buttonB = button
		elif num == 2:
			self.model.buttonX = button
		elif num == 3:
			self.model.buttonY = button
		elif num == 4:
			self.model.buttonLB = button
		elif num == 5:
			self.model.buttonRB = button
		elif num == 6:
			self.model.buttonLT = button
		elif num == 7:
			self.model.buttonRT = button
		elif num == 8:
			self.model.buttonBack = button
		elif num == 9:
			self.model.buttonStart = button

	class GamepadThread(threading.Thread):
		def __init__(self, parent, num, doStuff, delay):
			threading.Thread.__init__(self)
			self.parent = parent
			self.num = num
			self.doStuff = doStuff
			self.delay = delay

		def run(self):
			print 'thread',self.num,':','started'
			isRunning = True
			while isRunning and self.parent.isRunning:
				self.doStuff()
				time.sleep(self.delay)
			print 'thread',self.num,':','ended'


def main(gamepad=0):
	pygame.init()
	# input_manager = LogitechGamepadDriver()
	# input_manager.startThreads()

if __name__ == '__main__':
	main(int(sys.argv[1]))
