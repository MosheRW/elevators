# Example file showing a basic pygame "game loop"
from json.encoder import ESCAPE
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        

        if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                
                print(key_name)
        
       # print(key)
       # print(pygame.key.get_pressed())
        key = pygame.key.get_pressed()
        #if key[pygame.K_ESCAPE] or key[pygame.KSCAN_ESCAPE]:
        if key[pygame.KSCAN_ESCAPE]:
        #if key[pygame.K_ESCAPE]:
            running = False 
        #     
             
        #print(pygame.KSCAN_ESCAPE)
        if event.type == pygame.KSCAN_ESCAPE:   #pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()