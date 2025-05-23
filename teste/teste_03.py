import unittest

class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    
    def multiplicar(self, a, b):
        return a * b

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 3), 2)
        self.assertEqual(self.calc.subtrair(-1, -1), 0)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(0, 100), 0)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

# Para executar no Colab precisamos usar um método diferente
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
