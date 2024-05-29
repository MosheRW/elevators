class Node:
     __data = None
     __next = None
     def __init__ (self, data = None, next_ = None):
        if type(data) != None:
            self.__data = data 
        self._next = next_
   


     def set_data(self, data):
        self.__data = data
     
     def set_next(self, next):
        self.__data = next

     def get_data(self):
        return self.__data
     
     def get_next(self):
        return self.__next

     def __repr__(self):
         return f'data: {self.__data}, next: {self.__next.__data}'
     
     def __str__(self):
         return f'data: {self.__data}'
     

class Queque:
    __size = 0
    __head = None
    __tail = None
    def __init__ (self, data = None):
        if type(data) != None:
            self.__head = Node(data)
            self.__tail = self.__head
            self.__size += 1
           

    def push(self, data):
        if self.is_empty():
            self.__head = Node(data)
            self.__tail = None
            
        else:
            self.__tail = Node(data, self.__tail.get_next())
            self.__tail  = self.__tail.get_next()
            
        self.__size += 1
        
    def pop(self):
        if self.__head != None:
            data = self.__head.get_data()
            if self.__head.get_next() == None:
                self.__init__()
            else:
                self.__head = self.__head.get_next()
                self.__size -= 1
        
        return data
    
    def peek(self, pos = "head"):
        
        if pos == "head":
            return self.__head.get_data()
        else: #get tails
            return self.__tail.get_data()
            
    


    def get_size(self):
        return self.__size
    
    def is_empty(self):
       return self.get_size() == 0
   
    def __repr__(self) -> str:
        temp = self.__head
        data = ""
        while temp != None:
            data += f" {temp.get_data()},"
            temp = temp.get_next()
        return data
        
    def __str__(self):
        
        return self.__repr__()
        
        
        
