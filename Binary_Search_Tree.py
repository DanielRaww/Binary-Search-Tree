from Queue import Queue
class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

   class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.
   
      def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None
         self.height = 1
      # TODO complete Node initialization

   def __init__(self):
      self.__root = None
    # TODO complete initialization

   def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    #pass # TODO replace pass with your implementation
      self.__root = self.ins_rec_elem(value, self.__root)
    
   def ins_rec_elem(self, value, t):
      if t is None:
         t = self.__BST_Node(value)
      elif value < t.value:
         t.left = self.ins_rec_elem(value, t.left)
      elif value > t.value:
         t.right = self.ins_rec_elem(value, t.right)
      elif value is t.value:
         raise ValueError
      
      if t.left:  
         if t.height is t.left.height:
            t.height += 1
      if t.right:
         if t.height is t.right.height:
            t.height += 1
      return t
       
   def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    #pass # TODO replace pass with your implementation
      self.__root = self.rem_rec_elem(value, self.__root)
    
   def rem_rec_elem(self, value, t):
      if t == None:
         raise ValueError
         
      elif value > t.value:
         t.right = self.rem_rec_elem(value, t.right)
         if t.right is None and t.left is None:
            t.height = 1
         elif t.right is None and t.left is not None:
            t.height = 1 + t.left.height
         elif t.right is not None and t.left is None:
            t.height = 1 + t.right.height
         elif t.right is not None and t.left is not None:
            t.height = 1 + max(t.left.height, t.right.height)
         return t
      
      elif value < t.value:
         t.left = self.rem_rec_elem(value, t.left)
         if t.right is None and t.left is None:
            t.height = 1
         elif t.right is None and t.left is not None:
            t.height = 1 + t.left.height
         elif t.right is not None and t.left is None:
            t.height = 1 + t.right.height
         elif t.right is not None and t.left is not None:
            t.height = 1 + max(t.left.height, t.right.height)
         return t
            
      elif value is t.value:
         if t.left is None and t.right is None:
            t = None
         elif t.left is not None and t.right is not None:
            t.value = self.find_right_min(t)
            t.right = self.rem_rec_elem(t.value, t.right)
            if t.right == None and t.left == None:
               t.height = 1
            elif t.right is not None and t.left is not None:
               t.height = 1 + max(t.left.height, t.right.height)
            elif t.right is None and t.left is not None:
               t.height = 1 + t.left.height
            elif t.right is not None and t.left is None:
               t.height = 1 + t.right.height
            return t
         elif t.left is None and t.right is not None:
            return t.right
         elif t.left is not None and t.right is None:
            return t.left
         
   def find_right_min(self, t):
      last_node = t.right
      while last_node.left is not None:
         last_node = last_node.left
      return last_node.value
        
   def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    #pass # TODO replace pass with your implementation
      if self.__root is None:
         return '[ ]'
      else:
         return "[ " + self.rec_in_order(self.__root)[:-2] + " ]"
    
   def rec_in_order(self, t):
      strings = ""
      if t is not None:
         strings = self.rec_in_order(t.left)
         strings += str(t.value) + ", "
         strings += self.rec_in_order(t.right)
      return strings
   
   def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    #pass # TODO replace pass with your implementation
      if self.__root is None:
         return '[ ]'
      else:
         return "[ " + self.rec_pre_order(self.__root)[:-2] + " ]"
      
   def rec_pre_order(self, t):
      strings = ""
      if t is not None:
         strings = str(t.value) + ", "
         strings += self.rec_pre_order(t.left)
         strings += self.rec_pre_order(t.right)
      return strings
            
   def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
      #pass # TODO replace pass with your implementation
      if self.__root is None:
         return '[ ]'
      else:
         return "[ " + self.rec_post_order(self.__root)[:-2] + " ]"
         
   def rec_post_order(self, t):
      strings = ""
      if t is not None:
         strings = self.rec_post_order(t.left)
         strings += self.rec_post_order(t.right)
         strings += str(t.value) + ", "
      return strings
      
   def breadth_first(self):
      display = "[ "
      q = Queue()
      q.enqueue(self.__root)
      cur_height = self.__root.height
      if self.__root is None:
         return '[ ]'
      while len(q) > 0:
         cur_node = q.dequeue()
         if cur_node.height > cur_height:
            cur_height += 1
         display += str(cur_node.value) + ', '
      
         if cur_node.left:
            cur_node.left.height = cur_height + 1
            q.enqueue(cur_node.left)
         
         if cur_node.right:
            cur_node.right.height = cur_height + 1
            q.enqueue(cur_node.right)
      display = display[:-2] + " ]"
      return display  

   def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
      #pass # TODO replace pass with your implementation
      if self.__root is None:
         return 0
      else:
         return self.__root.height
         
   def __str__(self):
      return self.in_order()

if __name__ == '__main__':
   pass #unit tests make the main section unnecessary.
#   BSTree = Binary_Search_Tree()
#   BSTree.insert_element(70)
#   BSTree.insert_element(60)
#   BSTree.insert_element(50)
#   BSTree.insert_element(55)
#   BSTree.insert_element(65)
#   BSTree.insert_element(30)
#   BSTree.insert_element(20)
#   BSTree.insert_element(25)
#   BSTree.insert_element(10)
#   BSTree.remove_element(50)
#   BSTree.remove_element(30)
#   BSTree.remove_element(60)
#   print(BSTree)
