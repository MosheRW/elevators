﻿import pygame

#responsebol on window and display managment

TIME_TRAVEL_BETWEEN_FLOORS = 0.5 #seconds
WAIT_IN_FLOOR = 2
ELEVATOR_SIZE = (60,60)
FLOOR_SIZE = (160,60)
#SPACE = 5
SPACE = 0
ELEVATOR_PIC_FILE = 'resources\elv.png'
ELEVATOR_GREEN_PIC_FILE = 'resources\green-elv.png'
FLOOR_PIC_FILE = 'resources\wall.jpg'
FRAN_RATE = 60
PACE = 2
FRAMES_TO_CROSS_A_FLOOR = int(TIME_TRAVEL_BETWEEN_FLOORS * FRAN_RATE)
HORIZONTAL_BUFFER_SIZE = (FLOOR_SIZE[0],7)
HORIZONTAL_BUFFER_COLOR = "black"


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


font = pygame.font.Font('Roboto-Black.ttf',23)

text = font.render("time",True,(0,0,0))

textRect = text.get_rect()


textRect.center = ((1280 // 2, 720 //2))
