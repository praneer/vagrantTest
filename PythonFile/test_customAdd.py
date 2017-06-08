import unittest
from CustomAdd import MyAdd
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):        		
		self.assertEqual( MyAdd.doAdd(3, 4), 7)
 
    def test_strings_a_3(self):
        self.assertEqual( MyAdd.doAdd(3, 3), 6)	
 
if __name__ == '__main__':
    unittest.main()
