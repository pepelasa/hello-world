import unittest
import math

class Test_Lab31(unittest.TestCase):

    #Right
    def test_integer(self):
        self.assertEqual(math.ceil(5/1), 5)
    #Boundaries
    def test_low_boundary(self):
        self.assertEqual(math.ceil(5.000000000000001), 6)
    #Boundaries
    def test_high_boundary(self):
        self.assertEqual(math.ceil(5.999999999999999), 6)

    #Inverse relationships

    #Cross-check results by other means
    
    #Errors forced to happen
    def test_high_boundary(self):
        with self.assertRaises(TypeError): math.ceil("5")
    #Performance
    


if __name__ == '__main__':
    unittest.main()