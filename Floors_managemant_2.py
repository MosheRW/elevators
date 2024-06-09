from floor_2 import Floor_2 as Floor


class Floors_managment:
    def __init__ (self, num_of_floors = 11):
        self.__num_of_floors = num_of_floors
        
        self._the_floors = [Floor(i) for i in range(self.__num_of_floors + 1)]

#-------------------------------------------------------------------------        
    #initilize the floors in the array        
    def init(self):
         for i in range(len(self._the_floors)):
            self._the_floors[i].init(i)
    
    #get an array of the floors graphical represntations tuples            
    def get(self):
        return [self._the_floors[i].get() for i in range(len(self._the_floors))]

    #updates the floors 
    def update(self):
        for i in range(len(self._the_floors)):
            self._the_floors[i].update()
        
#----------------------------------------------------------------------------
    #returns if a given flooe is already invite an elevator to
    def is_this_floor_needs_an_elevator(self, floor) -> bool:
        return self._the_floors[floor].is_this_floor_needs_an_elevator()
    
    #sets a given floor as waiting to an elevator, and delgating the time it will take
    def get_an_elevator(self, floor, new_time):
        self._the_floors[floor].get_elevator(new_time)
       
#----------------------------------------------------------------------------
        
    #returns which floor who clicked by the user, or '-1' if none clicked
    def who_clicked(self, location_of_the_click):
        for i in range(len(self._the_floors)):
            if self._the_floors[i].is_clicked(location_of_the_click):
                return i
        return -1       

#----------------------------------------------------------------------------
    #textual representation functions
    def __repr__(self):
        return f'the floors: {self._the_floors}'
    
    def __str__(self):
        return f'the floors: {self._the_floors}'