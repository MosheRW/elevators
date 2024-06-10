import pygame

from  Elevator_2 import Elevator
import Elevator_2 as ele

class Elevators_Management_2:

    def __init__(self, elevators = 12):
        self.__num_of_elevators = elevators
  
        self._the_elevators = [Elevator(i,0) for i in range(self.__num_of_elevators)]
        

#--------------------------------------------------------------------
    #initilize the elevators in the array        
    def init(self):
        for i in range(len( self._the_elevators)):
            self._the_elevators[i].set(ele.get_init_position(i))
            
    #updates the elevators      
    def update(self, iterations = 1):
        for i in  range(len(self._the_elevators)):
            self._the_elevators[i].update(iterations)     
       
    #get an array of elevators the graphical represntations tuples
    def get(self):
        return [self._the_elevators[i].get() for i in range(len(self._the_elevators))]

#--------------------------------------------------------------------
    #calling an elevator to given floor, and returninhg the time it will take it to arrive ther
    def get_an_elevator(self, floor):
        #seeks the best elevator to that floor. (elevat is an index)
        elevat = self.__shortest_time_elevator(floor)
        # call to that elevator,
        # and returns the updated time to the end of its schedule (exluding the final waiting time)
        return self._the_elevators[elevat].call(floor)

#--------------------------------------------------------------------   
    #calculation methodes
       
    def __shortest_time_elevator(self, floor = 4) -> int:
        minimum = 0        
        for i in range(1,len(self._the_elevators)):
            if self.__is_left_smaller(i,minimum, floor):
                minimum = i       
        return minimum
            
    def __is_left_smaller(self, elevator_1, elevator_2, floor) -> bool:
         left_ele_time = self._the_elevators[elevator_1].is_call_worthy(floor)
         right_ele_time = self._the_elevators[elevator_2].is_call_worthy(floor)
    
         if left_ele_time[0] < right_ele_time[0] \
            or (left_ele_time[0] == right_ele_time[0]  and  left_ele_time[1] < right_ele_time[1]):
                return True                 
         return False

#--------------------------------------------------------------------
    #textual representation functions    
    
    def __repr__(self) -> str:
        return f'the elevators: {self._the_elevators}'

    def __str__(self) -> str:
        return f'the elevators: {self._the_elevators}'

