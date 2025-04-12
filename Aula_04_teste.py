# Código da aplicação fornecida
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida!")
    return a / b

# Testes unitários com unittest
import unittest

class TestOperacoesMatematicas(unittest.TestCase):
    def test_adicionar(self):
        self.assertEqual(adicionar(1, 2), 3)
        self.assertEqual(adicionar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(2, 1), 1)
        self.assertEqual(subtrair(0, 5), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 3), 9)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
