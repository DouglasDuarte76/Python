pip install boto3 azure-mgmt-resource paramiko


import boto3
import paramiko
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential

# Configuração para AWS
aws_session = boto3.Session(
    aws_access_key_id='SEU_ACCESS_KEY_AWS',
    aws_secret_access_key='SEU_SECRET_KEY_AWS',
    region_name='us-east-1'
)
ec2 = aws_session.client('ec2')

# Configuração para Azure
credential = DefaultAzureCredential()
subscription_id = 'SEU_SUBSCRIPTION_ID_AZURE'
resource_client = ResourceManagementClient(credential, subscription_id)

# Função para monitorar servidores on-premises via SSH
def monitorar_servidor_onpremises(hostname, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        stdin, stdout, stderr = client.exec_command('uptime')
        print(f"Uptime do servidor {hostname}: {stdout.read().decode().strip()}")

        # Executar outros comandos para auditoria de conformidade
        stdin, stdout, stderr = client.exec_command('df -h')
        print(f"Uso de disco no servidor {hostname}:\n{stdout.read().decode().strip()}")

        client.close()
    except Exception as e:
        print(f"Erro ao conectar ao servidor on-premises {hostname}: {e}")

# Função para auditar instâncias EC2 na AWS
def auditar_aws():
    print("Iniciando auditoria de conformidade em AWS...")
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instância AWS ID: {instance['InstanceId']}, Estado: {instance['State']['Name']}")
            # Implementar lógica de auditoria para instâncias EC2

# Função para auditar recursos no Azure
def auditar_azure():
    print("Iniciando auditoria de conformidade em Azure...")
    for rg in resource_client.resource_groups.list():
        print(f"Recurso Grupo: {rg.name}")
        # Implementar lógica de auditoria para recursos no Azure

# Executar auditoria em ambientes híbridos
auditar_aws()
auditar_azure()
monitorar_servidor_onpremises('seu.servidor.local', 'username', 'password')
