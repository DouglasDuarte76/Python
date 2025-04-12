pip install boto3


import boto3

# Criar uma sessão na AWS
session = boto3.Session(
    aws_access_key_id='SEU_ACESS_KEY',
    aws_secret_access_key='SEU_SECRET_KEY',
    region_name='us-east-1'  # Altere para a região apropriada
)

# Conectar ao serviço EC2
ec2 = session.client('ec2')

# Função para listar instâncias EC2 e seus grupos de segurança
def listar_instancias_ec2():
    response = ec2.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instância ID: {instance['InstanceId']}")
            print(f"Estado: {instance['State']['Name']}")
            print(f"Tipo de Instância: {instance['InstanceType']}")
            print("Grupos de Segurança:")
            for sg in instance['SecurityGroups']:
                print(f"  - Nome: {sg['GroupName']}, ID: {sg['GroupId']}")
                verificar_regras_segurança(sg['GroupId'])

# Função para verificar as regras de segurança de um grupo
def verificar_regras_segurança(group_id):
    response = ec2.describe_security_groups(GroupIds=[group_id])
    
    for sg in response['SecurityGroups']:
        for rule in sg['IpPermissions']:
            print(f"    - Protocolo: {rule.get('IpProtocol', 'N/A')}")
            print(f"    - Portas: {rule.get('FromPort', 'N/A')} - {rule.get('ToPort', 'N/A')}")
            for ip_range in rule.get('IpRanges', []):
                print(f"    - IPs Permitidos: {ip_range['CidrIp']}")
            print()

# Executar a função de listagem e verificação
listar_instancias_ec2()
