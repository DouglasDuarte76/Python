pip install radon pylint coverage

____________________________________

# calculadora.py
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

____________________________________

# test_calculadora.py
import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 4), 12)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)
        self.assertEqual(divisao(10, 0), "Erro: Divisão por zero")

if __name__ == "__main__":
    unittest.main()

____________________________________

radon cc calculadora.py -a

____________________________________


calculadora.py - A (4)
    4:0 soma - 1
    7:0 subtracao - 1
    10:0 multiplicacao - 1
    13:0 divisao - 2

____________________________________

pylint calculadora.py

____________________________________

Your code has been rated at 8.75/10

____________________________________

coverage run -m unittest discover
coverage report -m

____________________________________

Name             Stmts   Miss  Cover
------------------------------------
calculadora.py      10      0    100%

____________________________________

# calculadora.py (refatorado)
def divisao(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero")
    return a / b
