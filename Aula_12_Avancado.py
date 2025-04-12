pip install pandas scikit-learn seaborn matplotlib


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar dataset (substituir pelo caminho do arquivo real)
url = "https://raw.githubusercontent.com/aliifam/cybersecurity-datasets/main/network_intrusion.csv"
df = pd.read_csv(url)

# Exibir as primeiras linhas do dataset
print(df.head())

# Remover colunas não necessárias
df.drop(columns=['Timestamp', 'Source IP', 'Destination IP'], inplace=True)

# Converter colunas categóricas em numéricas
df = pd.get_dummies(df)

# Separar recursos (X) e rótulos (y)
X = df.drop(columns=['Label'])
y = df['Label']

# Dividir dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Exibir o número de amostras em cada classe
print(y.value_counts())

______________________________________________________________________________________

# Criar e treinar o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Exibir importância das features
importances = modelo.feature_importances_
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# Plotar as features mais importantes
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance[:10])
plt.title("Importância das Features na Detecção de Intrusões")
plt.show()
