
import Graphic_Manager as gm

class Timer_2:
    def __init__(self):
        self.__seconds = 0
        self.__parts = 0
        self.__is_running = False
        
    def set(self, seconds, parts = 0):
        ##print  (f"1 Timer_2.Set: seconds: {seconds},  parts: {parts} \n self.__seconds: {self.__seconds}, self.__parts: {self.__parts}")  
        
        if type(seconds) == tuple:
            self.__seconds = seconds[0]
            self.__parts = seconds[1]
        else:
            self.__seconds = int(seconds)
            self.__parts = int(parts)
        
            
        ##print  (f"2 Timer_2.Set: seconds: {seconds},  parts: {parts} \n self.__seconds: {self.__seconds}, self.__parts: {self.__parts}")  
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
        if self.is_running():
            self.__parts -= 1
        
            if self.__parts < 0:                    #changed from <=
                self.__seconds -= 1
                self.__parts = gm.FRAN_RATE  - 1    #changed from exact FRAN_RATE
            
            if self.__seconds < 0:
                self.set_nulify()
                    
        assert self.__parts <=  gm.FRAN_RATE, "ERROR. too big"
    def get(self):
        return self.__seconds,  self.__parts

    def  set_nulify(self):
        self.__seconds = 0
        self.__parts = 0
        self.__is_running = False


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
            print("the timer is runnig: ", end="")
            if type(sec) == tuple:
                print("input is tuple: ", end="")
                print(f"the timer is runnig: ", end="")
                temp_sec =  self.__seconds + sec[0]
                temp_parts =  self.__parts + sec[1]
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
        if self.get()[0] >=10:
            sec = f"{self.get()[0]}"
        else:
             sec = f"0{self.get()[0]}"
             
        if self.get()[1] >= 10:
            parts =  f"{self.get()[1]}"
        else:
             parts = f"0{self.get()[1]}"
        
        return f"{sec}:{parts}"

        #return f"{self.get()[0]}:{self.get()[1]}"
    
        #return f"sec: {self.get()[0]}, parts: {self.get()[1]}, is running: {self.is_running()}\n"
      
    def __repr__(self):
        return f"sec: {self.get()[0]}, parts: {self.get()[1]}, is running: {self.is_running()}\n"
        

def get_with_addition(self, sec, parts = 0):
    temp_sec =  self.get()[0] + sec
    temp_parts = self.get()[1] + parts
        
    return calculate(temp_sec, temp_parts)

def calculate(sec = 0, parts = 0):
    if  parts < 0:
        sec -= abs(parts) // gm.FRAN_RATE
        parts = gm.FRAN_RATE - (abs(parts) % gm.FRAN_RATE)
        
        return  int(sec), int(parts)
        

    sec += parts // int(gm.FRAN_RATE)# * gm.WAIT_IN_FLOOR))
    parts = parts % int(gm.FRAN_RATE)# * gm.WAIT_IN_FLOOR))
   
    assert  int(sec) == sec and int(parts) == parts, "Numbers do not match"
    return int(sec), int(parts)
    


tim = Timer_2()

tim.set((2,30))

##print(tim.get())

tim.set(2,30)

##print(tim.get())