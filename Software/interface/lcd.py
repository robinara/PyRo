import network.utilities
import driver.lcd
import time
from controller.lineStuffer import *
import threading 

base_station="192.168.1.101"
timeout=2

class MPS(threading.Thread):
		
	def __init__(self):
		#Define model parameters

		threading.Thread.__init__(self)
		self.isRunning=True
		self.num=1
		self.HARDWARE="HW"
		self.BIOMETRICS="BIO"
		self.NAV="NAV"
		self.parent=None
		self.display="HW"
		self.lcd = lcddriver.lcd()
		self.lcd.lcd_display_string(stuffline("RoboDisplay ACTIVE"), 1)
		#lcd.lcd_backlight(1)
		time.sleep(0.5)
		#lcd.lcd_backlight(0)
		j=1
		i=1
		#clear_line="                     "
		waiting="."
		while j<10:
		
			self.lcd.lcd_display_string(stuffline("Initializing"+waiting), 2)
			waiting+="."
			#print waiting
			i+=1
			if i>4:
				#lcd.lcd_display_string("Initializing     ",2)
				waiting="."
				i=1	
			j+=1
			time.sleep(1)
		#clear_line="                     "
		#lcd.lcd_display_string(clear_line,2)	
		self.lcd.lcd_display_string(stuffline("Complete"), 2)
		time.sleep(1)

	def run(self):
		print "Display running"
		while self.isRunning:
			if self.display==self.HARDWARE:
				print "HW selected"
				self.hardwareDisplay()
			if self.display==self.BIOMETRICS:
				print "BIO Selected"
				self.bioDisplay()
			if self.display==self.NAV:
				print "NAV Selected"
				self.navDisplay()

	def end(self):
		self.isRunning=False

	def hardwareDisplay(self):
		
		i=1
		power="Power: "
		Temperature="Temperature: "
		link="Link Quality: "

		while self.display==self.HARDWARE:
			#input=raw_input()
			link_lat=network.utilities.ping(base_station,timeout)*1000
			link_lat="%0.1f"%link_lat
			self.lcd.lcd_display_string(stuffline("System Operational"),1)
			self.lcd.lcd_display_string(stuffline(Temperature+str(i)+"C"),2)
			self.lcd.lcd_display_string(stuffline(power+str(100-i)+"%"), 3)
			self.lcd.lcd_display_string(stuffline(link+link_lat+"ms"), 4)
			i+=1
			if i>29:
				i=1
			time.sleep(0.5)

	def bioDisplay(self):
		
		i=1
		power="HR: "
		temperature="BODY TEMP: "
		link="Link Quality: "

		while self.display==self.BIOMETRICS:
			#input=raw_input()
		
			self.lcd.lcd_display_string(stuffline("OXYGEN: "+str(1+i/10.0)+"L"),1)
			self.lcd.lcd_display_string(stuffline(temperature+str(29+i/29)+str(i)+"C"),4)
			self.lcd.lcd_display_string(stuffline(power+str(100-i)+"BPM"), 3)
			self.lcd.lcd_display_string(stuffline("CO2: "+str(40+2*i)+"ppm"), 2)
			i+=1
			if i>29:
				i=1
			time.sleep(0.5)

	def navDisplay(self):
		
		i=1
		heading_current="Heading: "
		heading_wpt="WPT Heading: "
		position="UTM: "
		distance="D2WPT: "

		while self.display==self.NAV:
			#input=raw_input()
		
			self.lcd.lcd_display_string(stuffline(heading_current+str(245)),1)
			self.lcd.lcd_display_string(stuffline(heading_wpt+str(230)),2)
			self.lcd.lcd_display_string(stuffline(position+"1234.3N,1105.1E"), 3)
			self.lcd.lcd_display_string(stuffline(distance+str(199.3)+"m"), 4)
			#i+=1
			#if i>29:
			#	i=1
			time.sleep(0.5)
