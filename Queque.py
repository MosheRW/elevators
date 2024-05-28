class Node:
     def __init__ (self, data = 0):
         self.__data = data
         self.__next = None
        
         if type(data) != int or data != 0:
              self.__size = 1
         else:
              self.__size = 0


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
    def __init__ (self, init_data = "start"):
        self.__head = Node(init_data)
        self.__tail = self.__head
        
    def push(self, data):
        self.__tail.set_next(Node(data))
        self.__tail  = self.__tail.get_next()
        self.__size += 1
        
    def pop(self):
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
        else:
            return self.__tail.get_data()
            
    


    def get_size(self):
        return self.__size
    
    def is_empty(self):
       return self.get_size() == 1
   
    def __repr__(self) -> str:
        temp = self.__head
        data = ""
        while temp != None:
            data += f" {temp.get_data()},"
            temp = temp.get_next()
        return data
        
    def __str__(self):
        return self.__repr__()
        
        
        
