pip install boto3

import boto3

# Criar uma sessão na AWS
session = boto3.Session(
    aws_access_key_id='SEU_ACCESS_KEY',
    aws_secret_access_key='SEU_SECRET_KEY',
    region_name='us-east-1'
)

# Conectar ao serviço EC2
ec2 = session.client('ec2')
iam = session.client('iam')

# Função para verificar a conformidade de instâncias EC2
def verificar_instancias_ec2():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instância ID: {instance['InstanceId']}")
            print(f"Estado: {instance['State']['Name']}")
            if instance['State']['Name'] == 'running':
                verificar_grupos_de_seguranca(instance['InstanceId'])

# Função para verificar grupos de segurança
def verificar_grupos_de_seguranca(instance_id):
    response = ec2.describe_security_groups(
        Filters=[{'Name': 'instance-id', 'Values': [instance_id]}]
    )
    for sg in response['SecurityGroups']:
        print(f"  - Grupo de Segurança: {sg['GroupName']}")
        for permission in sg['IpPermissions']:
            if permission['IpProtocol'] == '-1':
                print(f"  - [ALERTA] Permissão de acesso total encontrada para {sg['GroupName']}")
            else:
                print(f"  - Protocolo: {permission['IpProtocol']}, Porta: {permission['FromPort']} - {permission['ToPort']}")

# Função para verificar as políticas IAM
def verificar_politicas_iam():
    response = iam.list_users()
    for user in response['Users']:
        print(f"Usuário IAM: {user['UserName']}")
        attached_policies = iam.list_attached_user_policies(UserName=user['UserName'])
        if not attached_policies['AttachedPolicies']:
            print(f"  - [ALERTA] Usuário sem políticas de segurança atribuídas: {user['UserName']}")

# Executar verificações de conformidade
print("Iniciando auditoria de conformidade...")
verificar_instancias_ec2()
verificar_politicas_iam()
print("Auditoria concluída.")
