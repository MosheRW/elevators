from floor_2 import states

def get_init_position(floor, floor_position):
	pass

class button:
	def __init__(self, floor, location):
		self.__floor = floor
		self.__location
		self._img
		self._text
		self._status = states.STILL
		

	def init(self):
		pass

#-----------------------------------	
	def set(self, floor, location):
		pass
	
	def get(self):
		pass
	
	def update(self):
		pass
	
#----------------------------------
	def set_img(self, new_img):
		pass

	def set_text(self, new_text):
		pass
	
	def set_position(self, new_position):
		pass
	
#----------------------------------
#	
	def get_img(self):
		pass
	
	def get_text(self):
		pass
	
	def get_position(self):
		pass

#----------------------------------
#	
	def update_img(self):
		pass
	
	def update_text(self):
		pass
	
	def update_position(self):				#<--- Probably unnecessary
		pass
	

#----------------------------------
	def is_clicked(self)	 -> bool:
		pass

#----------------------------------
	
	def calculate_size_and_place(self):
		pass
	
	def calculate_size(self):
		pass
	
	def calculate_place(self):
		pass
	
#----------------------------------