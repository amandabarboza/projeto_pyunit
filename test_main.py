import unittest
from dataclasses import is_dataclass
from main import Product

class TestProduct(unittest.TestCase):
    
    def test_if_it_is_a_dataclass(self):
        # verifica a classe Product
        self.assertTrue(is_dataclass(Product))
        
    def setUp(self):
        self.product = Product(1, 'Teste', 2.0, 20)
    
    def test_constructor(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, 'Teste')
        self.assertEqual(self.product.price, 2.0)
        self.assertEqual(self.product.stock, 20)
        
    def test_increase_stock(self):
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock, 30)
        
    def test_decrease_stock(self):
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock, 10)


if __name__ == '__main__':
    unittest.main()