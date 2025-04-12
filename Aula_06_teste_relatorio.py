# Instalação das ferramentas
pip install pylint coverage

# Passo 1: Configurar e rodar Pylint para verificação de qualidade
pylint projeto/ --output-format=colorized

# Passo 2: Rodar testes unitários (utilizando pytest como exemplo)
pytest

# Passo 3: Medir a cobertura de código com coverage.py
coverage run -m pytest
coverage report
coverage html  # Gera um relatório em HTML para visualização

# Passo 4: Criar um script de automação
echo "
#!/bin/bash
echo 'Executando Pylint...'
pylint projeto/ --output-format=colorized
echo 'Executando testes...'
pytest
echo 'Medindo cobertura de código...'
coverage run -m pytest
coverage report
coverage html
echo 'QA automatizado completo. Relatório gerado em htmlcov/index.html'
" > executar_qa.sh
chmod +x executar_qa.sh
./executar_qa.sh
