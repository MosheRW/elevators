from Building import Building 
import pygame
import Graphic_Manager as gm

class Game:
    screen = None
    
    def __init__(self, floors = 8, elevators =3):
        self.__num_of_floors = floors
        self.__num_of_elevators =elevators
        
        self.__building = Building(self.__num_of_floors, self.__num_of_elevators)
        
        
        self.__clock = pygame.time.Clock()


    def init(self, state = "test"):
        if state != "test":
            self.__num_of_floors    = input("insert the number of floors: ")
            self.__num_of_elevators    = input("insert the number of elevators: ")
                
        else: 
            self.__num_of_floors = 8
            self.__num_of_elevators = 3
                
        self.init_screen()
            
    def erease_screen(self):
        pass
        
    def init_screen(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1280, 720))
        print(pygame.display.get_desktop_sizes())
        self.screen.fill("white")
        self.screen.set_colorkey()
       

    #tests
    def tests(self):
        tes = [8,3,5,7,4,2,1]
        tes_i = 0
            
        clock = pygame.time.Clock()
        running = True
        count = 0
        while running:
            
             for event in pygame.event.get():
                 
                 key = pygame.key.get_pressed()
                 
                 
                 
                 if key[pygame.K_ESCAPE]:
                    running = False 
                    
                 if key[pygame.K_RETURN]:
                     if  tes_i <   len(tes):
                         
                         print(self.__building)
                         self.__building.get_elevator(tes[tes_i])
                         print(self.__building)
                         tes_i += 1
                     elif tes_i ==   len(tes):
                         running = False
            
             """                         
             count += 1
        
             if count == 60:
               # print("hii")
                #print(self.__building)
                count = 0
            
             #   pygame.display.flip()
             """
             self.__building.update()
             self.__clock.tick(60)
             



    def get_ele(self,i):
        self.__building.get_elevator(i)
        
    def print_building(self):
        print(self.__building)
        
    def update(self):
        self.__building.update()
        
game = Game()
game.init()
game.tests()

"""
tes = [8,3,5,7,4,2,1]
tes_i = 0

    
#for tes_i in tes:
for i in range(len(tes)):
    print(tes[i])
  #  game.update()
    game.get_ele(set[i])
    game.update()
    game.print_building()
    
"""    