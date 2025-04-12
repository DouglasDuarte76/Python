# Passo 1: Instalar radon, coverage.py e pylint
pip install radon coverage pylint

# Código de exemplo para análise
echo "
def calcular_fatorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def calcular_soma_serie(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            soma -= i
        else:
            soma += i
    return soma
" > exemplo.py

# Passo 2: Calcular a complexidade ciclomática com radon
radon cc exemplo.py -a

# Passo 3: Medir a cobertura de testes com coverage.py
# (Assumindo que há testes unitários definidos em test_exemplo.py)
echo "
import unittest
from exemplo import calcular_fatorial, calcular_soma_serie

class TestExemplo(unittest.TestCase):
    def test_calcular_fatorial(self):
        self.assertEqual(calcular_fatorial(5), 120)
        self.assertEqual(calcular_fatorial(0), 1)
        self.assertEqual(calcular_fatorial(-1), None)

    def test_calcular_soma_serie(self):
        self.assertEqual(calcular_soma_serie(5), 3)
        self.assertEqual(calcular_soma_serie(6), -3)

if __name__ == '__main__':
    unittest.main()
" > test_exemplo.py

coverage run -m unittest discover
coverage report -m

# Passo 4: Analisar a qualidade do código com pylint
pylint exemplo.py

# Passo 5: Interpretação dos resultados e sugestão de melhorias
# (Os alunos devem interpretar os resultados das ferramentas e sugerir melhorias para reduzir a complexidade, aumentar a cobertura de testes e melhorar a qualidade geral do código)
