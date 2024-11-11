import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(4), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(44), 150)

    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(84), 100)

    def test_Invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid Input")
    
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()