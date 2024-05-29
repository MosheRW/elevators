class Node:
     __data = None
     __next = None
     def __init__ (self, data = None, next_ = None):
        if type(data) != None:
            self.__data = data 
        self._next = next_
   


     def set_data(self, data):
        self.__data = data
     
     def set_next(self, next_):
        self.__data = next_

     def get_data(self):
        return self.__data
     
     def get_next(self):
        return self.__next

     def __repr__(self):
         return f'data: {self.__data}, next: {self.__next.__data}'
     
     def __str__(self):
         return f'data: {self.__data}'
     

class Queque:
    size = 0
    head = None
    tail = None
    def __init__ (self, data = None):
        if type(data) != None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        else:
            self.head = None
            self.tail = None
            self.size = 0
           

    def push(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.__tail = self.head
            
        else:
            self.tail = Node(self.tail.get_data(), Node(data))
            self.tail  = self.tail.get_next()
            
        self.size += 1
        
    def pop(self):
        print("pop")
        if self.head != None:
            data = self.head.get_data()
            if self.head.get_next() == None:
                self.__init__()
            else:
                self.__head = self.__head.get_next()
                self.__size -= 1
        
        return data
    
    def peek(self, pos = "head"):
        print('peek')
        if pos == "head":
            return self.head.get_data()
        else: #get tails
            return self.__tail.get_data()
            
    


    def get_size(self):
        return self.size
    
    def is_empty(self):
       print(f'size: {self.get_size()}')
       #print(self)
       return self.get_size() == 0
   
    def __repr__(self) -> str:
        temp = self.head
        data = ""
        while temp != None:
            data += f" {temp.get_data()},"
            temp = temp.get_next()
        return data
        
    def __str__(self):
        
        return self.__repr__()
        
        
        
