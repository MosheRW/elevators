
#from floor_2 import states
import Graphic_Manager as gm
import pygame
from enum import Enum
states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

def get_init_position(floor, floor_position):
	pass

class Button:
	def __init__(self, floor ,location, text):
		self.__floor = floor
		self.__position = location
		self._shape = None
		self._text = None
		self._the_text_as_str = "00:00"
		self._status = states.STILL
		

	def init(self, new_text):
		self.set_text(new_text)
		self.set_shape()

#-----------------------------------	
	def set(self, floor, location):
		pass
	
	def get(self):
		return self.get_text(), self.get_shape()
	
	def update(self, new_text, new_status):		
		self.set_status()
		self.set_text(new_text)
	
#----------------------------------
	def set_shape(self):
		self._shape = self._text.get_rect()

	def set_text(self, new_text):
		self._the_text_as_str = new_text
		self.build_the_text()

	def set_status(self, new_status):
		if self._status != new_status:
			self._status = new_status
			
	
	def set_position(self, new_position):
		self.__position = new_position
	
#----------------------------------
#	
	def get_shape(self):
		return self._shape.copy,  self.calculate_shape_position()
	
	def get_text(self):
		return self._text.copy, self.calculate_text_position()
	
	def get_position(self):
		return self.__position

#----------------------------------
#	
	def update_shape(self):				#<--- Probably unnecessary
		pass
	
	def update_text(self, new_text):		#<--- Probably unnecessary
		self._the_text_as_str = new_text
		self.build_the_text()
		
	def update_position(self,):				#<--- Probably unnecessary
		pass
	
	def build_the_text(self):
		self._text = gm.font.render(self._text,True,self.calculate_color())
#----------------------------------
	def is_clicked(self)	 -> bool:
		pass

#----------------------------------

	def calculate_shape_position(self):
		return self.get_position()
	
	def calculate_text_position(self):
		return self.get_position()
	

#----------------------------------
	
	def calculate_size_and_place(self):
		pass
	
	def calculate_size(self):
		pass
	
	def calculate_place(self):
		pass
	
#----------------------------------

	def calculate_color(self):
		black = (0,0,0)
		green = (0, 255, 0)
		
		if self.get_state() == states.WAITING:
			
			return green
		else:
			return black
		


#--------------------------------------------------------------------------

bu = Button(0, (160,160))		

bu.init("56:71")

screen = gm.get_screen()

screen.blit(bu.get_text()[0], bu.get_text()[1])
while True:
	pygame.display.flip()