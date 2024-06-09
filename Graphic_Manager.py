import pygame
pygame.init()
pygame.display.init()
pygame.font.init()


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
ELEVATOR_GREEN_PIC_FILE = 'resources\green-elv.png'
FLOOR_PIC_FILE = 'resources\wall.jpg'
DING_FILE = "resources\ding.mp3"

#inside the game constsnt globals
FRAN_RATE = 60
PACE = 2
FRAMES_TO_CROSS_A_FLOOR = int(TIME_TRAVEL_BETWEEN_FLOORS * FRAN_RATE)

#given floors buffer
HORIZONTAL_BUFFER_SIZE = (FLOOR_SIZE[0],7)
HORIZONTAL_BUFFER_COLOR = "black"

#screen and screen sizes
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(SCREEN_SIZE)
WINDOW_SIZE = pygame.display.get_window_size()
