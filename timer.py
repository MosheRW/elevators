class timer:
    def __init__(self, time_in_seconds = 0, frame_rate = 60):
        self.__time_in_seconds = time_in_seconds
        self.__frame_rate = frame_rate
        self.__delta = frame_rate
        

    def update(self):
        self.__delta -= 1
        
        if self.__delta == self.__frame_rate:
            self.__time_in_seconds -= 1
            self.__delta = self.__frame_rate
            

    def get(self):
        return  self.__time_in_seconds
            
    
    def get_in_double(self):
        if self.__delta >= self.__frame_rate/2:
            return  self.__time_in_seconds + 0.5   
    
    def set(self, time_in_seconds):
         self.__time_in_seconds = time_in_seconds
         self.__delta = self.__frame_rate
         
    def change_time(self, time_in_seconds, half_sec = 0):
         self.__time_in_seconds += time_in_seconds
         for _ in range(half_sec):
             self.__add_half_sec()

    def __add_half_sec(self):
        self.__delta += self.__frame_rate / 2
        
        if self.__delta >= self.__frame_rate:
            self.__time_in_seconds += 1

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
         return self.__time_in_seconds == other.__get()     and   self.__delta == other.__get_delta()

    def __repr__(self):
        return f'{self.__time_in_seconds}.{self.__delta}'
     
    def __str__(self):
        return f'{self.get_in_double()}'
             