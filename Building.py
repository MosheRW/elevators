import Elevators_Management as em
from Graphic_Manager import get_floors_boundries


class Building:
    def __init__(self, floors = 8, elevators = 3):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        
        # invited == True
        self.__floor_mange = [(0.0, False) for _ in range(self.__num_of_floors +1)]
        self.__elevator_mange = em.Elevators_Management(floors, elevators)

    

    def get_elevator(self, floor):
         data = self.__elevator_mange.get_an_elevator(floor)
         
         if data[0]:
               self.__floor_mange[floor] = (data[1], True)


    def update(self, time = 0.017):
            output_elevators = self.__elevator_mange.update(time)
            self.__update_floors_array(time)
            
            output_floors = self.__get_floors()
            
            return [output_elevators, output_floors]
                                
    def __update_floors_array(self, time):
        for i in range( self.__num_of_floors + 1):
            self.__update_a_floor(i, time)
                  
    def __update_a_floor(self, i, time):
        
        if self.__floor_mange[i][1]:
            
            if  self.__floor_mange[i][0] < time:
                 
                if self.__floor_mange[i][0] > 0:
                      self.__floor_mange[i] = (0.0, True)
                 
                elif self.__floor_mange[i][0] > (-2.0):
                    self.__floor_mange[i] = (self.__floor_mange[i][0] - time, True)
                    
                else:
                     self.__floor_mange[i][0] = (0.0, False)  
                                     
                     
            else:
                self.__floor_mange[i]= (self.__floor_mange[i][0] - time, True)
                 
                                                                                                      
    def __get_floors(self):
         return [self.__get_floor(i) for i in range(self.__num_of_floors +1)]
    
    def __get_floor(self, i):
       
        if self.__floor_mange[i][0] <= 0.0:
            if self.__floor_mange[i][1]:
                return  ((get_floors_boundries(i)[0], 0), "elevator here")
            else:
                return  ((get_floors_boundries(i)[0], 0), "netural") 
        else:
              return ((get_floors_boundries(i)[0], 0), "scdualded")
              
    
    def __str__(self):
         return f'floor_manger: {self.__floor_mange}\nelevator_mange: {self.__elevator_mange}'
    
    def __repr__(self):
         return f'floor_manger: {self.__floor_mange}\nelevator_mange: {self.__elevator_mange}'
         
         
         
        
            