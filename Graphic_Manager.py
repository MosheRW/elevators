﻿from re import L
import pygame
pygame.init()
pygame.display.init()
pygame.font.init()


#screen and screen sizes
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(SCREEN_SIZE)
WINDOW_SIZE = pygame.display.get_window_size()


#font to use in the project
font = pygame.font.Font('resources\Roboto-Black.ttf',23)

#time settings
TIME_TRAVEL_BETWEEN_FLOORS = 0.5 #seconds
WAIT_IN_FLOOR = 2

#sizes of the game images
ELEVATOR_SIZE = (60,60)
FLOOR_SIZE = (160,60)

#number of pixeles between elevators
SPACE = 5
#number of pixeles buttons on the floor
IDENTATION = 20

#media files path
ELEVATOR_PIC_FILE = 'resources\elv.png'
ELEVATOR_GREEN_PIC_FILE = 'resources\elv_doors_open.png'
ELEVATOR_UP_FILE = 'resources\elevator_going_up.png'
ELEVATOR_DOWN_FILE = 'resources\elevator_going_down.png'

#FLOOR_PIC_FILE = 'resources\wall.jpg'
FLOOR_PIC_FILE = 'resources\ew_wall.png'
DING_FILE = "resources\ding.mp3"

ELEVATOR_PIC =  pygame.image.load(ELEVATOR_PIC_FILE).convert_alpha()
ELEVATOR_PIC.set_colorkey("white")

ELEVATOR_GREEN_PIC = pygame.image.load(ELEVATOR_GREEN_PIC_FILE).convert_alpha()
ELEVATOR_PIC.set_colorkey("white")

ELEVATOR_UP_PIC = pygame.image.load(ELEVATOR_UP_FILE).convert_alpha()
ELEVATOR_UP_PIC.set_colorkey("white")

ELEVATOR_DOWN_PIC = pygame.image.load(ELEVATOR_DOWN_FILE).convert_alpha()
ELEVATOR_DOWN_PIC.set_colorkey("white")

FLOOR_PIC = pygame.image.load(FLOOR_PIC_FILE).convert()

#inside the game constsnt globals
FRAN_RATE = 60
PACE = 2
FRAMES_TO_CROSS_A_FLOOR = int(TIME_TRAVEL_BETWEEN_FLOORS * FRAN_RATE)
DURATION_OF_ITERATION = int(1000000000/FRAN_RATE)


#given floors buffer
HORIZONTAL_BUFFER_SIZE = (FLOOR_SIZE[0],7)
HORIZONTAL_BUFFER_COLOR = "black"


print(DURATION_OF_ITERATION)