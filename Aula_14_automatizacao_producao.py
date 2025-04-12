# Passo 1: Criar o repositório e adicionar o projeto Python
# Supondo que o projeto já esteja criado localmente
git init
git remote add origin https://github.com/usuario/projeto-python.git
git add .
git commit -m "Initial commit"
git push -u origin main

# Passo 2: Criar o arquivo de workflow CI/CD
mkdir -p .github/workflows
echo "
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout código
      uses: actions/checkout@v2

    - name: Configurar Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Executar testes unitários
      run: pytest

    - name: Executar testes funcionais com Selenium
      run: python test_selenium.py

    - name: Relatório de Cobertura
      run: |
        pip install coverage
        coverage run -m pytest
        coverage report
        coverage xml

    - name: Deploy para Staging (Opcional)
      env:
        HEROKU_API_KEY: \${{ secrets.HEROKU_API_KEY }}
      run: |
        git remote add heroku https://git.heroku.com/nome-do-app.git
        git push heroku main
" > .github/workflows/ci-cd.yml

# Passo 3: Commit e push do arquivo de workflow
git add .github/workflows/ci-cd.yml
git commit -m "Adicionar pipeline de CI/CD"
git push

# Passo 4: Criação do script de teste funcional com Selenium (test_selenium.py)
echo "
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='path/to/chromedriver')
driver.get('https://example.com')
assert 'Example Domain' in driver.title
elem = driver.find_element_by_xpath('//a[text()=\"More information...\"]')
elem.click()
assert 'IANA' in driver.title
driver.quit()
" > test_selenium.py

# Passo 5: Commit e push do script de teste
git add test_selenium.py
git commit -m "Adicionar teste funcional com Selenium"
git push
