pip install boto3 azure-mgmt-resource


import boto3
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential

# Configuração para AWS
aws_session = boto3.Session(
    aws_access_key_id='SEU_ACCESS_KEY_AWS',
    aws_secret_access_key='SEU_SECRET_KEY_AWS',
    region_name='us-east-1'
)
ec2 = aws_session.client('ec2')
iam = aws_session.client('iam')

# Configuração para Azure
credential = DefaultAzureCredential()
subscription_id = 'SEU_SUBSCRIPTION_ID_AZURE'
resource_client = ResourceManagementClient(credential, subscription_id)

# Função para auditoria de conformidade em AWS
def auditar_aws():
    print("Iniciando auditoria de conformidade em AWS...")
    # Verificar permissões de IAM
    usuarios = iam.list_users()
    for user in usuarios['Users']:
        print(f"Usuário IAM: {user['UserName']}")
        attached_policies = iam.list_attached_user_policies(UserName=user['UserName'])
        if not attached_policies['AttachedPolicies']:
            print(f"  - [ALERTA] Usuário sem políticas de segurança atribuídas: {user['UserName']}")

    # Verificar configurações de segurança das instâncias EC2
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instância AWS ID: {instance['InstanceId']}, Estado: {instance['State']['Name']}")
            # Implementar lógica de auditoria para instâncias EC2

# Função para auditoria de conformidade em Azure
def auditar_azure():
    print("Iniciando auditoria de conformidade em Azure...")
    for rg in resource_client.resource_groups.list():
        print(f"Recurso Grupo: {rg.name}")
        # Implementar lógica de auditoria para recursos no Azure

# Executar auditorias de conformidade
auditar_aws()
auditar_azure()
