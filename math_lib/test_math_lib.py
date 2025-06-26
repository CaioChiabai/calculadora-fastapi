"""
Testes para a biblioteca math_lib

Este arquivo contém todos os testes unitários para a biblioteca math_lib,
incluindo apenas as operações básicas: soma, subtração, multiplicação e divisão.
"""

import unittest
from math_lib.operations import add, subtract, multiply, divide


class TestBasicOperations(unittest.TestCase):
    """Testes para operações básicas"""
    
    def test_add(self):
        """Testa a função de adição"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, -50), 50)
    
    def test_subtract(self):
        """Testa a função de subtração"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(-10, 5), -15)
    
    def test_multiply(self):
        """Testa a função de multiplicação"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0.5, 4), 2)
        self.assertEqual(multiply(-5, -4), 20)
        self.assertEqual(multiply(1, 100), 100)
    
    def test_divide(self):
        """Testa a função de divisão"""
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3.0)
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(10, -2), -5.0)
        
        # Teste de divisão por zero
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertIn("Divisão por zero não é permitida", str(context.exception))


if __name__ == '__main__':
    # Executa todos os testes
    unittest.main(verbosity=2)
