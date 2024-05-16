import unittest
from Myclass import Myclass

class Testclass(unittest.TestCase):

    def test_add(self):
        calc = Myclass(5 ,3)
        self.assertEqual(calc.add(),8)


    def test_subtract(self):
        calc = Myclass(5 ,3)
        self.assertEqual(calc.subtract(),8)
