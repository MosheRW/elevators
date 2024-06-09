from re import I
import pygame
from enum import Enum

import Graphic_Manager as gm
import Timer_2


ele_status = Enum('ele_status',['GOING_UP','GOING_DOWN', 'STILL', 'DOORS_OPEN', 'INVITED'])


class Elevator:
    def __init__(self,serial,starting_point = 0):
        
        self._queque = []                   #queque of floors wiatinf to the elevator
        self._floor  = int(starting_point)  #the last floor the elevator parked in
        self._serial = serial               #the elevator serial number from all the elevators
        self._position = (0,0)              #the position on the screen in Euclidean values
        
        self._status = ele_status.STILL     #the status of the elevator, one five availables above.(enum. initilize to still)
        self.img =  pygame.image.load(gm.ELEVATOR_PIC_FILE).convert()   #img representation of the elevator
        
        self.novment_counter = 0            #counts the pixels the elevator moves from the last time the elevators opend its doors
        self.novment_limit = 0              #the num of pixels the elevator need to move until its next destnation         
        
        self._time_until_clear = Timer_2.Timer_2()          #timer object. store the time until the end of the entire scedualed travel, including the waiting time at any floor
        self._time_to_end_status = Timer_2.Timer_2()        #timer object. store the time until the current operation will end.

#--------------------------------------------------------------------------#       
    #set the Euclidean location of the elevator
    def set(self, position):
        self.set_position(position)
          
    #get the graphical represntations end Euclidean location of the elevator in a tuple
    def get(self) -> tuple:
        return (self.get_img(),self.get_position())
    
    #updates the location, graphic represantation, status and timers of the elevator 
    def update(self):
         self.move()  
         self.update_big_timer()
         self.update_small_timer()
         self.update_status()
         self.update_img()

#--------------------------------------------------------------------------#       
             
    
    # is_call_worthy:       <-      attantion: this function will not change any stored data!
    # calculate ans returns the time it'ill take to the elevator to get to a specific floor,
    # concidering the current time sceduale, and the time it will take to travel to new floor
    def is_call_worthy(self, floor):
        
        # getting the last floor in line
        last_floor_in_line = self.__get_last_floor_in_line()                                    
        
        # calculating the time travel from the last floor in line - to the new floor
        the_new_jurny_time = calculate_time_from_one_store_to_another(last_floor_in_line,floor) 
        
        # calculating and returning the current time scedualed with the addition of time of the new floor
        return self._time_until_clear.get_with_addition(the_new_jurny_time)
    

    #-----------------------------------------------   
    # call function:
    # adding the new call to the sceduale and the queque
    def call(self, floor):
        #cases that no need to make a change - even the elevator calld       
        if self.__get_last_floor_in_line() == floor:
                return  self.get_time().get()
               
        #calculating the time untill the arriving in the newest scedualded floor
        new_time = self.is_call_worthy(floor) 
        
        #adding the newely invited floor to the queque
        self._queque.append(floor)
        
        # if the elevator is on stil state - setting it to ivited status
        # so in the next update, it will calculate the direction of movment and moves
        if  self.get_status() == ele_status.STILL:
             self.set_status(ele_status.INVITED)
             
        #setting the ncalculated time             
        self._time_until_clear.set(new_time)     
       
        # adding the 'waiting in floor' time on top of the 'waiting to the elevator' time,
        # so we will know when the elevator will be available again
        self._time_until_clear.add(gm.WAIT_IN_FLOOR,0) 
        
        
        assert type(new_time) == tuple and new_time != (0,0), "ERROR"        
        
        # retuning the time without the recently added wait in floor time
        # so we can know when elevator will arrive at the newely scedualed floor
        return  new_time
        

#-----------------------------------------------------------------------------------------------
    #the get functions
        
    def get_time(self):
        return self._time_until_clear   

    def get_position(self):
        return self._position
  
    def get_img(self):        
        return pygame.transform.scale(self.img, gm.ELEVATOR_SIZE)    
    
    def get_status(self):
        return self._status
    
    def get_floor(self):
        return self._floor
           
    # get_last_floor_in_line returns the last floor in line,
    # or the current floor if there is no floor in line
    def __get_last_floor_in_line(self):
          if(len(self._queque) > 0):
                 return self._queque[-1]
          return self.get_floor()
              

#--------------------------------------------------------------------
      
    def set_position(self, position, y = 0):
        if type(position) == tuple:
            self._position = position            
        else:
            self._position[0] = position
            self._position[1] = y                

    def set_img(self, filename = gm.ELEVATOR_PIC_FILE):
        self.img = pygame.image.load(filename).convert()
       
    def set_status(self, new_status):
        self._status = new_status
        
    def set_floor(self, new_floor):
        self._floor = new_floor
    

