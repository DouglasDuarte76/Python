# Passo 1: Instalar Bandit e Safety
pip install bandit safety

# Código de exemplo com possíveis vulnerabilidades
echo "
import os
import sqlite3

def executar_comando_sql(usuario_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM users WHERE name = {usuario_input}')
    return cursor.fetchall()

def executar_comando_sistema(comando):
    os.system(comando)

usuario_input = 'admin'
comando = 'ls -la'

executar_comando_sql(usuario_input)
executar_comando_sistema(comando)
" > app.py

# Passo 2: Executar Bandit para verificar vulnerabilidades no código
bandit -r .

# Passo 3: Executar Safety para verificar vulnerabilidades nas dependências
# (Assumindo que há um arquivo requirements.txt no projeto)
echo "
requests==2.19.1
Django==2.0.0
" > requirements.txt
safety check -r requirements.txt

# Passo 4: Análise dos resultados
# Verificar os resultados gerados pelo Bandit e Safety, que devem indicar vulnerabilidades.

# Passo 5: Correção das vulnerabilidades
# Correções sugeridas para o código de exemplo:
echo "
import os
import sqlite3

def executar_comando_sql_seguro(usuario_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (usuario_input,))
    return cursor.fetchall()

def executar_comando_sistema_seguro(comando):
    if comando in ['ls', 'pwd']:  # Validação de comando
        os.system(comando)
    else:
        print('Comando não permitido')

usuario_input = 'admin'
comando = 'ls'

executar_comando_sql_seguro(usuario_input)
executar_comando_sistema_seguro(comando)
" > app.py

# Reexecutar Bandit para garantir que as correções eliminaram as vulnerabilidades
bandit -r .
