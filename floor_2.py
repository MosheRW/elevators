#from Queque import Queque
from enum import Enum
from Graphic_Manager import WAIT_IN_FLOOR, get_floors_boundries
import Graphic_Manager as gm
from Timer_2 import Timer_2
import pygame
from Button import Button
from Button import states


#states = Enum('states', ['WAITING', 'ELEVATOR_HERE', 'STILL'])

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
        
        self._button = Button(self.get_position(), str(self._floor), "yellow")
        self._timer_text = Button(self.get_position(),"00:00","black")
        self.__empty = Button(self.get_position(),"00:00","black",  False)
        
        self.__buffer = pygame.Surface((160, 7))
        self.__buffer.fill(gm.HORIZONTAL_BUFFER_COLOR)

        #the text hendlers could be unnecessary or need to be changed
        self.text = gm.font.render(self.textGenerator(),True,(0,0,0))
        self.text_rect = self.text.get_rect()


#---------------------------------------------------------------------------------
        
    def init(self, floor):
        self._floor = floor
        self.set_status(states.STILL)
        self.set_position(get_init_position(floor))
        self._button.set(self.calculate_button_pos(),str(self.get_floor()),(255,255,255))# ") #(149, 201, 232))
        self._timer_text.set(self.calculate_timer_pos(), "00:00", "gray")
        self.set_buffer()
        
        #self._timer_text.init(f"{self.get_timer()}")
        
        
#---------------------------------------------------------------------------------

        
    def is_this_floor_needs_an_elevator(self):
        return self.get_status() == states.STILL
    

    def get_elevator(self, time):        
        ###print(f"-> 1 -> Floor_2.get_elevator.time: {time}   <-")
        self.set_timer(time)
        ###print(f"-> 2 -> Floor_2.get_elevator.time: {time}   <-")
        self.set_status(states.WAITING)
#----------------------------------------------------------------------------------
        
    def get(self):    
        return (self.get_img(), self.get_text(), self.get_button(),self.get_buffer())
    
    def update(self):
        #print(f" Floor serial: {self._floor}. timer: {self._timer} \n") 
        #self.update_text()
        self.update_timer()
        self.update_status()
        self.update_text()
        self.update_button()
        
  
#----------------------------------------------------------

    def get_floor(self):
        return self._floor
    
    def get_position(self):
        return self._position
    
    def get_status(self):
        assert type(self._status) == states, "ERROR, Wrong type"
        ###print( self._status)
        return self._status
        #temp = self._status
        #return temp
    
    def get_timer(self):
        return self._timer.get()
    
    def get_img(self):
         return (pygame.transform.scale(self.img, gm.FLOOR_SIZE), self.get_position())
    
    def get_text(self):
        return self._timer_text.get()
        if self.get_status() == states.WAITING:
            return self._timer_text.get()
        return self.__empty.get()
    
    def get_buffer(self):
        return (self.__buffer, self.get_position())    
    
    def get_button(self):
        return self._button.get()
        
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
        self._timer_text = Button(self.calculate_timer_pos(),"00:00","black")
        
    def set_buffer(self):
        self.__buffer = pygame.Surface(gm.HORIZONTAL_BUFFER_SIZE)
        self.__buffer.fill(gm.HORIZONTAL_BUFFER_COLOR)
        
        
        
        
    

#-------------------------------------------------------------

    def update_status(self):
        if  self.get_status() == states.WAITING:
            
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
    
    def update_img(self):                           #maybe need to implement another one, with state as inputs
        pass

    def update_text(self):
        self._timer_text.update(str(self._timer),states.STILL)
        #self.set_text()

    def update_button(self):
        self._button.update(str(self.get_floor()),self.get_status()) 
        
#----------------------------------------------------------
#        
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
        return self._button.is_clicked(m_position)
    """
        m_position = convert(m_position)
        ##print(f"\n\n{self.get_floor()}")
        ##print(f"m_position: {m_position}")
        top_x, top_y = self.get_position()
        bottom_x, bottom_y = gm.FLOOR_SIZE[0], self.get_position()[1] - gm.FLOOR_SIZE[1]
        
        ##print(f"top: ({top_x}, {top_y}), bottom: ({bottom_x}, {bottom_y})")

        if m_position[0] <= top_x   and m_position[0] >= bottom_x:
           if m_position[1] <= top_y   and m_position[1] >= bottom_y:
            return True
        return False
        
        """

    def calculate_button_pos(self):
        
        return ( self.get_position()[0] + 20, self.get_position()[1] - 20)
               

    def calculate_timer_pos(self):
        return ( self.get_position()[0] + gm.FLOOR_SIZE[0] - (20 + self._timer_text.getrect().right),   self.get_position()[1] - 20)
       
    
#-------------------------------------------------------------
    def __str__ (self):
        return f'|floor: {self.get_floor()},  status: {self.get_status()}, timer: {self.get_timer()} |\n'
    
    def __repr__ (self):
       return f'|floor: {self.get_floor()},  status: {self.get_status()}, timer: {self.get_timer()} |\n'


"""
fl = Floor_2(0)
##print(fl.get_position())
##print(fl.is_clicked((15,15)))
"""