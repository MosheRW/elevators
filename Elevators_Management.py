


class Elevators_Management:
    def __init__(self, floors = 8, elevators = 3):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        self.__is_the_floor_in_line = [False for _ in range(self.__num_of_floors)]
        self.__the_elevators = [Elevator() for _ in range(self.__num_of_elevators)]
        
        