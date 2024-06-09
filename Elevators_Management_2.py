import random
from Elevator_2 import Elevator
import Elevator_2 as ele
import Graphic_Manager as gm
import pygame

from Timer_2 import Timer_2 
import Timer_2 as timer


class Elevators_Management_2:

    
    def __init__(self, elevators = 12):
        self.__num_of_elevators = elevators
  
        self._the_elevators = [Elevator(i,0) for i in range(self.__num_of_elevators)]
        

    def init(self):
        for i in range(len( self._the_elevators)):
            self._the_elevators[i].set(ele.get_init_position(i))
            
            
    def update(self):
        for i in  range(len(self._the_elevators)):
            self._the_elevators[i].update()     
       
                    
    def get(self):
        return [self._the_elevators[i].get() for i in range(len(self._the_elevators))]

        
    def get_an_elevator(self, floor):     
        elevat = self.__shortest_time_elevator(floor)         # the shortest queque
        #print(f"elevator num: {elevat}")
        tup = self._the_elevators[elevat].call(floor)
        #print(f"Elevator_managemant.get_an_elevator.tup: {tup}")
        #return timer.calculate(tup[0], tup[1] - 30)
        #return self._the_elevators[elevat].call(floor)
        return tup
         
   
    def __shortest_time_elevator(self, floor = 4) -> int:
        minimum = 0
        
        for i in range(1,len(self._the_elevators)):
            if self.is_left_smaller(i,minimum, floor):
                minimum = i
       
        #print(f"Elevator_managemant.__shortest_time_elevator: is_call_worthy= {self._the_elevators[minimum].is_call_worthy(floor)}")
        return minimum
        
    def is_left_smaller(self, elevator_1, elevator_2, floor) -> bool:
         temp_1 = self._the_elevators[elevator_1].is_call_worthy(floor)
         temp_2 = self._the_elevators[elevator_2].is_call_worthy(floor)
         
         if temp_1[0] <temp_2[0]:
                return True
         elif temp_1[0] == temp_2[0] and  temp_1[1] <temp_2[1]:
                return True 
            
         return False

    def __repr__(self) -> str:
        return f'the elevators: {self._the_elevators}'

    def __str__(self) -> str:
        return f'the elevators: {self._the_elevators}'






#----------------------------------------------             
    def pack(self, screen):
        for i in range(len(self._the_elevators)):
            #screen.blit(elevators_pac[i][0],(elevators_pac[i][1][0],gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]))
            self._the_elevators[i].get_position()[0]
            screen.blit(self._the_elevators[i].get_img(),(self._the_elevators[i].get_position()[0],gm.WINDOW_SIZE[1] - self._the_elevators[i].get_position()[1]))

def pack(elevators_pac, screen):
    pass
    #for i in range(len(elevators_pac)):
        #screen.blit(elevators_pac[i][0],(elevators_pac[i][1][0],gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]))
      #  screen.blit(self._the_elevators[i].get_img(),(elevators_pac[i][1][0],gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]))


def test():
    pygame.init
    screen = gm.get_screen()
    e = Elevators_Management_2(12)
    e.init()
    
    #tes = [random.randint(1,12) for _ in range(20)]
    ##print(tes)
    #doc= [False for _ in range(13)]
    #tes_i = 0
    count = 0
    running = True
    clock = pygame.time.Clock()
    
    screen.fill("white")
    screen.set_colorkey()
    #time = Timer_2()
    #time.set(10)
    
    ##print(e)
    while running:
            
            for event in pygame.event.get():
                  
                if event.type == pygame.KEYDOWN:
                    
                    key = pygame.key.get_pressed()
                    
                    
                 
                    if key[pygame.K_ESCAPE]:
                        running = False 
                    
                    if key[pygame.K_RETURN]:
                          
                         #if tes_i < len(tes):
                        
                        floor =  random.randint(1,10)
                             
                        ##print(f"floor: {floor}")
                        time = e.get_an_elevator(floor)                                                       
                        ##print(f"time to: {time}")
                       
                        #e.get_an_elevator(tes_i)
                                
                    #tes_i += 1
                       
                        

            
            screen.fill("white")
            screen.set_colorkey()
            
           
           #time.update()
            e.update()
            e.pack(screen)
           # #print(f"time: {time.get()}, is running? {time.is_running()}")
          
            
            pygame.display.flip()          
            
            count += 1
            
            if count == 20:
                 
                 count = 0
          
            clock.tick(60)
        
    """
    for i in range(len(tes)):
        #print(e.get_an_elevator(i))
       """ 
        

#test()
