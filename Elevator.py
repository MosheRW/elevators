from Queque import Queque
from enum import Enum
from Graphic_Manager import get_floors_boundries

directions = Enum('directions', ['UP','DOWN', 'STAND'])

class Elevator:
    def __init__(self, location = 0):
        self.__elevator_location = location
        self.__queque = Queque()
        self.__last_in_line = location
        self.__seconds_remain = 0.0
        self.__position
        self.__direction = directions.STAND
        self.__last_floor_entry = 0.0

    def updtae(self, floors, time = 0.17) :
        self.__seconds_remain -= time
        
        self.update_pos(self)
        self.update_state(self, floors)
        
        return self.__position
        
    def update_pos(self):
   
        if self.__direction == directions.up:
            self.__position = (self.__position[0], self.__position[1] +1)
            
        elif self.__direction == directions.DOWN:
            self.__position = (self.__position[0], self.__position[1] -1)
                  
    def update_state(self, floors):
        
        if self.__direction == directions.STAND:
            if self.__seconds_remain - self.__last_floor_entry >= 2.0:
                self.__get_next_direction()
         
        else:
            if get_floors_boundries(self.__queque.peek(),floors) == self.__position[1]:
                self.__last_floor_entry = self.__seconds_remain
                self.__direction = directions.STAND
     
  
        
    def get_next_direction(self):
        if self.__direction == directions.STAND:            
            if self.__queque.peek() > self.__location:
                self.__direction = directions.UP
            elif self.__queque.peek() < self.__location:
                self.__direction = directions.DOWN



    def get(self):
        return self.__location

    def get_the_elevator(self, location) -> bool:
        self.__queque.push(location)
        self._last_in_line = location
        self.set_the_new_time(location)
    
    def set_the_new_time(self, location):
        #currentTime + timePos ther + time to travel to the new location
        self.__seconds_remain += self.__calculate_addition_time(location)
   
    def to_get_the_elevator(self, location) -> float:       
        return self.__seconds_remain + self.__calculate_addition_time(location)
    
    def __calculate_addition_time(self, location) -> float:
        return 2.0 + self.__calculate_travel_time(location)
        #currentTime + timePos ther + time to travel to the new location 
           
    def __calculate_travel_time(self, location_1, location_2 = None ) -> float:
        if location_2 == None:
            location_2 = self.__elevator_location
            
        if location_1 > location_2:
            return 0.5 * (location_1 - location_2)
        else:
            return 0.5 * (location_2 - location_1)
        
#Comparison Operators:
        
    def __gt__(self, other):
        return self.to_get_the_elevator > other.to_get_the_elevator
    
    def __eq__(self, other):
        return self.to_get_the_elevator == other.to_get_the_elevator

    def __ge__(self, other):
        return self > other or self == other
           
    def __lt__(self, other):
        return other.to_get_the_elevator > self.to_get_the_elevator
   
    def __le__(self, other):
        return self < other or self == other
    
    def __ne__(self, other):
        return other.to_get_the_elevator != self.to_get_the_elevator

   
