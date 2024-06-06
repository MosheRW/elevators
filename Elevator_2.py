
import pygame
#import Queque
import Graphic_Manager as gm
from enum import Enum
import Timer_2


ele_status = Enum('ele_status',['GOING_UP','GOING_DOWN', 'STILL', 'DOORS_OPEN', 'INVITED'])

def get_init_position(serial, first_elevator_is = 1) -> tuple:
            return (int(gm.FLOOR_SIZE[0] + gm.SPACE + gm.ELEVATOR_SIZE[0] + (serial - first_elevator_is) * (gm.ELEVATOR_SIZE[0] + gm.SPACE)),     int(gm.ELEVATOR_SIZE[1]))

class Elevator:
    screen = gm.get_screen()
    
    def __init__(self,serial,starting_point = 0):
        pygame.init
        
        self._queque = []
        self._floor  = int(starting_point)
        self._serial = serial
        self._position = (0,0)
        
        self._status = ele_status.STILL
        self.img =  pygame.image.load(gm.ELEVATOR_PIC_FILE).convert()
        self.novment_counter = 0
        self.novment_limit = 0
        
        self._time_until_clear = Timer_2.Timer_2()
        
        self._time_to_end_status = Timer_2.Timer_2()

        self.__destination = 0

#--------------------------------------------------------------------------
#        
    def set(self, position):
        self.set_position(position)
          
    def get(self):
        #return self.screen.blit(self.get_img(),self.get_position())
        return (self.get_img(),self.get_position())
             

    def is_call_worthy(self, floor):
        if(len(self._queque) > 0):
              temp = self._time_until_clear.get_with_addition(calculate_time_from_one_store_to_another(self._queque[-1],floor))
        else:
             temp = self._time_until_clear.get_with_addition(calculate_time_from_one_store_to_another(self._floor,floor))
             #temp = self._time_until_clear.get_with_addition(calculate_time_from_one_store_to_another(self.__destination,floor))
             
        #print(f"{self._serial} Elevator.is_call_worthy.temp: {temp}")
        return temp


    def call(self, floor):
        #print("\n\n" + str(self.get_status()) + "\n")
        if len(self._queque) > 0:
            print(">>>")
            if self._queque[-1] == floor:
                return  self.get_time().get()
        
        elif len(self._queque) == 0:
            if self._floor == floor:
                return   self.get_time().get() #(0,0)
        
          
        #---------#
            
        temp = self.is_call_worthy(floor) 
        self._queque.append(floor)
   
       # if  self.get_status() != ele_status.DOORS_OPEN:
        if  self.get_status() == ele_status.STILL:
             self.set_status(ele_status.INVITED)
             """
             temp = self._time_until_clear.get_with_addition(calculate_time_from_one_store_to_another(self._floor,floor))
        else:
            temp = self._time_until_clear.get_with_addition(calculate_time_from_one_store_to_another(self._queque[-1],floor))
                """     
        #temp = self.is_call_worthy(floor) 
        
        ##print(F"call.temp: {temp}")
        self._time_until_clear.set(temp)     
        #self._time_until_clear.add(temp[0], temp[1])
       
        temp2 = self.get_time().get() 
        self._time_until_clear.add(2)
        
        #temp = self._time_until_clear.get()
        assert type(temp) == tuple, "ERROR"
        assert temp != (0,0), "ERROR"
        
        print(f"Elevator_2.call.temp: {temp}")
        print(f"Elevator_2.call.temp2: {temp2}")
        
        #if self.get_status() == ele_status.STILL:
         #   return temp2
        #return  self._time_until_clear.get()
        return  temp
        
       
    def get_time(self):
        return self._time_until_clear
   
    def update(self):
         self.move()  
         self.update_big_timer()
         self.update_small_timer()
         self.update_status()
         self.update_img()


    def get_position(self):
        return self._position
    
    def set_position(self, position, y = 0):
        if type(position) == tuple:
            self._position = position
            
        else:
            self._position[0] = position
            self._position[1] = y            
    

    def get_img(self):
        
        return pygame.transform.scale(self.img, gm.ELEVATOR_SIZE)
    


    def set_img(self, filename = gm.ELEVATOR_PIC_FILE):
        self.img = pygame.image.load(filename).convert()
    
    def update_img(self):
        if self.get_status() == ele_status.DOORS_OPEN:
            
            self.set_img(gm.ELEVATOR_GREEN_PIC_FILE)
            
        else:
             self.set_img()
            

    def get_status(self):
        return self._status
    
    def set_status(self, new_status):
        self._status = new_status
        
    def get_floor(self):
        return self._floor
    
    def set_floor(self, new_floor):
        self._floor = new_floor
    
        
    def update_big_timer(self):
        self._time_until_clear.update()
        ##print(self._time_until_clear)
    
    def update_small_timer(self):
        self._time_to_end_status.update()
    

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
    

    def is_got_to_place(self):
        return self.novment_counter >= self.novment_limit
    
    def open_the_doors(self):    
        self._time_to_end_status.set(gm.WAIT_IN_FLOOR)
        self.set_status(ele_status.DOORS_OPEN)
        self.set_floor(self._queque.pop(0))
        #<------
    
    def update_status_case_still(self):
          if self.get_status() == ele_status.STILL:            
            pass  
              # self.set_status(self.get_status())
            #maybe check if got invited?

    def update_status_case_moving(self):
        if self.get_status() == ele_status.GOING_DOWN or self.get_status() == ele_status.GOING_UP:
            if(self.is_got_to_place()):
                 self.open_the_doors()
                
    def update_status_case_doors_opened(self):
         if self.get_status() == ele_status.DOORS_OPEN:
            if self._time_to_end_status.is_running():
                pass # self.set_status(self.get_status())
            elif len(self._queque) > 0:
                self.set_status(ele_status.INVITED)
                #self.update()
               # dbug =input("is the elevator ariived too early?: ")
            else:
                 self.set_status(ele_status.STILL)
                 self._time_until_clear.set_nulify()
                # dbug =input("is the elevator ariived too early?: ")
                


    def update_status_case_invited(self):
        if self.get_status() == ele_status.INVITED:
            if len(self._queque) > 0:                     
                #self.set_status(self.calculate_movment_direction(self._floor))
                self.set_status(self.calculate_movment_direction(self._queque[0]))
                self.update_novment_limit(self._queque[0])
                self.__destination = self._queque[0]
            else:
                self.set_status(ele_status.STILL)
        
    def update_status(self):
         self.update_status_case_still()
         self.update_status_case_moving()
         self.update_status_case_doors_opened()
         self.update_status_case_invited()
   
    def calculate_movment_direction(self, end):
        return calculate_movment_direction(self._floor,end)
        

    def update_novment_limit(self, end):
        self.novment_limit = calculate_novment_limit(self._floor,end)
        self.novment_counter = 0
        


    def __str__(self):
        return f"\nserial: {self._serial}, status: {self._status}, position: {self._position}, timer: {self._time_until_clear}" 
    
    def __repr__(self):
        if len(self._queque) > 0:
            temp = str(self._queque[0])
        else: ""
        
        return f"\nserial: {self._serial}, status: {self._status} " +  temp + f", position: {self._position}, timer: {self._time_until_clear}, small timer: {self._time_to_end_status}, movments: {self.novment_counter}"
    

