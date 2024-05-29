from Elevator import Elevator
import Graphic_Manager as gm

class Elevators_Management:
    def __init__(self, floors = 8, elevators = 3):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
     #   self.__is_the_floor_in_line = [False for _ in range(self.__num_of_floors + 1)]                      #needs to move to another class
     #   self.__the_elevators = [Elevator(0,gm.ELEVATOR_SIZE[0]*i) for i in range(self.__num_of_elevators)]
        self.__the_elevators = [Elevator(0,0,i) for i in range(self.__num_of_elevators)]
        
    def get_an_elevator(self, floor):
     
        elevat = self.__shortest_time_elevator(floor)         # the most short queque
        
        return self.__the_elevators[elevat].get_the_elevator(floor)
         
      
    def update(self, time = 0.17):
        for elevate in  self.__the_elevators:
                 elevate.update(self.__num_of_floors, time)
       
                 
    def get(self):
        return [i.get() for i in self.__the_elevators]
                
    def __shortest_time_elevator(self, floor):
        minimum = 0
        
        
        for i in range(1,len(self.__the_elevators)):
            if self.is_left_smaller(i,minimum, floor):
                minimum = i
        """        
        for i in range(1,self.__the_elevators):
            if self.__the_elevators[i].to_get_the_elevator(floor) < self.__the_elevators[num].to_get_the_elevator(floor):
                num = i
           """
        
       # return (i, self.__the_elevators[minimum].to_get_the_elevator(floor))
        return i
        
    def is_left_smaller(self, elevator_1, elevator_2, floor) -> bool:
            return self.__the_elevators[elevator_1].to_get_the_elevator(floor) < self.__the_elevators[elevator_2].to_get_the_elevator(floor)
    

    def __repr__(self) -> str:
        return f'the elevators: {self.__the_elevators}'

    def __str__(self) -> str:
        return f'the elevators: {self.__the_elevators}'
             