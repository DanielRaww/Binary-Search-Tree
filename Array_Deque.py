from Deque import Deque

class Array_Deque(Deque):

   def __init__(self):
    # capacity starts at 1; we will grow on demand.
      self.__capacity = 1
      self.__contents = [None] * self.__capacity
      self.__front = 0
      self.__back = 0
      self.__size = 0
    # TODO replace pass with any additional initializations you need.
    #pass
    
   def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    #pass
      if (self.__size == 0):
         return('[ ]')
      Num = str(self.__contents[self.__front])
      QBracket = ' '
      SPoint = 0
      while (SPoint < (self.__size - 1)):
         QBracket = QBracket + Num + ', '
         SPoint = SPoint + 1
         Num = str(self.__contents[(self.__front + self.__capacity + SPoint)%self.__capacity])
      QBracket = QBracket + Num
      QBracket = '['+QBracket+' ]'
      return QBracket
    
   def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
      #pass
      return self.__size
   def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
      #pass
      Contents = self.__contents
      self.__capacity = self.__capacity * 2
      self.__contents = [ None ] * self.__capacity
      for i in range(self.__size):
         self.__contents[i] = Contents[(self.__front + self.__size + i) % self.__size]
      self.__front = 0
      self.__back = self.__size - 1
      
   def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
      #pass
      if (self.__capacity <= self.__size):
         self.__grow()
      self.__front = (self.__front + self.__capacity - 1) % self.__capacity
      self.__contents[self.__front] = val
      self.__size += 1
     
   def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
      #pass
      if (self.__size == 0):
         return None
      Pop = self.__contents[self.__front]
      self.__front = (self.__front + self.__capacity + 1) % self.__capacity
      self.__size -= 1
      return Pop
      
         
   def peek_front(self):
    # TODO replace pass with your implementation.
      #pass
      if (self.__size == 0):
         return None
      return self.__contents[self.__front]
      
    
   def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
      #pass
      
      if (self.__capacity <= self.__size):
         self.__grow()
      #Contents = self.__contents
      self.__back = (self.__back + self.__capacity + 1) % self.__capacity
      self.__contents[self.__back] = val
      self.__size += 1
      
   def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
      #pass
      
      if (self.__size == 0):
         return None
      Pop = self.__contents[self.__back]
      self.__back = (self.__back + self.__capacity - 1) % self.__capacity
      self.__size -= 1
      return Pop

   def peek_back(self):
    # TODO replace pass with your implementation.
     # pass
      if (self.__size == 0):
         return None
      return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
  #pass
#   x = Array_Deque()
#   print(x)
#   x.push_back(5)
#   print(x)
#   x.push_front(10)
#   print(x)
#   print(x.peek_front())
#   print(x.peek_back())
#   print(x)
#   x.pop_back()
#   print(x)
#   x.pop_front()
#   print(x)