def calculate_time_from_one_store_to_another(strt, end):
    #print (f"{abs(strt - end)}, strt:{strt}, end:{end}")
    return Timer_2.calculate(0,int(abs(strt - end)) * gm.FRAMES_TO_CROSS_A_FLOOR)
             

 
def calculate_movment_direction(strt, end):
        if strt > end:
            return ele_status.GOING_DOWN
        elif strt < end:
            return ele_status.GOING_UP
        else:
            return ele_status.GOING_DOWN

def calculate_novment_limit(strt, end):
    return int(abs(strt - end) * gm.ELEVATOR_SIZE[1])
"""
#if strt <= end:
    if strt < end:
        return (end - strt) * (gm.ELEVATOR_SIZE[1] + gm.SPACE)
    elif strt > end:
        return (strt - end) *(gm.ELEVATOR_SIZE[1] + gm.SPACE)
    else:
        return 0
"""            
             
       # assert strt != end, "ERROE"
            
        
        

#------------------------------------------------------
def test()        :
    
    pygame.init
    screen = gm.get_screen()
    clock = pygame.time.Clock()
    ele = Elevator(0)
    
    floor = 4
    
    #print(ele)

    #print(ele.is_call_worthy(floor))
    
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
   # #print(ele.is_call_worthy(5))

    #print(ele)

#test()

##print(calculate_time_from_one_store_to_another(0,5) )