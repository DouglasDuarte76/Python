# Passo 1: Instalar as ferramentas de análise estática
pip install pylint flake8 mypy

# Passo 2: Executar Pylint no projeto
pylint projeto/

# Passo 3: Executar Flake8 no projeto
flake8 projeto/ --max-complexity 10

# Passo 4: Executar MyPy para verificação de tipos
mypy projeto/

# Exemplo de código a ser analisado
echo "
def adicionar(a, b):
    return a + b

def dividir(a, b):
    return a / b

x = adicionar(1, '2')  # Problema de tipo aqui
print(dividir(4, 0))   # Problema de divisão por zero
" > projeto/main.py

# Após análise, corrigir problemas detectados
echo "
from typing import Union

def adicionar(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def dividir(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if b == 0:
        raise ValueError('Divisão por zero não permitida!')
    return a / b

x = adicionar(1, 2)  # Corrigido para evitar conflito de tipos
print(dividir(4, 2))  # Corrigido para evitar divisão por zero
" > projeto/main.py

# Reexecutar Pylint, Flake8, e MyPy para verificar as melhorias
pylint projeto/
flake8 projeto/
mypy projeto/
