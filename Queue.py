from Deque_Generator import get_deque

class Queue:

   def __init__(self):
      self.__dequ = get_deque()

   def __str__(self):
      # TODO replace pass with your implementation.
      #pass
      return str(self.__dequ)
     
   def __len__(self):
      # TODO replace pass with your implementation.
      #pass
      return len(self.__dequ)
     
   def enqueue(self, val):
      # TODO replace pass with your implementation.
      #pass
      self.__dequ.push_back(val)
     
   def dequeue(self):
      # TODO replace pass with your implementation.
      #pass
      return(self.__dequ.pop_front())
# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
