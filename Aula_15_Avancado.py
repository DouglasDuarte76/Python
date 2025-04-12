pip install hypothesis
_____________________________

# calculadora.py
def soma(a, b):
    return a + b

_____________________________

# test_calculadora.py
import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(10, -5), 5)

if __name__ == "__main__":
    unittest.main()

_____________________________

# test_hypothesis.py
from hypothesis import given, strategies as st
from calculadora import soma

# Garante que soma(a, b) == soma(b, a) (propriedade comutativa)
@given(st.integers(), st.integers())
def test_soma_comutativa(a, b):
    assert soma(a, b) == soma(b, a)

# Garante que soma(a, 0) == a (propriedade do elemento neutro)
@given(st.integers())
def test_soma_elemento_neutro(a):
    assert soma(a, 0) == a

_____________________________

pytest test_hypothesis.py

_____________________________

============================= test session starts ==============================
hypothesis: tests=10000
...
========================= 2 passed in 0.12 seconds =============================

_____________________________

# calculadora.py (modificado)
def divisao(a, b):
    return a / b  # Pode falhar se b == 0

_____________________________

# test_hypothesis.py (modificado)
@given(st.integers(), st.integers().filter(lambda x: x != 0))
def test_divisao(a, b):
    assert divisao(a, b) == a / b

_____________________________

pytest test_hypothesis.py

_____________________________