#--------------------------------------------------------------------
 
    def update_img(self):
        if self.get_status() == ele_status.DOORS_OPEN:            
            self.set_img(gm.ELEVATOR_GREEN_PIC_FILE)            
        else:
             self.set_img()
                        
    def update_big_timer(self):
        self._time_until_clear.update()
        
    def update_small_timer(self):
        self._time_to_end_status.update()
             
    def update_status(self):
         self.update_status_case_still()
         self.update_status_case_moving()
         self.update_status_case_doors_opened()
         self.update_status_case_invited()

#--------------------------------------------------------------------
    
    #update status methodes and calculators
    def update_status_case_still(self):
          if self.get_status() == ele_status.STILL:            
            assert len(self._queque) == 0, "error. still even there is floors in line"
            
    def update_status_case_moving(self):        
        if (self.get_status() == ele_status.GOING_DOWN
            or self.get_status() == ele_status.GOING_UP ) \
                and self.is_got_to_place():                        
                    self.open_the_doors()
                
    def update_status_case_doors_opened(self):
         if self.get_status() == ele_status.DOORS_OPEN:
            
            if self._time_to_end_status.is_running():
                pass 
            
            elif len(self._queque) > 0:
                self.set_status(ele_status.INVITED)
                
            else:
                 self.set_status(ele_status.STILL)
                 self._time_until_clear.set_nulify()

    def update_status_case_invited(self):
        if self.get_status() == ele_status.INVITED:
            if len(self._queque) > 0:                
                self.set_status(self.calculate_movment_direction(self._queque[0]))
                self.update_novment_limit(self._queque[0])
                self.__destination = self._queque[0]
            else:
                self.set_status(ele_status.STILL)       
  
    def update_novment_limit(self, end):
        self.novment_limit = calculate_novment_limit(self._floor,end)
        self.novment_counter = 0

    def open_the_doors(self):    
        self._time_to_end_status.set(gm.WAIT_IN_FLOOR)
        self.set_status(ele_status.DOORS_OPEN)
        self.set_floor(self._queque.pop(0))
           
    def is_got_to_place(self):
        return self.novment_counter >= self.novment_limit    
 
    def calculate_movment_direction(self, end):
        return calculate_movment_direction(self._floor,end)
        

#--------------------------------------------------------------------
    #movemant methodes
    def move(self):
        if self.get_status() == ele_status.GOING_UP:
             self.move_up()
        elif  self.get_status() == ele_status.GOING_DOWN:
             self.move_down()

    def move_up(self):
        self._position = (self._position[0], self._position[1] + gm.PACE)
        self.novment_counter += gm.PACE
    
    def move_down(self):
         self._position = (self._position[0], self._position[1] - gm.PACE)
         self.novment_counter += gm.PACE         
    
#--------------------------------------------------------------------
    #textual representation functions    
    def __str__(self):
        return f"\nserial: {self._serial}, status: {self._status}, position: {self._position}, timer: {self._time_until_clear}" 
    
    def __repr__(self):
        if len(self._queque) > 0:
            temp = str(self._queque[0])
        else: ""
        
        return f"\nserial: {self._serial}, status: {self._status} " +  temp + f", position: {self._position}, timer: {self._time_until_clear}, small timer: {self._time_to_end_status}, movments: {self.novment_counter}"

#--------------------------------------------------------------------


def get_init_position(serial, first_elevator_is = 1) -> tuple:
            return (int(gm.FLOOR_SIZE[0] + gm.SPACE + gm.ELEVATOR_SIZE[0] + 
                        (serial - first_elevator_is) * (gm.ELEVATOR_SIZE[0] + gm.SPACE)), 
                int(gm.ELEVATOR_SIZE[1]))

def calculate_time_from_one_store_to_another(strt, end):
    return Timer_2.calculate(0,int(abs(strt - end)) * gm.FRAMES_TO_CROSS_A_FLOOR)

              
def calculate_movment_direction(strt, end):
        if strt > end:
            return ele_status.GOING_DOWN
        elif strt < end:
            return ele_status.GOING_UP
        #else:
         #   return ele_status.GOING_DOWN

def calculate_novment_limit(strt, end):
    return int(abs(strt - end) * gm.ELEVATOR_SIZE[1])

#------------------------------------------------------
def test()        :
    
    pygame.init
    screen = gm.get_screen()
    clock = pygame.time.Clock()
    ele = Elevator(0)
    
    floor = 4
    
    ###print(ele)

    ###print(ele.is_call_worthy(floor))
    
    count = 0
    
    #screen.fill("white")
    #screen.set_colorkey()
    
    while True:
         count += 1
         
         if count == 240:
            ele.call(floor)
         
         ele.update()
         
        
         
         screen.fill("white")
         screen.set_colorkey()
         
         screen.blit(ele.get_img(), ele.get_position())
         pygame.display.flip()
    
         clock.tick(60)  # limits FPS to 60
   # ###print(ele.is_call_worthy(5))

    ###print(ele)

#test()

####print(calculate_time_from_one_store_to_another(0,5) )