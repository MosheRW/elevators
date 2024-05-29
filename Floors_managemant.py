from floor import Floor
import Graphic_Manager as gm


class floors_managment:
    def __init__ (self, num_of_floors):
        self.__num_of_floors = num_of_floors
        self.__the_floors = [Floor(i) for i in range(self.__num_of_floors +1)]
        

    def get(self):
        return [floor.get() for floor in self.__the_floors]

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
    


