import Graphic_Manager as gm
import pygame
from enum import Enum

states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

class Button:
	def __init__(self ,position, text = "00:00", color = "white", backround = True):
		
		self.__position = position		#store the euclidean location
		self._status = states.STILL		#the status of the floor button, one from the three availables above.(enum. initilize to still)
					
		self._the_text_as_str = text										#the text to show
		self._text = gm.font.render("hello",True,self.calculate_color())	#the actual surface of the text (pygame object)
		
		self._backround_color = color										#the backround color code
		self._backround = backround											#boolean value. if the backround is clear or with color
		
		self.__rect = self._text.get_rect(bottomleft = self.get_position())	#rect pygme object. the area of the button.(use to click calulation)
		self._shape = pygame.Surface((self.getrect().w, self.getrect().h))	#surface object. use to store the bacround of the text button
		
		if self._backround :			#if backround is true: coloring the backround shapes
			self._shape.fill(self._backround_color)
		
#-----------------------------------		
		#initilize the button
	def init(self, new_text):
		self.__set_text(new_text)
		self.__set_shape()

#-----------------------------------	
	#set the button location, text, colors of the text and backround, and status.
	def set(self, position, text = "00:00", color = "white", backround = True, status = states.STILL):
		self.__set_position(position)
		self.__set_text(text)
		self.__set_shape()		
		self._backround = backround
		
		if  self._backround:
			self.__set_backround_color(color)
		self.__set_status(status)		
		
	#get the graphical represntations and Euclidean location of the button in a tuple		
	def get(self):
		return self.get_text(), self.get_shape(), self.get_position()
	
	#updates the status, the text and the text color.
	def update(self, new_text, new_status):		
		self.__set_status(new_status)		
		self.__set_text(new_text)
	
#----------------------------------
	#return boolean value. if the button clicked
	def is_clicked(self, mous_pos)	 -> bool:
		return self.getrect().collidepoint(mous_pos)
	
#----------------------------------
	def __set_shape(self):
		self._shape = pygame.Surface((self.getrect().w, self.getrect().h))
		self.__set_backround_color(self._backround_color)
				
	def __set_text(self, new_text):
		self._the_text_as_str = new_text
		self.__build_the_text()
		self.__rect = self._text.get_rect(bottomleft = self.get_position())

	def __set_status(self, new_status):
		if self._status != new_status:
			self._status = new_status			
	
	def __set_position(self, new_position):
		self.__position = new_position
		
	def __set_backround_color(self, new_color):
		if self._backround :
			self._shape.fill(new_color)
		
	
#----------------------------------
	
	def get_shape(self):
		return self._shape
	
	
	def get_text(self):
		return self._text
	
	def getrect(self):		
		return self.__rect
	
	def get_position(self):
		return self.__position

	def get_state(self):
		return self._status
	
#----------------------------------
	
	def __build_the_text(self):
		self._text = gm.font.render(self._the_text_as_str,True,self.calculate_color())
	
#----------------------------------

	def calculate_color(self):
		if self.get_state() == states.WAITING:	
			return (0,255,0)	#green		
		return (0,0,0)	#black
		
