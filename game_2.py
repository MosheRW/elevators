import random
import pygame

import Graphic_Manager as gm
from Building_2 import Building 


class Game:
    screen = gm.screen
    
    def __init__(self, floors = 11, elevators =7):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        self._building = Building(self.__num_of_floors, self.__num_of_elevators)
                       
        
        
    def init(self):
        #maybe need to change the size of the screen here
        pygame.init()        
        self._building.init()


                  
    def erease_screen(self):
        self.screen.fill("white")
        self.screen.set_colorkey()
             
    def draw(self):
        self.erease_screen()
        self.draw_game_moduls()
        
    def draw_game_moduls(self):
        floors_pac, elevators_pac = self._building.get()
        self.draw_floors(floors_pac)
        self.draw_elevators(elevators_pac)
        
    def draw_floors(self, floors_pac):
        
        for i in range(len(floors_pac)):
            #draw the floor img
            self.screen.blit(floors_pac[i][0][0],   cuordinates_calculator(floors_pac[i][0][1]))
            
            #draw the timer including the backround
            self.screen.blit(floors_pac[i][1][1],   cuordinates_calculator(floors_pac[i][1][2]))
            self.screen.blit(floors_pac[i][1][0],   cuordinates_calculator(floors_pac[i][1][2]))
            
            #draw the call button including the backround
            self.screen.blit(floors_pac[i][2][1],   cuordinates_calculator(floors_pac[i][2][2]))
            self.screen.blit(floors_pac[i][2][0],   cuordinates_calculator(floors_pac[i][2][2]))
            
            #draw the buffer between floors
            self.screen.blit(floors_pac[i][3][0],   cuordinates_calculator(floors_pac[i][3][1]))
            


    def draw_elevators(self, elevators_pac):
        for i in range(len(elevators_pac)):
            
            assert (gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]) >= 0 \
               and  (gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]) <= gm.WINDOW_SIZE[1],\
              f'{(elevators_pac[i][1][0], gm.WINDOW_SIZE[1] - elevators_pac[i][1][1])}'
            
            ele = elevators_pac[i]
            
            #draw the elevator img
            self.screen.blit(ele[0], cuordinates_calculator(ele[1]))        


    # pull floor from numpad events.
    # if 'Enter' pressed returning random floor.
    # if no floor clikced returning '-1'
    def get_floor_from_keyboard(self, key):
         
         if key[pygame.K_KP0] or key[pygame.K_0]:
             return 0
         elif key[pygame.K_KP1] or key[pygame.K_1]:
             return 1
         elif key[pygame.K_KP2] or key[pygame.K_2]:
             return 2
         elif key[pygame.K_KP3] or key[pygame.K_3]:
             return 3
         elif key[pygame.K_KP4] or key[pygame.K_4]:
             return 4
         elif key[pygame.K_KP5] or key[pygame.K_5]:
             return 5
         elif key[pygame.K_KP6] or key[pygame.K_6]:
             return 6
         elif key[pygame.K_KP7] or key[pygame.K_7]:
             return 7
         elif key[pygame.K_KP8] or key[pygame.K_8]:
             return 8
         elif key[pygame.K_KP9] or key[pygame.K_9]:
             return 9
         elif key[pygame.K_RETURN]:
             return random.randint(0,self.__num_of_floors)
         
         return -1
    
    
    
    #pull floor from mouse events. if no floor clikced returning '-1'
    def get_floor_from_mouse(self):
        if pygame.mouse.get_pressed()[0]:
              pos = pygame.mouse.get_pos()
              return  self._building.who_clicked(    cuordinates_calculator(pos))
        return -1



    
    def play(self):
        clock = pygame.time.Clock()
        
        running = True
        while running:
              
              floor = -1
              if pygame.mouse.get_pressed()[0]:
                    floor = self.get_floor_from_mouse()
              for event in pygame.event.get():
                                   
                  #pull floor from mouse events
                  #floor = -1
                 # if pygame.mouse.get_pressed()[0]:
                  #  floor = self.get_floor_from_mouse()
                  
                  #pull floor from keyboard events
                  if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        
                        #if esc pressed - quiting
                        if key[pygame.K_ESCAPE]:
                            running = False          
                            
                        #pull floor from numpad events    
                        floor =  self.get_floor_from_keyboard(key)
                       
                  if floor != -1:
                        self._building.get_elevator(floor)
                             
                          
                            
              self._building.update()                                               
              self.draw()
              
              pygame.display.flip()
              
              clock.tick(gm.FRAN_RATE)

    

#calculating the end cuordinats (i stored the locations in Cartesian pivot table)
def cuordinates_calculator(cuordinates):
    return (cuordinates[0],gm.WINDOW_SIZE[1] - cuordinates[1])
    



g = Game()
g.init()
g.play()