import Elevators_Management

class Building:
    def __init__(self, floors = 8, elevators = 3):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        self.floor_mange = [(0.0, False) for _ in range(self.__num_of_floors +1)]
        self.elevator_mange = Elevators_Management()

    
    def update(self, time = 0.17):
            output_elevators = self.elevator_mange.update()
            output_floors = self.elevator_mange.update()
            
            
        

    def update_floors_array():
        pass
    
    def get_floors(self):
         return [self.get_floor(i) for i in range(self.__num_of_floors +1)]
    
    def get_floor(self, i):
        if self.floor_mange[i] == 0.0: 
         
         
         
         
        
            