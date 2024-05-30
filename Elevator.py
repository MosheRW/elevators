import random
from Queque import Queque
from Queque import test
from enum import Enum
from Graphic_Manager import WAIT_IN_FLOOR, get_floors_boundries
import Graphic_Manager as gm
from timer import timer


from updatable_pic_model import UPM


directions = Enum('directions', ['GOING_UP','GOING_DOWN', 'STILL', 'DOORS_OPEN'])

class Elevator(UPM):
    __last_in_line = 0
    _queque = Queque()
    __current_ride = timer()
    def __init__(self, floor = 0, position = 0, serial = 0):
        
        super().__init__(floor, gm.ELEVATOR_PIC_FILE, get_init_position(floor))
        
        self.serial = serial
        
        self.__last_in_line = self._floor
                    
        self._state = directions.STILL
        

    def set_position(self, position):
         self._position =  position

    def set_the_new_time(self, floor):
        
        #currentTime + time to travel to the new location + timePos ther 
        print('elevator.add the new time')
        time_to_add = self.__calculate_addition_time(floor)
        print(f'time_to_add: {time_to_add}')
        self._timer.change_time(time_to_add[0],time_to_add[1])
           
    def get_the_elevator(self, floor):
        
        self._queque.push(floor)
        self._last_in_line = floor
        self.set_the_new_time(floor)
       # self._state = 
        self.__calculate_if_got_invited()
        
        
        return (self._timer.get_exact()[0] - 2, self._timer.get_exact()[1])

 
    def to_get_the_elevator(self, floor):       
        return self._timer.get_exact_with_addition(self.__calculate_addition_time(floor))
     

    def update(self, floors, time = 0.17) :
        
        self.update_()
        
        self.__update_pos()
        self.__update_iternal_timer()
        self.__update_state( floors)
  
        

    def __update_pos(self):
   
        if self._state == directions.GOING_UP:
            self._position = (self._position[0], self._position[1] +1)
            
        elif self._state == directions.GOING_DOWN:
            self._position = (self._position[0], self._position[1] -1)
                  
    def __update_state(self, floors):#to heandle
        # on the way - calculate if arrived(using_time)
        # still - calculate if got invited
        # doors open - calculate if time to close
        
       # print(self._queque)
        if self._state == directions.GOING_DOWN or  self._state == directions.GOING_UP:
            self.__calculate_if_arrived()
        elif self._state == directions.DOORS_OPEN:
            self.__calculate_if_time_to_close()
        else:
            self.__calculate_if_got_invited()
          
    def __update_iternal_timer(self):
        self.__current_ride.update()
       

    def __calculate_if_arrived(self):     #going_up, going_down
        if self.__current_ride.get_exact() == (0,0):
            
            self._state = directions.DOORS_OPEN
            self.__current_ride.set_exact(int(WAIT_IN_FLOOR),0)

            self._floor = self._queque.pop()
        
    def  __calculate_if_time_to_close(self):  #doors_open
        if self.__current_ride.get_exact() == (0,0):
            self.calculate_if_got_invited()
            
    def __calculate_if_got_invited(self):#still (and )
        assert not type(self._queque) == None, "queque is None" 

        if not self._queque.is_empty():
            print("__calculate_if_got_invited")    
            if self._queque.peek() > self._floor:
                self._state = directions.GOING_UP
                    
            elif self._queque.peek() < self._floor:
                self._state = directions.GOING_DOWN       
                    
        else:
            self._state = directions.STILL
               
    def __calculate_addition_time(self, floor):
        travel_time = self.__calculate_travel_time(self.__last_in_line, floor)
        return (travel_time[0] + 2, travel_time[1])
       # return 2.0 + self.__calculate_travel_time(location)
        #currentTime + timePos ther + time to travel to the new location 
           
    def __calculate_travel_time(self, floor_1, floor_2 = None ):
        if floor_2 == None:
            floor_2 = self._floor
            
        if floor_1 > floor_2:
            return (int(int(floor_1 - floor_2) / 2) , int(floor_1 - floor_2) % 2)
        else:
            return (  int(int(floor_2 - floor_1) / 2 ), int(floor_2 - floor_1) % 2)
        
#Comparison Operators:
    """        
    def __gt__(self, other):
        return self.to_get_the_elevator() > other.to_get_the_elevator()
    
    def __eq__(self, other):
        return self.to_get_the_elevator() == other.to_get_the_elevator()

    def __ge__(self, other):
        return self > other or self == other
           
    def __lt__(self, other):
        return other.to_get_the_elevator() > self.to_get_the_elevator()
   
    def __le__(self, other):
        return self < other or self == other
    
    def __ne__(self, other):
        return other.to_get_the_elevator() != self.to_get_the_elevator()
    """

    
    def __str__ (self):
            return f'|elevator: {self.serial},  ' + UPM.__str__(self) + " timer: " + repr(self._timer) + ' |'
    
    def __repr__ (self):
        return f'elevator: {self.serial}   ' + UPM.__repr__(self) + " timer: " + repr(self._timer) +' |'
        
#test()    

def get_init_position(serial, first_elevator_is = 1):      
            return (gm.FLOOR_SIZE[0] + gm.SPACE + (serial - first_elevator_is) * (gm.ELEVATOR_SIZE[0] + gm.SPACE), 0)


def test():
    e = Elevator()
    
    tes = [random.randint(1,10) for _ in range(10)]
    
    for i in range(len(tes)):
        print(e.to_get_the_elevator(i))
        

#test()