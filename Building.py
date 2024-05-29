         
from Graphic_Manager import get_floors_boundries
from Floors_managemant import Floors_managment
from Elevators_Management import Elevators_Management 


class Building:
    def __init__(self, floors = 8, elevators = 3):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        self._floors_mange = Floors_managment(self.__num_of_floors)        #[(0.0, False) for _ in range(self.__num_of_floors +1)]
        self.__elevator_mange = Elevators_Management(self.__num_of_floors, self.__num_of_elevators)
 
#methodes to utilise the class
    def get_elevator(self, floor):
        if self._floors_mange.is_this_floor_needs_an_elevator(floor):
         
            exac_time = self.__elevator_mange.get_an_elevator(floor)
            self._floors_mange.get_an_elevator(floor,exac_time)

    def update(self, time = 0.017):
        self._floors_mange.update()
        self.__elevator_mange.update()
        
    def get(self):
        return (self._floors_mange.get(), self.__elevator_mange.get())
    

        """
        output_elevators = self.__elevator_mange.update(time)
        self.__update_floors_array(time)
            
        output_floors = self.__get_floors()
            
        return [output_elevators, output_floors]
        """
    """
        #methodes to update the floors status                               
    def __update_floors_array(self, time):
        for i in range( self.__num_of_floors + 1):
            self.__update_a_floor(i, time)
                  
    def __update_a_floor(self, i, time):
        
        if self._floor_mange[i][1]:
            
            if  self._floor_mange[i][0] < time:
                 
                if self._floor_mange[i][0] > 0:
                      self._floor_mange[i] = (0.0, True)
                 
                elif self._floor_mange[i][0] > (-2.0):
                    self._floor_mange[i] = (self._floor_mange[i][0] - time, True)
                    
                else:
                     self._floor_mange[i][0] = (0.0, False)  
                                     
                     
            else:
                self._floor_mange[i]= (self._floor_mange[i][0] - time, True)
 
    """
    def __str__(self):
         return f'floor_manger: {self._floor_mange}\nelevator_mange: {self.__elevator_mange}'
    
    def __repr__(self):
         return f'floor_manger: {self._floor_mange}\nelevator_mange: {self.__elevator_mange}'
         
         
         
        
            