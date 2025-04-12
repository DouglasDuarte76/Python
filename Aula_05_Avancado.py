pip install mutmut

# calculadora.py
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

___________________________________

# test_calculadora.py
import unittest
from calculadora import soma, subtracao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(10, 4), 6)

if __name__ == "__main__":
    unittest.main()

___________________________________

mutmut run

___________________________________

mutmut results

___________________________________

# test_calculadora.py (versão aprimorada)
import unittest
from calculadora import soma, subtracao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(100, 200), 300)  # Novo caso
        self.assertEqual(soma(0, 0), 0)  # Novo caso

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(10, 4), 6)
        self.assertEqual(subtracao(-2, -3), 1)  # Novo caso
        self.assertEqual(subtracao(0, 5), -5)  # Novo caso

if __name__ == "__main__":
    unittest.main()

___________________________________

mutmut run
mutmut results

___________________________________

