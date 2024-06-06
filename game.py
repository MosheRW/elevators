import random
from Building import Building 
import pygame
import Graphic_Manager as gm


class Game:
    screen = gm.get_screen()
    
    def __init__(self, floors = 12, elevators = 10):
        self.__num_of_floors = floors
        self.__num_of_elevators = elevators
        
        self.__building = Building(self.__num_of_floors, self.__num_of_elevators)
        
        
        self.__clock = pygame.time.Clock()


    def init(self, state = "test"):
        pygame.init()
        if state != "test":
            self.__num_of_floors    = input("insert the number of floors: ")
            self.__num_of_elevators    = input("insert the number of elevators: ")
                
        else: 
            self.__num_of_floors = 8
            self.__num_of_elevators = 3
                
        self.init_screen()
            
    def erease_screen(self):
        self.screen.fill("white")
        self.screen.set_colorkey()
        
    def init_screen(self):
        
        #print(pygame.display.get_desktop_sizes())
        self.screen.fill("white")
        self.screen.set_colorkey()
     
    def display(self):
        self.erease_screen()
        self.pack_to_desplay()
        
    def pack_to_desplay(self):
        floors_pac, elevators_pac = self.__building.get()
        self.pack_floors_to_desplay(floors_pac)
        self.pack_elevators_to_desplay(elevators_pac)
        
    def pack_floors_to_desplay(self, floors_pac):
        for i in range(len(floors_pac)):
            self.screen.blit(floors_pac[i][0],(floors_pac[i][1][0],gm.WINDOW_SIZE[1] - floors_pac[i][1][1]))
            
    def pack_elevators_to_desplay(self, elevators_pac):
        for i in range(len(elevators_pac)):
           # assert (gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]) >= 0 and  (gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]) <= gm.WINDOW_SIZE[1], f'{(elevators_pac[i][1][0], gm.WINDOW_SIZE[1] - elevators_pac[i][1][1])}'
            
            self.screen.blit(elevators_pac[i][0],(elevators_pac[i][1][0], gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]))
        

    #tests
    def tests(self):
        tes = [6,3,5,7,4,2,1]
        #tes = [1,1,1,1,1,1,1]
        tes_i = 0
            
      
        running = True
        count = 0
        
        while running:
             count += 1
             for event in pygame.event.get():
                  
                  if event.type == pygame.KEYDOWN:
                     tes_i += 1
                     key = pygame.key.get_pressed()
                 
                
                
                 
                     if key[pygame.K_ESCAPE]:
                        running = False 
                    
                     if key[pygame.K_RETURN]:
                        # self.__building.get_elevator(random.randint(2,10))  
                         if tes_i < len(tes):                         
                            self.__building.get_elevator(tes[tes_i])                           
                         
                     """   
                 f, m = self.get_floor(key)
                 if m:
                    self.__building.get_elevator(f)
                    """
                 ##print(self.__building)
                     
                   
                         
                     #if count == 4:
                      #   running = False 
                                      
           
             if count % 20 == 0:
                 ##print(count,end="\r")
                 #print(self.__building, end="\r")
                 
             if count == 60: 
                count = 0
                
             self.__building.update()
             self.display()
             
             pygame.display.flip()
             
             self.__clock.tick(60)
        
        #print(self.__building)

    def get_floor(self, key):
         if key[pygame.K_KP0]:
             return 0,True
         elif key[pygame.K_KP1]:
             return 1,True
         elif key[pygame.K_KP2]:
             return 2,True
         elif key[pygame.K_KP3]:
             return 3,True
         elif key[pygame.K_KP4]:
             return 4,True
         elif key[pygame.K_KP5]:
             return 5,True
         elif key[pygame.K_KP6]:
             return 6,True
         elif key[pygame.K_KP7]:
             return 7,True
         elif key[pygame.K_KP8]:
             return 8,True
         elif key[pygame.K_KP9]:
             return 9,True
         
         return -1,False


    def get_ele(self,i):
        self.__building.get_elevator(i)
        
    def #print_building(self):
        #print(self.__building)
        
    def update(self):
        self.__building.update()


def close_terminal():
    
    #print("insert first digit: ",)
    first = int(input(""))# end="\r")
    
    while first != 4:
        #print("insert first digit: ") #\r)#, end="\r")
        first = int(input(""))
        

    
    #print("insert second digit: ") #, end="\r")
    second = int(input(""))
    
    while second != 0:
        #print("insert second digit: ") #, end="\r")
        second = int(input(""))
    
    #print("insert thired digit: ") #, end="\r")
    thired = int(input(""))
    
    while thired != 4:
        #print("insert thired digit: ") #, end="\r")
        thired = int(input(""))
        

    
    #print("insert fourth digit: ") #, end="\r")
    fourth = int(input(""))
    
    while fourth != 1:
        #print("insert fourth digit: ") #, end="\r")
        fourth = int(input(""))
        


#img = pygame.image.load(gm.ELEVATOR_PIC_FILE).convert()



game = Game()
#game.init()
game.tests()
close_terminal()

"""
tes = [8,3,5,7,4,2,1]
tes_i = 0

    
#for tes_i in tes:
for i in range(len(tes)):
    #print(tes[i])
  #  game.update()
    game.get_ele(set[i])
    game.update()
    game.#print_building()
    
"""    