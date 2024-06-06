
#from floor_2 import states
import Graphic_Manager as gm
import pygame
from enum import Enum

states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

class Button:
	def __init__(self ,position, text = "00:00", color = "white", backround = True):
		
		self.__position = position		
		self._status = states.STILL
					
		self._the_text_as_str = text
		self._text = gm.font.render("hello",True,self.calculate_color())
		
		self._backround_color = color
		self._backround = backround
		
		self._shape = pygame.Surface((self.getrect().w, self.getrect().h))
		

		if self._backround :
			self._shape.fill(self._backround_color)
		
	
		

	def init(self, new_text):
		self.set_text(new_text)
		self.set_shape()

#-----------------------------------	
	def set(self, location, text = "00:00", color = "white", status = states.STILL):
		self.set_position(location)
		self.set_text(text)
		self.set_shape()
		self.set_backround_color(color)
		self.set_status(status)
		
	
#----------------------------------
	def is_clicked(self, mous_pos)	 -> bool:
		return self.getrect().collidepoint(mous_pos)

#---------------------------------
			
	def get(self):
		return self.get_text(), self.get_shape(), self.get_position()
	
	def update(self, new_text, new_status):		
		self.set_status(new_status)
		
		self.set_text(new_text)
	
#----------------------------------
	def set_shape(self):
		self._shape = pygame.Surface((self.getrect().w, self.getrect().h))
		self.set_backround_color(self._backround_color)
		
	def set_text(self, new_text):
		self._the_text_as_str = new_text
		self.__build_the_text()

	def set_status(self, new_status):
		if self._status != new_status:
			self._status = new_status			
	
	def set_position(self, new_position):
		self.__position = new_position
		
	def set_backround_color(self, new_color):
		if self._backround :
			self._shape.fill(new_color)
		
	
#----------------------------------
#	
	def get_shape(self):
		return self._shape
	
	
	def get_text(self):
		return self._text
	
	def getrect(self):			
		rect =  self._text.get_rect(bottomleft = self.get_position())
		return rect
	
	def get_position(self):
		return self.__position

	def get_state(self):
		return self._status
#----------------------------------
#	
	def update_shape(self):				#<--- Probably unnecessary
		pass
	
	def update_text(self, new_text):		#<--- Probably unnecessary
		self._the_text_as_str = new_text
		self.__build_the_text()
		
	def update_position(self,):				#<--- Probably unnecessary
		pass
	
	def __build_the_text(self):
		self._text = gm.font.render(self._the_text_as_str,True,self.calculate_color())
	
#----------------------------------

	def calculate_color(self):
		if self.get_state() == states.WAITING:	
			return (0,255,0)	#green		
		return (0,0,0)	#black
		


#--------------------------------------------------------------------------

