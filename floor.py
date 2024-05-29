from Queque import Queque
from enum import Enum
from Graphic_Manager import WAIT_IN_FLOOR, get_floors_boundries
import Graphic_Manager as gm
from timer import timer


from updatable_pic_model import UPM

states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

class Floor(UPM):
    def __init__(self, floor = 0, position = 0):
        #super.__init__('Floor')
        super().__init__(floor, gm.FLOOR_PIC_FILE, get_init_position(floor))

        #super
        self._state = states.STILL


    def is_this_floor_needs_an_elevator(self):
        return self._state == states.STILL
    
    def get_elevator(self, exact_time):
        self._state = states.WAITING
        self._timer.set(exact_time[0], exact_time[1])


    def update(self):
        self.__update_timer()
        self.__update_status()
        
    def __update_timer(self):
        self._timer.update()
        
    def __update_status(self):
        if  self._state == states.STILL:
            pass
        elif  self._state == states.WAITING:
            if self._timer.is_time_is_up():
                self._state = states.ELEVATOR_HERE
                self._timer.set(2)
        else: #case elevator is here
            if self._timer.is_time_is_up():
                self._state = states.STILL
         
    def __str__ (self):
        return f'floor: {self._floor}, ' + UPM.__str__(self)
    
    def __repr__ (self):
        return f'floor: {self._floor}' + UPM.__repr__(self)
        



def get_init_position(serial, first_floor_is = 0):
     return (0, gm.FLOOR_SIZE[1] + (serial - first_floor_is) * (gm.ELEVATOR_SIZE[0]))