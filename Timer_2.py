
import Graphic_Manager as gm

class Timer_2:
    def __init__(self):
        self.__seconds = 0
        self.__parts = 0
        self.__is_running = False
        
    def set(self, seconds, parts = 0):
        if type(seconds) == tuple:
            self.__seconds = seconds[0]
            self.__parts = seconds[0]
        else:
            self.__seconds = int(seconds)
            self.__parts = int(parts)
        
            
            
        self.calculate()
        self.update_is_running()        
                
    def add(self, seconds, parts = 0):
        self.__seconds += seconds
        self.__parts += parts
        
        self.calculate()
        self.update_is_running()
    
    def remove(self, seconds, parts = 0):
        self.__seconds -= seconds
        self.__parts -= parts
        
        self.calculate()
        self.update_is_running()
    
    def update(self):
        self.__parts -= 1
        
        if self.__parts <= 0:
            self.__seconds -= 1
            self.__parts = gm.FRAN_RATE
            
            if self.__seconds < 0:
                self.__seconds = 0
                self.__parts = 0
                self.__is_running = False

    def get(self):
        return self.__seconds,  self.__parts

    def is_running(self):
        return self.__is_running

    def update_is_running(self):
        self.__is_running = self.calculate_if_running()
        
    def calculate_if_running(self):
        return self.__seconds > 0 or  self.__parts > 0
    
    def calculate(self):
         self.__seconds,  self.__parts = calculate(self.__seconds, self.__parts)
        
    def __eq__(self, other):
        return self.get()[0] == other.get()[0] and self.get()[1] == other.get()[1]

    def __sub__(self, other):
        temp_sec =  self.get()[0]+ other.get()[0]
        temp_parts = self.get()[1] + other.get()[1]
        
        return calculate(temp_sec, temp_parts)
       
    def get_with_addition(self, sec, parts = 0):
        temp_sec = 0
        temp_parts = 0
        if self.is_running():
            if type(sec) == tuple:
                temp_sec =  self.__seconds + sec[0]
                temp_parts =  self.__seconds + sec[1]
            else:
                temp_sec =  self.__seconds + sec
                temp_parts = self.__parts + parts
        
            return calculate(temp_sec, temp_parts)
        
        else:
             if type(sec) == tuple:
                return calculate(sec[0], sec[1])
             else:        
                 return calculate(sec, parts)

    def __str__(self):
        return f"sec: {self.get()[0]}, parts: {self.get()[1]}, is running: {self.is_running()}\n"
      
    def __repr__(self):
        return f"sec: {self.get()[0]}, parts: {self.get()[1]}, is running: {self.is_running()}\n"
        

def get_with_addition(self, sec, parts = 0):
    temp_sec =  self.get()[0] + sec
    temp_parts = self.get()[1] + parts
        
    return calculate(temp_sec, temp_parts)

def calculate(sec = 0, parts = 0):
    sec += parts // int(gm.FRAN_RATE)# * gm.WAIT_IN_FLOOR))
    parts = parts % int(gm.FRAN_RATE)# * gm.WAIT_IN_FLOOR))
    
    return int(sec), int(parts)
    
