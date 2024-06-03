import random
from Elevator_2 import Elevator
import Elevator_2 as ele
import Graphic_Manager as gm
import pygame


class Elevators_Management_2:

    
    def __init__(self, elevators = 12):
        self.__num_of_elevators = elevators
  
        self._the_elevators = [Elevator(i,0) for i in range(self.__num_of_elevators)]
        

           
    def update(self):
        for i in  range(len(self._the_elevators)):
            self._the_elevators[i].update()     
       
                 
    def get(self):
        temp = [self._the_elevators[0].get()]
        for i in range(1,len(self._the_elevators)):
            temp += self._the_elevators[i].get()
            print(self._the_elevators[i].get())
        print(temp)
        return temp
        #return [self._the_elevators[i].get() for i in range(len(self._the_elevators))]

                
    def get_an_elevator(self, floor):     
        elevat = self.__shortest_time_elevator(floor)         # the shortest queque
        tup = self._the_elevators[elevat].call(floor)
        return tup
         
   
    def __shortest_time_elevator(self, floor = 4) -> int:
        minimum = 0
        
        for i in range(1,len(self._the_elevators)):
            if self.is_left_smaller(i,minimum, floor):
                minimum = i
       
        return minimum
        
    def is_left_smaller(self, elevator_1, elevator_2, floor) -> bool:
            print(f"floor: {floor}")    
            print(f"is_left_smaller: {self._the_elevators[elevator_1].is_call_worthy(floor)}, {self._the_elevators[elevator_2].is_call_worthy(floor)}")
        
           # if self._the_elevators[elevator_1].to_get_the_elevator(floor)[0] < self._the_elevators[elevator_2].to_get_the_elevator(floor)[0]:
            if self._the_elevators[elevator_1].is_call_worthy(floor)[0] < self._the_elevators[elevator_2].is_call_worthy(floor)[0]:
                return True
           # elif self._the_elevators[elevator_1].to_get_the_elevator(floor)[0] == self._the_elevators[elevator_2].to_get_the_elevator(floor)[0] and  self._the_elevators[elevator_1].to_get_the_elevator(floor)[1] < self._the_elevators[elevator_2].to_get_the_elevator(floor)[1]:
            elif self._the_elevators[elevator_1].is_call_worthy(floor)[0] == self._the_elevators[elevator_2].is_call_worthy(floor)[0] and  self._the_elevators[elevator_1].is_call_worthy(floor)[1] < self._the_elevators[elevator_2].is_call_worthy(floor)[1]:
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
            screen.blit(self._the_elevators[i].get_img(),(self._the_elevators[i].get_position()[0],gm.WINDOW_SIZE[1] - self._the_elevators[i].get_position()[1]))

def pack(elevators_pac, screen):
    pass
    #for i in range(len(elevators_pac)):
        #screen.blit(elevators_pac[i][0],(elevators_pac[i][1][0],gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]))
      #  screen.blit(self._the_elevators[i].get_img(),(elevators_pac[i][1][0],gm.WINDOW_SIZE[1] - elevators_pac[i][1][1]))


def test():
    pygame.init
    screen = gm.get_screen()
    e = Elevators_Management_2()
    
    tes = [random.randint(2,10) for _ in range(10)]
    tes_i = 0
    count = 0
    running = True
    clock = pygame.time.Clock()

    print(e)
    while running:
            
            for event in pygame.event.get():
                  
                if event.type == pygame.KEYDOWN:
                    tes_i += 1
                    key = pygame.key.get_pressed()
                    
                    
                 
                    if key[pygame.K_ESCAPE]:
                        running = False 
                    
                    if key[pygame.K_RETURN]:
                        if tes_i < len(tes):
                            e.get_an_elevator(tes[tes_i])                                                       
                            #e.get_an_elevator(tes_i)                                                       
                       
                        


            screen.fill("white")
            screen.set_colorkey()
            
            e.update()
            e.pack(screen)
            
            pygame.display.flip()          
            
            count += 1
            
            if count == 20:
                 print(e)
                 count = 0
            
            clock.tick(30)
        
    """
    for i in range(len(tes)):
        print(e.get_an_elevator(i))
       """ 
        

test()
