Vulnerabilidade: Injeção de SQL
Impacto: Alto
Recomendação: Usar prepared statements para prevenir injeções de SQL.

Vulnerabilidade: Falha de autenticação
Impacto: Médio
Recomendação: Implementar autenticação multifatorial.

Vulnerabilidade: Exposição de dados sensíveis
Impacto: Alto
Recomendação: Criptografar dados sensíveis em trânsito e em repouso.

Vulnerabilidade: Senhas fracas
Impacto: Baixo
Recomendação: Exigir uma política de senhas fortes.

___________

from datetime import datetime

# Função para gerar o relatório de auditoria
def gerar_relatorio_auditoria(arquivo_dados):
    # Leitura dos dados de vulnerabilidades
    with open(arquivo_dados, 'r') as f:
        vulnerabilidades = f.readlines()

    # Cabeçalho do relatório
    relatorio = []
    relatorio.append("Relatório de Auditoria de Segurança\n")
    relatorio.append(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    relatorio.append("=" * 50 + "\n")
    
    # Introdução
    relatorio.append("Introdução\n")
    relatorio.append("Esta auditoria teve como objetivo identificar vulnerabilidades de segurança no sistema e propor recomendações para mitigar riscos.\n\n")

    # Resultados
    relatorio.append("Resultados da Auditoria\n")
    relatorio.append("A seguir estão as vulnerabilidades identificadas durante a auditoria:\n")
    
    for linha in vulnerabilidades:
        relatorio.append(linha)

    # Conclusão
    relatorio.append("\nConclusão\n")
    relatorio.append("A auditoria identificou vulnerabilidades críticas que precisam de atenção imediata. As recomendações propostas devem ser implementadas o mais breve possível para garantir a segurança do sistema.\n")

    # Salvando o relatório em um arquivo de texto
    with open('relatorio_auditoria.txt', 'w') as arquivo_relatorio:
        arquivo_relatorio.writelines(relatorio)

    print("Relatório de auditoria gerado com sucesso.")

# Caminho para o arquivo de dados de vulnerabilidades
arquivo_dados = 'resultados_auditoria.txt'

# Gerar o relatório de auditoria
gerar_relatorio_auditoria(arquivo_dados)

___________

# Exemplo de uso da biblioteca pandas para gerar um relatório em CSV
import pandas as pd

# Geração de relatório CSV a partir de dados de auditoria
def gerar_relatorio_csv(arquivo_dados):
    dados = {
        'Vulnerabilidade': [],
        'Impacto': [],
        'Recomendação': []
    }

    with open(arquivo_dados, 'r') as f:
        linhas = f.readlines()

    # Organizar os dados de vulnerabilidades
    for i in range(0, len(linhas), 3):
        vulnerabilidade = linhas[i].split(": ")[1].strip()
        impacto = linhas[i+1].split(": ")[1].strip()
        recomendacao = linhas[i+2].split(": ")[1].strip()
        
        dados['Vulnerabilidade'].append(vulnerabilidade)
        dados['Impacto'].append(impacto)
        dados['Recomendação'].append(recomendacao)

    # Criar DataFrame e salvar como CSV
    df = pd.DataFrame(dados)
    df.to_csv('relatorio_auditoria.csv', index=False)
    print("Relatório CSV gerado com sucesso.")

# Gerar o relatório CSV
gerar_relatorio_csv(arquivo_dados)
