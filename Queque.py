import random


class Node:
     data = None
     next_ = None
     def __init__ (self, data = None, next_1 = None):
        if type(data) != None:
            self.data = data 
        self.next_ = next_1
   


     def set_data(self, data):
        self.__data = data
     
     def set_next(self, next_):
        self.__data = next_


     def get_data(self):
        return self.data
     
     def get_next(self):
        return self.next_

     def __repr__(self):
         return f'data: {self.data}, next: {self.next_.data}'
     
     def __str__(self):
         return f'data: {self.data}'
     

class Queque_0:
    size = 0
    head = None
    tail = None
    
    def __init__ (self, data = None):
        self.size = 0
        if type(data) != None:
           self.init(data)
       
           
    def init(self, data):
        #
        new_node = Node(data)
        self.head = new_node
        self.tail =  self.head
        self.size = 1
        
       #print(f'inserted data: {data} end of Queque.init, self.head.data: {self.head.data}')
        
        assert type(self.head) != None, "inside Queque.init"
        
    def push(self, data):
#        new_node = Node(data)

        if self.head == None or  self.head.data == None:
            self.init(data)
            assert type(self.head) != None, "inside Queque.push 1"
        else:
            assert type(self.head) != None, "inside Queque.push 1.5"
            new_node = Node(data)
            assert type(self.head) != None, "inside Queque.push 2.1"
            #self.head.next_ = new_node
            self.tail.next_ = new_node
            assert type(self.head) != None, "inside Queque.push 2.2"
            self.tail = self.tail.next_
            assert type(self.head) != None, "inside Queque.push 2.3"
            self.size += 1

            assert type(self.head) != None, "inside Queque.push 2.4"

        """
        if self.is_empty():
            self.head = Node(data)
            self.__tail = self.head
            
        else:
            tem
            self.tail = Node(self.tail.get_data(), Node(data))
            self.tail  = self.tail.get_next()
            
        self.size += 1
        """    
   
    def pop(self):
       #print("pop")
        
        if self.head != None and self.size >= 1:
            data = self.head.get_data()
            
            self.head = self.head.get_next()
            self.size -= 1
            
            return data           
    
    def peek(self):
        assert type(self.head) != None, "inside Queque.peek"
        assert type(self.head.data) != None, "inside Queque.peek"
       #print(type(self.head))
       #print("peek")
       #print(self.head)
       # data = self.head.get_data()
        data = self.head.data
        return data


    def get_size(self):
        return self.size
    
    def is_empty(self):
      #print(f'size: {self.get_size()}')
       #print(self)
       return self.get_size() <= 0 or self.head == None or self.head.data == None
   
    def __repr__(self) -> str:
        temp = self.head
        data = ""
        
        while temp != None:
            data += f" {temp.get_data()},"
            temp = temp.get_next()
        return data
        
    def __str__(self):
        
        return self.__repr__()
        
        
        
def test():
    data = [random.randint(1,10) for _ in range(10)]
   #print(data)
    
    q = Queque(data[0])
   #print(f'initilize: {q}')
    
    for i in range(1,8,2):
        q.push(data[i])
       #print(f'pushing: {data[i]}')
       #print(f'first push:{q}')

       #print(f'first peek: {q.peek()}')
       
        q.push(data[i+1])
       #print(f'pushing: {data[i+1]}')
       #print(f'second push:{q}')

        q.pop()
       #print(f'pop:{q}')
        
       #print(f'second peek: {q.peek()}')
        
       #print(f'end of loo:{q}')
        
    while not q.is_empty():
        q.pop()
       #print(f'pop:{q}')
        

#test()