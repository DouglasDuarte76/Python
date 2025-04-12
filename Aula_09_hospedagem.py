# Passo 1: Criar o repositório e adicionar o projeto Python
# Supondo que o projeto já esteja criado localmente
git init
git remote add origin https://github.com/usuario/projeto-python.git
git add .
git commit -m "Initial commit"
git push -u origin main

# Passo 2: Criar o arquivo de workflow de CI/CD
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

    - name: Rodar Pylint
      run: |
        pip install pylint
        pylint projeto/

    - name: Rodar testes unitários
      run: |
        pip install pytest
        pytest

    - name: Relatório de Cobertura
      run: |
        pip install coverage
        coverage run -m pytest
        coverage report
        coverage xml
" > .github/workflows/ci-cd.yml

# Passo 3: Commit e push do arquivo de workflow
git add .github/workflows/ci-cd.yml
git commit -m "Adicionar pipeline de CI/CD"
git push

# Passo 4: (Opcional) Configurar deploy automatizado em Heroku
echo "
    - name: Deploy para Heroku
      env:
        HEROKU_API_KEY: \${{ secrets.HEROKU_API_KEY }}
      run: |
        git remote add heroku https://git.heroku.com/nome-do-app.git
        git push heroku main
" >> .github/workflows/ci-cd.yml
