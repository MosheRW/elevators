from floor_2 import Floor_2 as Floor
import floor_2 as fl
import Graphic_Manager as gm


class Floors_managment:
    def __init__ (self, num_of_floors = 11):
        self.__num_of_floors = num_of_floors
        
        self._the_floors = [Floor(i) for i in range(self.__num_of_floors + 1)]

#-------------------------------------------------------------------------        
    def init(self):
         for i in range(len(self._the_floors)):
            self._the_elevators[i].set_position((fl.get_init_position(i)))
       
        
    def get(self):
        return [self._the_floors[i].get() for i in range(len(self._the_floors))]


    def update(self):
        for i in range(len(self._the_floors)):
            self._the_floors[i].update()
        
#----------------------------------------------------------------------------

    def is_this_floor_needs_an_elevator(self, floor):
        return self.__the_floors[floor].is_this_floor_needs_an_elevator()
        
    def get_an_elevator(self, floor, new_time):
        self._the_floors[floor].get_elevator(new_time)
        

    def who_clicked(self, location_of_the_click):
        pass
        #return index of the floor
    

#----------------------------------------------------------------------------

    def __repr__(self):
        return f'the floors: {self.__the_floors}'
    
    def __str__(self):
        return f'the floors: {self.__the_floors}'