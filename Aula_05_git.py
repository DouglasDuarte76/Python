# Inicializar o repositório Git
git init

# Criar a estrutura inicial do projeto Python
mkdir projeto
cd projeto
touch main.py

# Criar uma branch para nova funcionalidade
git branch calcular_fatorial
git checkout calcular_fatorial

# Implementar a função e testes em Python
echo "
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)
" > main.py

echo "
import unittest
from main import fatorial

class TestFatorial(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(0), 1)

if __name__ == '__main__':
    unittest.main()
" > test_main.py

# Configurar um Git Hook para rodar os testes antes de cada commit
echo "

#!/bin/bash
python3 -m unittest test_main.py
" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Adicionar e commitar as mudanças
git add .
git commit -m "Adicionar função de cálculo de fatorial e testes"

# Mesclar a branch com a branch principal
git checkout main
git merge calcular_fatorial
