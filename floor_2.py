import pygame

import Graphic_Manager as gm
from Timer_2 import Timer_2

from Button import Button
from Button import states



class Floor_2:
    
    def __init__(self, floor = 0):
        
        #data
        self._floor = floor
        self._position = get_init_position(self._floor)
        
        self._status = states.STILL
        self._timer = Timer_2()
        
        #graphics
        self.img =  pygame.image.load(gm.FLOOR_PIC_FILE).convert()                  #the floor img
        
        self._button = Button(self.__calculate_button_pos(),str(self.__get_floor()),(255,255,255))    #the elevator invite button (also display thefloor number)
        self._timer_text = Button(self.__get_position(),"00:00","gray")            #the timer display module. appearing when the timer is on
        self.__empty = Button(self.__get_position(),"","black",  False)        #outputing this case the timer isnt on
        
        self.__buffer = pygame.Surface(gm.HORIZONTAL_BUFFER_SIZE)                   #the buffer module
        self.__buffer.fill(gm.HORIZONTAL_BUFFER_COLOR)
        
        pygame.mixer.music.load(gm.DING_FILE)


#---------------------------------------------------------------------------------
        
    def init(self, floor):
        self._floor = floor
        
        self.set_status(states.STILL)
        self.set_position( get_init_position(floor))
        
        self._button.set(self.__calculate_button_pos(),str(self.__get_floor()),(255,255,255))
        self._timer_text.set(self.__calculate_timer_pos(), "00:00", "gray")
        
        self.__set_buffer()
        
        pygame.mixer.music.load(gm.DING_FILE)
        
        
#---------------------------------------------------------------------------------
        
    def is_this_floor_needs_an_elevator(self):
        return self.__get_status() == states.STILL
    

    def get_elevator(self, time):        
        self.set_timer(time)
        self.set_status(states.WAITING)
        
#----------------------------------------------------------------------------------

    #get the surface's of the class
    def get(self):    
        return (self.__get_img(), self.__get_text(), self.__get_button(),self.__get_buffer())
    
    #update the class variables, timers and statuses
    def update(self, iterations = 1): 
        #if iterations >= 1:
            self.__update_timer(iterations)
            self.__update_status()
            self.__update_text()
            self.__update_button()
        
  
#----------------------------------------------------------

    def __get_floor(self):
        return self._floor
    
    def __get_position(self):
        return self._position
    
    def __get_status(self):
        assert type(self._status) == states, "ERROR, Wrong type"
        return self._status
    
    def __get_timer(self):
        return self._timer.get()
    
    def __get_img(self):
         return (pygame.transform.scale(self.img, gm.FLOOR_SIZE), self.__get_position())
    
    def __get_text(self):        
        if self.__get_status() == states.WAITING:
            return self._timer_text.get()        
        return self.__empty.get()
    
    def __get_buffer(self):
        return (self.__buffer, self.__get_position())    
    
    def __get_button(self):
        return self._button.get()
        
#-----------------------------------------------------------

    def set_position(self,new_position):
        assert type(new_position) == tuple, "ERROR, incorrect value of new_position"
        self._position = new_position
        
    def set_status(self, new_status):
        assert type(new_status) == states, "ERROR, incorrect value of new_position"
        self._status = new_status
        self.__update_img()
        
    def set_timer(self, new_time):
        self._timer.set(new_time)

    def set_img(self,filename):
         self.img =  pygame.image.load(gm.FLOOR_PIC_FILE).convert()
         
    def __set_text(self):
        self._timer_text = Button(self.__calculate_timer_pos(),"00:00","black")
        
    def __set_buffer(self):
        self.__buffer = pygame.Surface(gm.HORIZONTAL_BUFFER_SIZE)
        self.__buffer.fill(gm.HORIZONTAL_BUFFER_COLOR)
        
        
#-------------------------------------------------------------
    # updates section        

    def __update_status(self):
        if  self.__get_status() == states.WAITING:                
            
            if not self._timer.is_running():                     #case elevator isnt here
                
                self.set_status(states.ELEVATOR_HERE)
                self.set_timer(gm.WAIT_IN_FLOOR)
                self.play_ding()
                
                
        elif self.__get_status() == states.ELEVATOR_HERE:          #case elevator is here
            
            if not self._timer.is_running():
                self.set_status(states.STILL)                       
    
    def __update_timer(self, iterations = 1):
        self._timer.update(iterations)
    
    def __update_img(self):
        #can change the elevator pic when the status changes
        pass

    def __update_text(self):
        self._timer_text.update(str(self._timer),states.STILL)
       
    def __update_button(self):
        self._button.update(str(self.__get_floor()),self.__get_status()) 
        
#----------------------------------------------------------
        
    def play_ding(self):        
        pygame.mixer.music.play()

    #boolean: returns true if the floors buttton clicked
    def is_clicked(self, m_position):
        return self._button.is_clicked(m_position)
    
#----------------------------------------------------------
    
    def __calculate_button_pos(self):        
        return ( self.__get_position()[0] + gm.IDENTATION,  self.__get_position()[1] - gm.IDENTATION)
               
    def __calculate_timer_pos(self):
        return (self.__get_position()[0] + gm.FLOOR_SIZE[0] - (gm.IDENTATION + self._timer_text.getrect().right),
                self.__get_position()[1] - gm.IDENTATION)
       
    
#-------------------------------------------------------------
    def __str__ (self):
        return f'|floor: {self.__get_floor()},  status: {self.__get_status()}, timer: {self.__get_timer()} |\n'
    
    def __repr__ (self):
       return f'|floor: {self.__get_floor()},  status: {self.__get_status()}, timer: {self.__get_timer()} |\n'


   
def get_init_position(serial, first_floor_is = 0):
     return (0, gm.FLOOR_SIZE[1] + (serial - first_floor_is) * (gm.ELEVATOR_SIZE[0]))
         