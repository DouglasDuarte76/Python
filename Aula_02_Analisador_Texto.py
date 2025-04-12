texto = input("Digite um texto para análise: ")

import string

texto = texto.lower()
for punct in string.punctuation:
    texto = texto.replace(punct, "")

palavras = texto.split()
frequencia_palavras = {}

for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

frequencia_ordenada = sorted(frequencia_palavras.items(), key=lambda item: item[1], reverse=True)

print("\nFrequência das palavras:")
for palavra, frequencia in frequencia_ordenada:
    print(f"{palavra}: {frequencia}")

    
import matplotlib.pyplot as plt

palavras = [item[0] for item in frequencia_ordenada[:10]]
frequencias = [item[1] for item in frequencia_ordenada[:10]]

plt.figure(figsize=(10, 6))
plt.bar(palavras, frequencias, color='blue')
plt.xlabel('Palavras')
plt.ylabel('Frequência')
plt.title('Palavras mais comuns')
plt.show()

