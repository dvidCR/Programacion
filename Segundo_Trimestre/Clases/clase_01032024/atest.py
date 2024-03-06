import unittest
from function import *

class TestFunction(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(incrementar(3), 4)
        
    def test_decrement(self):
        return self.assertEqual(decrementar(4) , 1)
        
if __name__ == '__main__':
    print(TestFunction())