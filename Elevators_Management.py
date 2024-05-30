import random
from Elevator import Elevator
import Graphic_Manager as gm

class Elevators_Management:
    __num_of_floors = 8
    __num_of_elevators = 4
    
    def __init__(self, floors = 8, elevators = 5):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
  
        self._the_elevators = [Elevator(0,0,i) for i in range(self.__num_of_elevators)]
        
    def get_an_elevator(self, floor):
     
        elevat = self.__shortest_time_elevator(floor)         # the most short queque
        
        tup = self._the_elevators[elevat].get_the_elevator(floor)
        return tup
         
      
    def update(self, time = 0.17):
       # for elevate in  self._the_elevators:
        for i in  range(len(self._the_elevators)):
            self._the_elevators[i].update()     
                 #elevate.update(self.__num_of_floors, time)
       
                 
    def get(self):
        return [self._the_elevators[i].get() for i in range(len(self._the_elevators))]
        #return [i.get() for i in range(len(self._the_elevators))]
                
    def __shortest_time_elevator(self, floor) -> int:
        minimum = 0
        
        
        for i in range(1,len(self._the_elevators)):
            if self.is_left_smaller(i,minimum, floor):
                minimum = i
       
        return minimum
        
    def is_left_smaller(self, elevator_1, elevator_2, floor) -> bool:
            if self._the_elevators[elevator_1].to_get_the_elevator(floor)[0] < self._the_elevators[elevator_2].to_get_the_elevator(floor)[0]:
                return True
            elif self._the_elevators[elevator_1].to_get_the_elevator(floor)[0] == self._the_elevators[elevator_2].to_get_the_elevator(floor)[0] and  self._the_elevators[elevator_1].to_get_the_elevator(floor)[1] < self._the_elevators[elevator_2].to_get_the_elevator(floor)[1]:
                return True 
    

    def __repr__(self) -> str:
        return f'the elevators: {self._the_elevators}'

    def __str__(self) -> str:
        return f'the elevators: {self._the_elevators}'
             

def test():
    e = Elevators_Management()
    
    tes = [random.randint(1,10) for _ in range(10)]
    
    for i in range(len(tes)):
        print(e.get_an_elevator(i))
        

#test()