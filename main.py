# Example file showing a basic pygame "game loop"
import os
import pygame
import Graphic_Manager as gm

import Button
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill("white")
screen.set_colorkey()




filename_1 = 'resources\elv.png'
img_1 = pygame.image.load(filename_1).convert()
filename_2 = 'resources\wall.jpg'
img_2 = pygame.image.load(filename_2).convert()


fonta = pygame.font.Font('Roboto-Black.ttf',23)

text = fonta.render("time",True,(0,0,0))

textRect = text.get_rect()

textRect.center = ((1280 // 2, 720 //2))


#ygame.transform.scale(img, (200,200) )
# pygame setup

screen.blit(img_1, (100,200))

clock = pygame.time.Clock()
running = True
pygame.mixer.init()
pygame.mixer.music.load('ding.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
shape = pygame.Rect(160,160, 20,20)
#shape = screen.subsurface(shape)
#shape.unlock()

#bu = Button.Button(0,(160,160), 'mee')
#bu.init("hello")
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        
        

        if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                
                print(key_name)
        key = pygame.key.get_pressed()


        if key[pygame.K_ESCAPE]:
            running = False 
     
        if event.type == pygame.KSCAN_ESCAPE:   #pygame.QUIT:
            running = False
            
        if key[pygame.K_RETURN]:
            screen.fill("white")
            
       # if key[pygame.MOUSEBUTTONUP]:
        #    floor = 
            #img_1 = pygame.transform.scale(img_1, gm.ELEVATOR_SIZE)
            #img_2 = pygame.transform.scale(img_2, gm.FLOOR_SIZE)
            
            
            #screen.blit(img_1, (100,300))
            #screen.blit(img_2, (0,0))
            #screen.blit(bu.get_text(), bu.getrect())
            
            print("")
            #pygame.draw.rect(screen,(0,0,0), shape)
            #screen.blit(text,textRect)
           # pygame.mixer.music.play(-1)
            
            

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.mixer.music.play()

pygame.quit()