
#from floor_2 import states
import Graphic_Manager as gm
import pygame
from enum import Enum
states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

def get_init_position(floor, floor_position):
	pass

class Button:
	def __init__(self ,location, text = "00:00", color = "white"):
		
		self.__position = location
		self._status = states.STILL
		
		self._backround_color = color
		
		self._the_text_as_str = text
		#self._text = gm.font.render(self._the_text_as_str,True,self.calculate_color())
		self._text = gm.font.render("hello",True,self.calculate_color())
		
		self._shape = pygame.Surface((self.getrect().w, self.getrect().h))
		self._shape.fill(self._backround_color)
		
		

	def init(self, new_text):
		self.set_text(new_text)
		self.set_shape()

#-----------------------------------	
	def set(self, location, text = "00:00", color = "white", status = states.STILL):
		self.set_position(location)
		self.set_backround_color(color)
		self.set_text(text)
		self.set_shape()
		self.set_status(status)
		
	
	def get(self):
		return self.get_text(), self.get_shape(), self.getrect()
	
	def update(self, new_text, new_status):		
		self.set_status(new_status)
		self.set_text(new_text)
	
#----------------------------------
	def set_shape(self):
		self._shape = pygame.Surface((self.getrect().w, self.getrect().h))
		self._shape.fill("gray")
		#self._shape = self._text.get_rect()
		#self._shape.center = (gm.WINDOW_SIZE[0] //2, gm.WINDOW_SIZE[1] //2 )
		
		#self._shape.x, self._shape.y = self.get_position()

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
		return self._shape
	
	
	def get_text(self):
		return self._text
	
	def getrect(self):
		return self._text.get_rect()
	
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
		self.build_the_text()
		
	def update_position(self,):				#<--- Probably unnecessary
		pass
	
	def build_the_text(self):
		self._text = gm.font.render(self._the_text_as_str,True,self.calculate_color())
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

"""
pygame.init()
"""

"""
bu = Button(0, (160,160), "57")		

bu.init("56:71")

screen = gm.get_screen()
clock = pygame.time.Clock()

screen.fill("white")
#screen.blit(bu.get_text()[0], bu.get_shape()[0])
while True:
	screen.fill("white")
	screen.fill("black")
	screen.fill("white")
	screen.blit(bu.get_shape(),(160,160))
	screen.blit(bu.get_text(), (160,160))
	
	#screen.draw.
	#screen.blit(bu.get_shape()[0], bu.get_shape()[1])
	#screen.blit(bu.get_shape()[0],  bu.get_shape()[1][0]) #, bu.get_shape()[1][1])
	pygame.display.flip()

	clock.tick(60)
	"""