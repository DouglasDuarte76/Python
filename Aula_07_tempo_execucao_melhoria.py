# Passo 1: Instalar coverage.py
pip install coverage

# Passo 2: Rodar os testes com cobertura
coverage run -m pytest

# Passo 3: Gerar e visualizar o relatório de cobertura
coverage report
coverage html  # Gera um relatório em HTML para visualização

# Passo 4: Analisar o relatório gerado em htmlcov/index.html

# Passo 5: Adicionar testes para aumentar a cobertura (exemplo)
echo "
import unittest
from main import soma, subtrair, multiplicar, dividir

class TestOperacoesMatematicas(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

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
" > test_operacoes.py

# Reexecutar os testes e medir novamente a cobertura
coverage run -m unittest discover
coverage report
coverage html
