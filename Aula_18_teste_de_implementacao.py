# Passo 1: Escrever o primeiro teste que falha
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

# Inicialmente, ao rodar isso, vai falhar porque a função fibonacci ainda não foi implementada
# Para rodar o teste: python3 -m unittest test_fibonacci.py

# Passo 2: Implementar o código mínimo necessário para passar no primeiro teste
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

# Agora o teste deve passar

# Passo 3: Escrever mais testes e implementar a funcionalidade correspondente
class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3)

# Implementação para passar nos novos testes
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Passo 4: Refatorar o código se necessário
# Neste caso, a função está correta e simples, mas podemos usar um approach iterativo para melhorar a performance.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Passo 5: Executar todos os testes novamente para garantir que a refatoração não quebrou nada
if __name__ == "__main__":
    unittest.main()
