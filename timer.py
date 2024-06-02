class timer:
    __time_in_seconds = 0
    __frame_rate = 0
    __delta = 0
       
    
    def __init__(self, time_in_seconds = 0, frame_rate = 60):
        self.__time_in_seconds = time_in_seconds
        self.__frame_rate = frame_rate
        self.__delta = 0
        

    def update(self):
         if  self.__time_in_seconds == 0:
            if self.__delta > 0:
                 self.__delta -= 1
               #  print(f"update -- sec: {self.__time_in_seconds}, delta: {self.__delta}", end="\r") #, flush=True) 
          
            """    
           if self.__delta == 0:
                 #  print(f"update -- sec: {self.__time_in_seconds}, delta: {self.__delta}", end="\r") #, flush=True)
            elif self.__delta > 0:
                self.__delta -= 1
                     print(f"update -- sec: {self.__time_in_seconds}, delta: {self.__delta}", end="\r") #, flush=True) 
               """ 

         elif self.__time_in_seconds < 0:
            self.__time_in_seconds  = 0
            self.__delta = 0
            
         elif self.__delta > 0:      # if self.__time_in_seconds > 0:
             
            self.__delta -= 1
            #assert self.__delta >= 0, f"delta is wrong: {self.__delta}"
            #if self.__delta == self.__frame_rate:
            if self.__delta == 0:              # self.__frame_rate:
                self.__time_in_seconds -= 1
                self.__delta = self.__frame_rate
            """
            if  self.__time_in_seconds < 0:
                self.__time_in_seconds  = 0
                self.__delta = 0
            """
         elif self.__delta == 0:
               self.__time_in_seconds -= 1
               self.__delta = self.__frame_rate - 1
            
          
    
    def is_time_is_up(self):
        return self.__time_in_seconds == 0 and self.__delta == 0
    
    def get(self):
        return  self.__time_in_seconds, self.__delta
            
    
    def get_in_double(self):
        if self.__delta >= self.__frame_rate//2:
            return  self.__time_in_seconds + 0.5   
    
    def set(self, time_in_seconds, half_sec = 0):
         self.__time_in_seconds = time_in_seconds
         self.__delta = self.__frame_rate
    
         
    def get_exact(self):
        return int(self.__time_in_seconds), int(self.__delta)
    

    def set_exact(self, time_in_seconds, delta):
         self.__time_in_seconds = time_in_seconds
         self.__delta = delta
         
    #def change_time(self, time_in_seconds, half_sec = 0):
    def change_time(self, time_in_seconds, delta):
         self.__time_in_seconds += time_in_seconds
         """   
         for _ in range(0,half_sec):
             self.__add_half_sec()
         """
         self.__delta  += delta
       
         
    def __add_half_sec(self):
        self.__delta += int(self.__frame_rate // 2) 
        
        if self.__delta >= self.__frame_rate:
            self.__time_in_seconds += 1
            self.__delta = 0                # self.__frame_rate

    
    def get_with_addition(self, addition):
        ints = self.__time_in_seconds + addition[0]
        halfs = addition[1]
        
        if self.__delta >= self.__frame_rate//2:
            halfs  += 1
            
        ints += (int(halfs) // 2)
        
        halfs = int(halfs) % 2
            
        return ints + halfs * 0.5
    
    def get_exact_with_addition(self, addition):
        
        temp =  self.__time_in_seconds
       # ints = self.__time_in_seconds + addition[0]
        
        assert temp ==  self.__time_in_seconds, "unauthorised change hasben done"
        
        tmp_delta = self.__delta
        temp_time_in_seconds = self.__time_in_seconds
        
        tmp_delta += int(self.__delta + addition[1])
        
        temp_time_in_seconds += tmp_delta // self.__frame_rate
        tmp_delta = tmp_delta % self.__frame_rate

        assert temp ==  self.__time_in_seconds, "unauthorised change hasben done"
#        ints += int(int(self.__delta + addition[1]) // self.__frame_rate)# - 1
        
 #       delta = int(int(self.__delta + addition[1]) % self.__frame_rate)
            
        return (temp_time_in_seconds, tmp_delta)
    


    def __get_delta(self):
        return  self.__delta
         
    def __gt__ (self, other):
        if self.__time_in_seconds > other.__time_in_seconds:
            return True
        elif  self.__time_in_seconds == other.__get():
            if  self.__delta > other.__get_delta():
                return True
            
        return False
    
    def __eq__ (self, other):
         return self.__time_in_seconds == other.get_exact()[0]     and   self.__delta == other.get_exact()[1]

    def __repr__(self):
        return f'{self.__time_in_seconds}.{self.__delta}'
     
    def __str__(self):
         return f'{self.__time_in_seconds}.{self.__delta}'
        #return f'{self.get_in_double()}'
             