import Elevator

class Elevators_Management:
    def __init__(self, floors = 8, elevators = 3):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        self.__is_the_floor_in_line = [False for _ in range(self.__num_of_floors + 1)]
        self.__the_elevators = [Elevator() for _ in range(self.__num_of_elevators)]
        
    def get_an_elevator(self, floor):# -> float:
        if not self.__is_the_floor_in_line:
            time, elevat = self.__shortest_time_elevator(floor)         # the most short queque
            assert self.__the_elevators[elevat].get_the_elevator(floor), "didn't order the elevator"    #get this elevtor
            
            return (True,time)
        return (False, 0.0)                                                 #maybe brock
           
    def __shortest_time_elevator(self, location):
        num = 0
        
        for i in range(1,self.__the_elevators):
            if self.__the_elevators[i].to_get_the_elevator(location) < self.__the_elevators[num].to_get_the_elevator(location):
                num = i
                
        return (i, self.__the_elevators[num].to_get_the_elevator(location))
        
    
    def update(self, time = 0.17):
        output = [self.__the_elevators[0].update(self.__num_of_floors, time)]
        
        for i in range(1, len(self.__the_elevators)):
            output.append(self.__the_elevators[i].update(self.__num_of_floors))
        
        return output