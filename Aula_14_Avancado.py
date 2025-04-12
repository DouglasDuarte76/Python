pip install pandas numpy scikit-learn seaborn matplotlib

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Criando um dataset simulado para tráfego de rede 6G
np.random.seed(42)
num_samples = 1000

# Características da rede 6G
dados = pd.DataFrame({
    "latencia_ms": np.random.normal(0.1, 0.05, num_samples),  # Latência média de 0.1 ms
    "largura_banda_Gbps": np.random.normal(10, 2, num_samples),  # Banda larga média de 10 Gbps
    "pacotes_malformados": np.random.randint(0, 10, num_samples),  # Número de pacotes corrompidos
    "tentativas_conexao": np.random.randint(1, 50, num_samples),  # Número de tentativas de conexão
    "taxa_erro_pacotes": np.random.uniform(0, 0.02, num_samples),  # Taxa de erro na transmissão
})

# Criando a coluna "ataque_detectado" (1 = ataque, 0 = tráfego normal)
dados["ataque_detectado"] = np.where(
    (dados["pacotes_malformados"] > 6) | 
    (dados["tentativas_conexao"] > 30) | 
    (dados["taxa_erro_pacotes"] > 0.015), 1, 0
)

# Exibir amostra dos dados
print(dados.head())

# Visualização dos ataques
sns.pairplot(dados, hue="ataque_detectado")
plt.show()

________________________________________________________________________________________

# Separar dados em recursos (X) e rótulos (y)
X = dados.drop(columns=['ataque_detectado'])
y = dados['ataque_detectado']

# Dividir dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Importância das features
importances = modelo.feature_importances_
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# Plotar as features mais importantes
plt.figure(figsize=(10, 5))
sns.barplot(x='Importance', y='Feature', data=feature_importance[:5])
plt.title("Importância das Features na Detecção de Ataques em Redes 6G")
plt.show()
