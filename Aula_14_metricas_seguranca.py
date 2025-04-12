pip install boto3

import boto3
import time

# Criar uma sessão na AWS
session = boto3.Session(
    aws_access_key_id='SEU_ACCESS_KEY',
    aws_secret_access_key='SEU_SECRET_KEY',
    region_name='us-east-1'
)

# Conectar ao serviço CloudWatch
cloudwatch = session.client('cloudwatch')

# Função para monitorar falhas de login
def monitorar_falhas_login():
    while True:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='FailedLoginAttempts',
            Dimensions=[
                {'Name': 'InstanceId', 'Value': 'SEU_INSTANCE_ID'}
            ],
            StartTime=time.time() - 300,  # Últimos 5 minutos
            EndTime=time.time(),
            Period=60,
            Statistics=['Sum']
        )
        
        for datapoint in response['Datapoints']:
            if datapoint['Sum'] > 5:
                print(f"[ALERTA] Múltiplas falhas de login detectadas! ({datapoint['Sum']} tentativas)")

        time.sleep(300)  # Repetir a cada 5 minutos

# Executar o monitoramento contínuo
monitorar_falhas_login()
