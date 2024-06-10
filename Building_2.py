from Floors_managemant_2 import Floors_managment
from Elevators_Management_2 import Elevators_Management_2 as Elevators_Management


class Building:
    def __init__(self, floors = 8, elevators = 3):
        
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        self._floors_mange = Floors_managment(self.__num_of_floors)  
        self._elevator_mange = Elevators_Management(self.__num_of_elevators)
        
#----------------------------------------------------------------------------
    
    def init(self):
        """
        initilize the floors and elevators managemant
        """
        self._floors_mange.init()
        #self._elevator_mange.init()
        
    #updates the floors and elevators                
    def update(self, iterations = 1):
        self._floors_mange.update(iterations)
        self._elevator_mange.update(iterations)
        
    #get an array of the floors and elevators graphical represntations arrays of tuples
    def get(self):
        return [self._floors_mange.get(), self._elevator_mange.get()]
        
#----------------------------------------------------------------------------

    #returns which floor who clicked by the user, or '-1' if none clicked
    def who_clicked(self, location_of_the_click):
        return self._floors_mange.who_clicked(location_of_the_click)
   
    # calling to an elevator to a given floor - if the floor is eligible to invite an elevator
    # and delegates the timing to the given floor
    def get_elevator(self, floor):
        if self._floors_mange.is_this_floor_needs_an_elevator(floor):
            
            time_stamp = self._elevator_mange.get_an_elevator(floor)
            
            assert type(time_stamp) == tuple, "Error, incorrect value"        
            
            self._floors_mange.get_an_elevator(floor,time_stamp)
        

#----------------------------------------------------------------------------

    def __str__(self):
         return f'floor_manger: {self._floors_mange}\nelevator_mange: {self._elevator_mange}'
    
    def __repr__(self):
         return f'floor_manger: {self._floors_mange}\nelevator_mange: {self._elevator_mange}'
         
         
         
        
            