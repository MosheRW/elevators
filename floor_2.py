#from Queque import Queque
from enum import Enum
from Graphic_Manager import WAIT_IN_FLOOR, get_floors_boundries
import Graphic_Manager as gm
from Timer_2 import Timer_2
import pygame
from Button import Button


states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

def get_init_position(serial, first_floor_is = 0):
     return (0, gm.FLOOR_SIZE[1] + (serial - first_floor_is) * (gm.ELEVATOR_SIZE[0]))

         
def convert(position):
    return (position[0], gm.WINDOW_SIZE[1] - position[1] )

class Floor_2:
    
    def __init__(self, floor = 0):
        
        self._floor = floor
        self._position = (0,0)
        
        self._status = states.STILL
        self._timer = Timer_2()
        
        self.img =  pygame.image.load(gm.FLOOR_PIC_FILE).convert()
        
        self._button = Button(self._floor)
        self._timer_text = Button(self._floor)
        
        
        #the text hendlers could be unnecessary or need to be changed
        self.text = gm.font.render(self.textGenerator(),True,(0,0,0))
        self.text_rect = self.text.get_rect()

    def init(self, floor):
        self._floor = floor
        self.set_status(states.STILL)
        self.set_position(get_init_position(floor))
        
#---------------------------------------------------------------------------------

        
    def is_this_floor_needs_an_elevator(self):
        return self.get_status() == states.STILL
    

    def get_elevator(self, time):        
        print(f"-> 1 -> Floor_2.get_elevator.time: {time}   <-")
        self.set_timer(time)
        print(f"-> 2 -> Floor_2.get_elevator.time: {time}   <-")
        self.set_status(states.WAITING)
#----------------------------------------------------------------------------------
        
    def get(self):    
        return (self.get_img(), self.get_position(), self.get_text())
    
    def update(self):
        #self.update_text()
        self.update_timer()
        self.update_status()
        self.update_text()
        
  
#----------------------------------------------------------

    def get_floor(self):
        return self._floor
    
    def get_position(self):
        return self._position
    
    def get_status(self):
        assert type(self._status) == states, "ERROR, Wrong type"
        #print( self._status)
        return self._status
        #temp = self._status
        #return temp
    
    def get_timer(self):
        return self._timer.get()
    
    def get_img(self):
         return pygame.transform.scale(self.img, gm.FLOOR_SIZE)
    
    def get_text(self):
        
        return self.text, self.get_position()
        #return self.text,self.text_rect
    
#-----------------------------------------------------------

    def set_position(self,new_position):
        assert type(new_position) == tuple, "ERROR, incorrect value of new_position"
        self._position = new_position
        
    def set_status(self, new_status):
        assert type(new_status) == states, "ERROR, incorrect value of new_position"
        self._status = new_status
        self.update_img()
        
    def set_timer(self, new_time):
        self._timer.set(new_time)

    def set_img(self,filename):         #maybe need to implement another one, with state as input
         self.img =  pygame.image.load(gm.FLOOR_PIC_FILE).convert()
         
    def set_text(self):
        self.text = gm.font.render(self.textGenerator(),True,(0,0,0))
       
        self.text_rect = self.text.get_rect()
        
        #self.text_rect.topleft(self.get_position())
        
        
        
    

#-------------------------------------------------------------

    def update_status(self):
        #temp =  self._status        # self.get_status()
        if  self.get_status() == states.WAITING:
        #if  temp == states.WAITING:
            if not self._timer.is_running():
                self.set_status(states.ELEVATOR_HERE)
                self.set_timer(gm.WAIT_IN_FLOOR)
                self.play_ding()
               # dBug =input("ariived on time? ")
                
        elif self.get_status() == states.ELEVATOR_HERE: #case elevator is here
            if not self._timer.is_running():
                self.set_status(states.STILL)

    
    def update_timer(self):
        self._timer.update()
        #if self.get_status() == states.WAITING:
         #   print(self.get_timer())
    
    def update_img(self):                           #maybe need to implement another one, with state as inputs
        pass


    def update_text(self):
        self.set_text()
        
    def play_ding(self):
        pygame.mixer.music.load("resources\ding.mp3")
        pygame.mixer.music.play()

    def textGenerator(self) -> str:
        #return str(self.get_timer()) + str(self.get_status())
    
        if self.get_status() == states.STILL:
            return f"{self.get_timer()} click here!"
        elif self.get_status() == states.ELEVATOR_HERE:
            return f"{self.get_timer()} arruved!"
        elif self.get_status() == states.WAITING:
            return f"{self.get_timer()} states.WAITING"



    def is_clicked(self, m_position):
        m_position = convert(m_position)
        print(f"\n\n{self.get_floor()}")
        print(f"m_position: {m_position}")
        
        
        top_x, top_y = self.get_position()
        bottom_x, bottom_y = gm.FLOOR_SIZE[0], self.get_position()[1] - gm.FLOOR_SIZE[1]
        
        print(f"top: ({top_x}, {top_y}), bottom: ({bottom_x}, {bottom_y})")

        if m_position[0] <= top_x   and m_position[0] >= bottom_x:
           if m_position[1] <= top_y   and m_position[1] >= bottom_y:
            return True
        return False
            
        """            
        print(f"{m_position[0] >= self.get_position()[0]}, {m_position[0] <= (self.get_position()[0] + gm.FLOOR_SIZE[0])}, {m_position[1] >= self.get_position()[1]}, {m_position[1] <= (self.get_position()[0] + gm.FLOOR_SIZE[1])}")
        print(f"{self.get_position()[0]}, {(self.get_position()[0] + gm.FLOOR_SIZE[0])}, {self.get_position()[1]}, {(self.get_position()[0] + gm.FLOOR_SIZE[1])}")
        if m_position[0] >= self.get_position()[0] and m_position[0] <= (self.get_position()[0] + gm.FLOOR_SIZE[0])     and     m_position[1] >= self.get_position()[1] and m_position[1] >= (self.get_position()[0] + gm.FLOOR_SIZE[1]):
            return True
        
        return False
            """    
        
    
#-------------------------------------------------------------
    def __str__ (self):
        return f'|floor: {self.get_floor()},  status: {self.get_status()}, timer: {self.get_timer()} |\n'
    
    def __repr__ (self):
       return f'|floor: {self.get_floor()},  status: {self.get_status()}, timer: {self.get_timer()} |\n'


"""
fl = Floor_2(0)
print(fl.get_position())
print(fl.is_clicked((15,15)))
"""