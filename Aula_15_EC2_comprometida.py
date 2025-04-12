pip install boto3

import boto3

# Criar uma sessão na AWS
session = boto3.Session(
    aws_access_key_id='SEU_ACCESS_KEY',
    aws_secret_access_key='SEU_SECRET_KEY',
    region_name='us-east-1'
)

# Conectar ao serviço Lambda e EC2
lambda_client = session.client('lambda')
ec2 = session.client('ec2')

# Código Python para a função Lambda
lambda_code = '''
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = event['detail']['instance-id']
    
    # Isolar a instância comprometida removendo-a de grupos de segurança críticos
    ec2.modify_instance_attribute(InstanceId=instance_id, Groups=[])
    print(f"Instância {instance_id} foi isolada.")
    return "Instância isolada com sucesso."
'''

# Criar a função Lambda
def criar_funcao_lambda():
    response = lambda_client.create_function(
        FunctionName='IsolarInstanciaComprometida',
        Runtime='python3.8',
        Role='SEU_ROLE_ARN',
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': bytes(lambda_code, 'utf-8')},
        Description='Função Lambda para isolar instâncias EC2 comprometidas.',
        Timeout=10,
        MemorySize=128,
        Publish=True,
    )
    print(f"Função Lambda '{response['FunctionName']}' criada com sucesso.")

# Executar a criação da função Lambda
criar_funcao_lambda()
