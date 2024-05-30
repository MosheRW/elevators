from floor import Floor
import Graphic_Manager as gm


class Floors_managment:
    def __init__ (self, num_of_floors):
        self.__num_of_floors = num_of_floors
        self.__the_floors = [Floor(i) for i in range(self.__num_of_floors +1)]
        

    def get(self):
        return [self.__the_floors[i].get() for i in range(len(self.__the_floors))]

    def update(self):
        for floor in self.__the_floors:
            floor.update()
        
    def is_this_floor_needs_an_elevator(self, floor):
        return self.__the_floors[floor].is_this_floor_needs_an_elevator()
        
    def get_an_elevator(self, floor, exact_time):
        self.__the_floors[floor].get_elevator(exact_time)
        
    def who_clicked(self, location_of_the_click):
        pass
        #return index of the floor
    


    def __repr__(self):
        return f'the floors: {self.__the_floors}'
    
    def __str__(self):
        return f'the floors: {self.__the_floors}'