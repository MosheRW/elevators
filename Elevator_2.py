import pygame
import Queque
import Graphic_Manager as gm
from enum import Enum

ele_status = Enum('ele_status',['GOING_UP','GOING_DOWN', 'STILL', 'DOORS_OPEN', 'INVITED'])

def get_init_position(serial, first_elevator_is = 1):      
            return (gm.FLOOR_SIZE[0] + gm.SPACE + gm.ELEVATOR_SIZE[0] + (serial - first_elevator_is) * (gm.ELEVATOR_SIZE[0] + gm.SPACE), gm.ELEVATOR_SIZE[1])

class Elevator:
    screen = gm.get_screen()
    
    def __init__(self,serial,starting_point = 0):
        pygame.init
        
        self._serial = serial
        self._position = get_init_position(0,0)
        
        self._status = ele_status.STILL
        self.img =  pygame.image.load( gm.ELEVATOR_PIC_FILE).convert()
        
        #self._time_until_clear = timer
        #self._time_to_end_status = timer
        
    def set(self):
        pass
    
    def get(self):
        pass
    
    def call(self, floor):
        pass
       
    def get_time(self, floor):
        pass
   
    def update(self):
        pass   

    def get_position(self):
        pass
    
    def set_position(self):
        pass
    
    def get_img(self):
        pass
    
    def set_img(self):
        pass
    
    def get_status(self):
        pass
    
    def set_status(self):
        pass
    
    def update_big_timer():
        pass 
    
    def update_small_timer():
        pass 