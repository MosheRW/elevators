         
from Graphic_Manager import get_floors_boundries
from Floors_managemant_2 import Floors_managment
from Elevators_Management_2 import Elevators_Management_2 as Elevators_Management


class Building:
    def __init__(self, floors = 8, elevators = 3):
        print("start building")
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        self._floors_mange = Floors_managment(self.__num_of_floors)        #[(0.0, False) for _ in range(self.__num_of_floors +1)]
        self._elevator_mange = Elevators_Management(self.__num_of_elevators)
        
#----------------------------------------------------------------------------

    def init(self):
        self._floors_mange.init()
        self._elevator_mange.init()
        
#----------------------------------------------------------------------------
    def get_elevator(self, floor):
        if self._floors_mange.is_this_floor_needs_an_elevator(floor):
            print("building.get_elevator")
            
            time_stamp = self._elevator_mange.get_an_elevator(floor)
            
            print(f"building.get_elevator,time: {time_stamp}")
            assert type(time_stamp) == tuple, "Error, incorrect value"
            
            self._floors_mange.get_an_elevator(floor,time_stamp)
        else:
             print("building.get_elevator.not need elevator")

    def update(self):
        self._floors_mange.update()
        self._elevator_mange.update()
        
    def get(self):
        return [self._floors_mange.get(), self._elevator_mange.get()]
    
    def __str__(self):
         return f'floor_manger: {self._floors_mange}\nelevator_mange: {self._elevator_mange}'
    
    def __repr__(self):
         return f'floor_manger: {self._floors_mange}\nelevator_mange: {self._elevator_mange}'
         
         
         
        
            