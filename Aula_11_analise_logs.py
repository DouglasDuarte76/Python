import logging

# Passo 1: Configuração básica do logger
logger = logging.getLogger('app_logger')
logger.setLevel(logging.DEBUG)

# Configuração do handler para escrever logs em um arquivo
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Configuração do formato dos logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Adiciona o handler ao logger
logger.addHandler(file_handler)

# Passo 2: Implementação de diferentes níveis de log
def divisao(a, b):
    logger.info(f'Divisão solicitada: {a} / {b}')
    if b == 0:
        logger.error('Tentativa de divisão por zero!')
        raise ValueError('Divisão por zero não permitida.')
    return a / b

# Passo 3: Registro de logs em um arquivo
try:
    resultado = divisao(10, 0)
except Exception as e:
    logger.exception('Erro durante a operação de divisão.')

# Simulação de outros eventos
logger.info('Aplicação iniciada.')
logger.warning('Uso excessivo de memória detectado.')
logger.info('Aplicação finalizada.')

# Passo 4: Análise dos logs gerados
# (Os alunos devem abrir o arquivo app.log e analisar o conteúdo gerado.)
