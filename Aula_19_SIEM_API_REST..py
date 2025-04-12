pip install boto3 azure-mgmt-resource paramiko requests


import boto3
import paramiko
import requests
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

# Função para coletar logs de servidores on-premises via SSH
def coletar_logs_onpremises(hostname, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        stdin, stdout, stderr = client.exec_command('cat /var/log/auth.log')
        logs = stdout.read().decode()
        enviar_logs_siem(logs)
        client.close()
    except Exception as e:
        print(f"Erro ao conectar ao servidor on-premises {hostname}: {e}")

# Função para coletar logs de instâncias EC2 na AWS
def coletar_logs_aws():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Coletando logs da instância AWS ID: {instance['InstanceId']}")
            # Simular coleta de logs e envio para SIEM
            logs = f"Logs da instância {instance['InstanceId']}"
            enviar_logs_siem(logs)

# Função para coletar logs de recursos no Azure
def coletar_logs_azure():
    for rg in resource_client.resource_groups.list():
        print(f"Coletando logs do grupo de recursos {rg.name}")
        # Simular coleta de logs e envio para SIEM
        logs = f"Logs do grupo de recursos {rg.name}"
        enviar_logs_siem(logs)

# Função para enviar logs para um SIEM (simulação de API REST)
def enviar_logs_siem(logs):
    try:
        siem_url = "https://seu-siem-endpoint/api/logs"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(siem_url, headers=headers, data=logs)
        if response.status_code == 200:
            print("Logs enviados com sucesso para o SIEM.")
        else:
            print(f"Falha ao enviar logs para o SIEM: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar logs para o SIEM: {e}")

# Executar coleta de logs e envio para SIEM
coletar_logs_onpremises('seu.servidor.local', 'username', 'password')
coletar_logs_aws()
coletar_logs_azure()
