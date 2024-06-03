#from Queque import Queque
from enum import Enum
from Graphic_Manager import WAIT_IN_FLOOR, get_floors_boundries
import Graphic_Manager as gm
from Timer_2 import Timer_2
import pygame


states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

def get_init_position(serial, first_floor_is = 0):
     return (0, gm.FLOOR_SIZE[1] + (serial - first_floor_is) * (gm.ELEVATOR_SIZE[0]))



class Floor_2:
    
    def __init__(self, floor = 0):
        
        self._floor = floor
        self._position = (0,0)
        
        self._status = states.STILL
        self._timer = Timer_2()
        
        self.img =  pygame.image.load(gm.FLOOR_PIC_FILE).convert()


    def init(self, floor):
        self._floor = floor
        self.set_status(states.STILL)
        self.set_position(get_init_position(floor))
        
#---------------------------------------------------------------------------------

        
    def is_this_floor_needs_an_elevator(self):
        return self.get_status() == states.STILL
    

    def get_elevator(self, time):
        self.set_status(states.WAITING)
        self.set_timer(time)
#----------------------------------------------------------------------------------
        
    def get(self):    
        return (self.get_img(), self.get_position())
    
    def update(self):
        self.update_timer()
        self.update_status()
        
  
#----------------------------------------------------------

    def get_floor(self):
        return self._floor
    
    def get_position(self):
        return self._position
    
    def get_status(self):
        assert type(self._status) == states, "ERROR, Wrong type"
        #print( self._status)
        return self._status
        #temp = self._status
        #return temp
    
    def get_timer(self):
        return self._timer.get()
    
    def get_img(self):
         return pygame.transform.scale(self.img, gm.FLOOR_SIZE)
    
#-----------------------------------------------------------

    def set_position(self,new_position):
        assert type(new_position) == tuple, "ERROR, incorrect value of new_position"
        self._position = new_position
        
    def set_status(self, new_status):
        assert type(new_status) == states, "ERROR, incorrect value of new_position"
        self._status = new_status
        self.update_img()
        
    def set_timer(self, new_time):
        self._timer.set(new_time)

    def set_img(self,filename):         #maybe need to implement another one, with state as input
       pass
    
#-------------------------------------------------------------

    def update_status(self):
        #temp =  self._status        # self.get_status()
        if  self.get_status() == states.WAITING:
        #if  temp == states.WAITING:
            if not self._timer.is_running():
                self.set_status(states.ELEVATOR_HERE)
                self.set_timer(gm.WAIT_IN_FLOOR)
                
        elif self.get_status() == states.ELEVATOR_HERE: #case elevator is here
            if not self._timer.is_running():
                self.set_status(states.STILL)

    
    def update_timer(self):
        self._timer.update()
    
    def update_img(self):                           #maybe need to implement another one, with state as inputs
        pass







#-------------------------------------------------------------
    def __str__ (self):
        return f'|floor: {self.get_floor()},  status: {self.get_status()}, timer: {self.get_timer()} |\n'
    
    def __repr__ (self):
       return f'|floor: {self.get_floor()},  status: {self.get_status()}, timer: {self.get_timer()} |\n'
        
