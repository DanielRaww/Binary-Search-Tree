import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
   
   def setUp(self):
      self.__BSTree = Binary_Search_Tree()
      
   def test_blank_tree(self):
      self.assertEqual('[ ]', str(self.__BSTree))
   
   def test_get_height_empty_tree(self):
      self.assertEqual(0, self.__BSTree.get_height())
      
   def test_get_height_one_element(self):
      self.__BSTree.insert_element(12)
      self.assertEqual(1, self.__BSTree.get_height())
      
   def test_remove_from_blank(self):
      with self.assertRaises(ValueError):
         self.__BSTree.remove_element(13)
         self.assertEqual('[ ]', str(self.__BSTree))
         self.assertEqual('[ ]', self.__BSTree.post_order())
         self.assertEqual('[ ]', self.__BSTree.pre_order())
         self.assertEqual(0, self.__BSTree.get_height())
         
   def test_insert_one_element(self):
      self.__BSTree.insert_element(0)
      self.assertEqual('[ 0 ]', str(self.__BSTree))
      
   def test_insert_two_elements(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.assertEqual('[ 1, 2 ]', str(self.__BSTree))
      self.assertEqual('[ 2, 1 ]', self.__BSTree.post_order())
      self.assertEqual('[ 1, 2 ]', self.__BSTree.pre_order())
      
   def test_remove_root_element(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.__BSTree.remove_element(2)
      self.assertEqual('[ 1 ]', str(self.__BSTree))
      
   def test_remove_root_element_test_2(self):
      self.__BSTree.insert_element(11)
      self.__BSTree.remove_element(11)
      self.assertEqual("[ ]", self.__BSTree.in_order())
      
   def test_remove_child_element_change_height(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.assertEqual(2, self.__BSTree.get_height())
      self.__BSTree.remove_element(2)
      self.assertEqual(1, self.__BSTree.get_height())
      
   def test_insert_child_element_same_height(self):
      self.__BSTree.insert_element(6)
      self.__BSTree.insert_element(5)
      self.__BSTree.insert_element(2)
      self.assertEqual(3, self.__BSTree.get_height())
      self.__BSTree.insert_element(8)
      self.assertEqual(3, self.__BSTree.get_height())
      
   def test_insert_two_elements(self):
      self.__BSTree.insert_element(5)
      self.__BSTree.insert_element(-2)
      self.assertEqual('[ -2, 5 ]', str(self.__BSTree))
      self.assertEqual('[ 5, -2 ]', self.__BSTree.pre_order())
      self.assertEqual('[ -2, 5 ]', self.__BSTree.post_order())
      
   def test_insert_same_val_two_elements(self):
      with self.assertRaises(ValueError):
         self.__BSTree.insert_element(4)
         self.__BSTree.insert_element(4)
      self.assertEqual('[ 4 ]', str(self.__BSTree))
      self.assertEqual('[ 4 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 4 ]', self.__BSTree.post_order())
      self.assertEqual(1, self.__BSTree.get_height())
      
   def test_insert_three_elements(self):
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.assertEqual('[ 0, 1, 2 ]', str(self.__BSTree))
      self.assertEqual('[ 0, 1, 2 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 2, 1, 0 ]', self.__BSTree.post_order())
            
   def test_remove_child_element_change_height(self):
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.assertEqual(3, self.__BSTree.get_height())
      self.__BSTree.remove_element(2)
      self.assertEqual(2, self.__BSTree.get_height())
      
   def test_remove_child_element_no_change_height(self):
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(4)
      self.assertEqual(2, self.__BSTree.get_height())
      self.__BSTree.remove_element(3)
      self.assertEqual(2, self.__BSTree.get_height())
      
   def test_remove_child_element_no_change_height_test_2(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(2)
      self.assertEqual(2, self.__BSTree.get_height())
      self.__BSTree.remove_element(0)
      self.assertEqual(2, self.__BSTree.get_height())
      
   def test_insert_four_elements(self):
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(3)
      self.assertEqual('[ 0, 1, 2, 3 ]', str(self.__BSTree))
      self.assertEqual('[ 0, 1, 2, 3 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 3, 2, 1, 0 ]', self.__BSTree.post_order())
      
   def test_four_remove_child_elment_change_height_test_2(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(4)
      self.assertEqual(4, self.__BSTree.get_height())
      self.__BSTree.remove_element(4)
      self.assertEqual(3, self.__BSTree.get_height())
      
   def test_insert_five_elements(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(5)
      self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__BSTree))
      self.assertEqual('[ 1, 2, 3, 4, 5 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 5, 4, 3, 2, 1 ]', self.__BSTree.post_order())
      
   def test_insert_five_elements(self):
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(4)
      self.assertEqual('[ 0, 1, 2, 3, 4 ]', str(self.__BSTree))
      self.assertEqual('[ 0, 1, 2, 3, 4 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 4, 3, 2, 1, 0 ]', self.__BSTree.post_order())
            
   def test_insert_six_elements(self):
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(5)
      self.assertEqual('[ 0, 1, 2, 3, 4, 5 ]', str(self.__BSTree))
      self.assertEqual('[ 0, 1, 2, 3, 4, 5 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 5, 4, 3, 2, 1, 0 ]', self.__BSTree.post_order())
            
   def test_random_insert_six_elements(self):
      self.__BSTree.insert_element(10)
      self.__BSTree.insert_element(7)
      self.__BSTree.insert_element(15)
      self.__BSTree.insert_element(8)
      self.__BSTree.insert_element(9)
      self.__BSTree.insert_element(12)
      self.assertEqual('[ 7, 8, 9, 10, 12, 15 ]', str(self.__BSTree))
      self.assertEqual('[ 10, 7, 8, 9, 15, 12 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 9, 8, 7, 12, 15, 10 ]', self.__BSTree.post_order())
      
   def test_insert_same_val_six_elements(self):
      with self.assertRaises(ValueError):
         self.__BSTree.insert_element(3)
         self.__BSTree.insert_element(7)
         self.__BSTree.insert_element(-4)
         self.__BSTree.insert_element(5)
         self.__BSTree.insert_element(9)
         self.__BSTree.insert_element(3)
         self.assertEqual('[ -4, 3, 5, 7, 9 ]', str(self.__BSTree))
         self.assertEqual('[ 3, -4, 7, 5, 9 ]', self.__BSTree.pre_order())
         self.assertEqual('[ -4, 5, 9, 7, 3 ]', self.__BSTree.post_order())
         
   def test_remove_root_six_elements(self):
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(-1)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(5)
      self.__BSTree.remove_element(2)
      self.assertEqual('[ -1, 0, 1, 3, 4, 5 ]', str(self.__BSTree))
      self.assertEqual('[ 3, 0, -1, 1, 4, 5 ]', self.__BSTree.pre_order())
      self.assertEqual('[ -1, 1, 0, 5, 4, 3 ]', self.__BSTree.post_order())
            
   def test_remove_right_child_six_elements(self):
      self.__BSTree.insert_element(7)
      self.__BSTree.insert_element(5)
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(6)
      self.__BSTree.insert_element(9)
      self.__BSTree.insert_element(8)
      self.__BSTree.insert_element(10)
      self.__BSTree.remove_element(9)
      self.assertEqual('[ 4, 5, 6, 7, 8, 10 ]', str(self.__BSTree))
      self.assertEqual('[ 7, 5, 4, 6, 10, 8 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 4, 6, 5, 8, 10, 7 ]', self.__BSTree.post_order())
      
   def test_remove_left_child_six_elements(self):
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(5)
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(6)
      self.__BSTree.remove_element(1)
      self.assertEqual('[ 0, 2, 3, 4, 5, 6 ]', str(self.__BSTree))
      self.assertEqual('[ 3, 2, 0, 5, 4, 6 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 0, 2, 4, 6, 5, 3 ]', self.__BSTree.post_order())
      
   def test_remove_child_element_height(self):
      self.__BSTree.insert_element(8)
      self.__BSTree.insert_element(6)
      self.__BSTree.insert_element(5)
      self.__BSTree.insert_element(7)
      self.__BSTree.insert_element(10)
      self.__BSTree.insert_element(9)
      self.__BSTree.insert_element(11)
      self.assertEqual(3, self.__BSTree.get_height())
      self.__BSTree.remove_element(5)
      self.assertEqual(3, self.__BSTree.get_height())
      self.__BSTree.remove_element(7)
      self.assertEqual(3, self.__BSTree.get_height())
      self.__BSTree.remove_element(9)
      self.assertEqual(3, self.__BSTree.get_height())
      self.__BSTree.remove_element(11)
      self.assertEqual(2, self.__BSTree.get_height())
   
   def test_insert_child_element_same_height_test_2(self):
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(6)
      self.__BSTree.insert_element(8)
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(1)
      self.assertEqual(4, self.__BSTree.get_height())
      self.__BSTree.insert_element(5)
      self.assertEqual(4, self.__BSTree.get_height())
      
   def test_remove_two_insert_elements(self):
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(-1)
      self.__BSTree.remove_element(-1)
      self.__BSTree.remove_element(1)
      self.assertEqual('[ ]', str(self.__BSTree))
      
   def test_remove_two_insert_elements_test_2(self):
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(1)
      self.__BSTree.remove_element(1)
      self.__BSTree.remove_element(3)
      self.assertEqual(0, self.__BSTree.get_height())
      
   def test_remove_unknown_element(self):
      with self.assertRaises(ValueError):
         self.__BSTree.insert_element(7)
         self.__BSTree.remove_element(11)
      self.assertEqual('[ 7 ]', str(self.__BSTree))
      self.assertEqual('[ 7 ]', self.__BSTree.pre_order())
      self.assertEqual('[ 7 ]', self.__BSTree.post_order())
      self.assertEqual(1, self.__BSTree.get_height())
      
   def test_breadth_first_two_levels(self):
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(3)
      self.assertEqual('[ 2, 1, 3 ]', self.__BSTree.breadth_first())
      
   def test_breadth_first_three_levels(self):
      self.__BSTree.insert_element(2)
      self.__BSTree.insert_element(0)
      self.__BSTree.insert_element(-1)
      self.__BSTree.insert_element(1)
      self.__BSTree.insert_element(4)
      self.__BSTree.insert_element(3)
      self.__BSTree.insert_element(5)
      self.assertEqual('[ 2, 0, 4, -1, 1, 3, 5 ]', self.__BSTree.breadth_first())
      self.assertEqual(3, self.__BSTree.get_height())
      
if __name__ == '__main__':
   unittest.main()