import pygame

#responsebol on window and display managment

TIME_TRAVEL_BETWEEN_FLOORS = 0.5 #seconds
WAIT_IN_FLOOR = 2.0
ELEVATOR_SIZE = (60,60)
FLOOR_SIZE = (160,60)
#SPACE = 5
SPACE = 0
ELEVATOR_PIC_FILE = 'resources\elv.png'
FLOOR_PIC_FILE = 'resources\wall.jpg'
FRAN_RATE = 60
PACE = 1


screenz = pygame.display.set_mode((1280, 720))
WINDOW_SIZE = pygame.display.get_window_size()
def get_floors_boundries(floor):
    return {"ceiling" : floor +1 * FLOOR_SIZE[1], "floor" : floor * FLOOR_SIZE[1]}

def get_screen():
    #return pygame.display.set_mode((1280, 720))
        
        return screenz
        

"""
לשים כאן פונקציה גלובלית שקוראת לקובץ התמונה של מעלית ועוד אחת לקובץ התמונה של קומה

תהיה מחלקה קומה

תהיה מחלקה טיימר

המחלקה קומה תהיה אחראית גם על הטיימר

כל מחלקה תהיה אחראית לייצר את התמונה כולל המיקום ולהחזיר אותו לפונקציה המרכזית באמצעות טכניקת משפך שיעשה אפדייט למסך עצמו ובו נעשה את השימוש בבליט

"""

pygame.font.init()

fonta = pygame.font.Font(pygame.font.get_default_font(),23)

text = fonta.render("time",True,(0,0,0))
