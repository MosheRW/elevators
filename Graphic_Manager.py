#responsebol on window and display managment

TIME_TRAVEL_BETWEEN_FLOORS = 0.5 #seconds
ELEVATOR_SIZE = (50,50)
FLOOR_SIZE = (135,50)

def get_floors_boundries(floor, num_of_floors):
    return {"ceiling" : floor +1 * FLOOR_SIZE[1], "floor" : floor * FLOOR_SIZE[1]}

