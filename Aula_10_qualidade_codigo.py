# Passo 1: Configurar o repositório e criar uma branch
git checkout -b nova_funcionalidade

# Passo 2: Implementar a funcionalidade (exemplo: função que calcula a média)
echo "
def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
" > projeto.py
git add projeto.py
git commit -m "Adicionar função para calcular média"

# Passo 3: Criar um Pull Request no GitHub
git push origin nova_funcionalidade

# Passo 4: Revisão do Pull Request pelo colega
# O revisor acessa o Pull Request no GitHub, comenta e sugere mudanças

# Passo 5: Implementar as correções sugeridas e fazer novo commit
echo "
def calcular_media(numeros):
    if not numeros:  # Verificar lista vazia
        return 0
    return sum(numeros) / len(numeros)

# Teste simples da função
if __name__ == '__main__':
    print(calcular_media([1, 2, 3, 4]))  # Deve imprimir 2.5
" > projeto.py
git add projeto.py
git commit -m "Corrigir verificação de lista vazia e adicionar teste"
git push origin nova_funcionalidade

# Passo 6: Aprovação do Pull Request após revisão final
# O revisor aprova o Pull Request e ele é integrado à branch principal
