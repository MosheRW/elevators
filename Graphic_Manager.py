import pygame
pygame.init()
pygame.display.init()
pygame.font.init()


font = pygame.font.Font('Roboto-Black.ttf',23)

TIME_TRAVEL_BETWEEN_FLOORS = 0.5 #seconds
WAIT_IN_FLOOR = 2


ELEVATOR_SIZE = (60,60)
FLOOR_SIZE = (160,60)

SPACE = 0

ELEVATOR_PIC_FILE = 'resources\elv.png'
ELEVATOR_GREEN_PIC_FILE = 'resources\green-elv.png'
FLOOR_PIC_FILE = 'resources\wall.jpg'
DING_FILE = "resources\ding.mp3"

FRAN_RATE = 60
PACE = 2
FRAMES_TO_CROSS_A_FLOOR = int(TIME_TRAVEL_BETWEEN_FLOORS * FRAN_RATE)

HORIZONTAL_BUFFER_SIZE = (FLOOR_SIZE[0],7)
HORIZONTAL_BUFFER_COLOR = "black"


SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(SCREEN_SIZE)
WINDOW_SIZE = pygame.display.get_window_size()
