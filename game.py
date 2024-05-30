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
        self.screen.fill("white")
        self.screen.set_colorkey()
        
    def init_screen(self):
        pygame.init()
        
        #self.screen = pygame.display.set_mode((1280, 720))
        self.screen = pygame.display.set_mode((1280, 720))
        print(pygame.display.get_desktop_sizes())
        self.screen.fill("white")
        self.screen.set_colorkey()
       
    def pack_to_desplay(self):
        #blit
        pass

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
                    
                 if key[pygame.K_RETURN]: # and count % 15 == 0:
                     if  tes_i <   len(tes):
                         print (f"invite to the {tes[tes_i]}'th floor\n")
                         #print(self.__building)
                         #print("")
                         self.__building.get_elevator(tes[tes_i])
                         print("")
                         print(self.__building)
                         tes_i += 1
                     elif tes_i ==   len(tes):
                         tes_i = 0
                         count += 1
                         
                     if count == 4:
                         running = False 
                                      
             
                          
             """   
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


def close_terminal():
    
    print("insert first digit: ",)
    first = int(input(""))# end="\r")
    
    while first != 4:
        print("insert first digit: ") #\r)#, end="\r")
        first = int(input(""))
        

    
    print("insert second digit: ") #, end="\r")
    second = int(input(""))
    
    while second != 0:
        print("insert second digit: ") #, end="\r")
        second = int(input(""))
    
    print("insert thired digit: ") #, end="\r")
    thired = int(input(""))
    
    while thired != 4:
        print("insert thired digit: ") #, end="\r")
        thired = int(input(""))
        

    
    print("insert fourth digit: ") #, end="\r")
    fourth = int(input(""))
    
    while fourth != 1:
        print("insert fourth digit: ") #, end="\r")
        fourth = int(input(""))
        


#img = pygame.image.load(gm.ELEVATOR_PIC_FILE).convert()

game = Game()
game.init()
#game.tests()
close_terminal()

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