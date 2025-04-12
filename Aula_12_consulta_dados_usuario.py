# Funções de um sistema fictício para testes
def consulta_dados_usuario(usuario_id):
    """Simula uma consulta de dados do usuário, retornando informações sensíveis."""
    # Exemplo de vulnerabilidade de injeção de SQL
    query = f"SELECT * FROM usuarios WHERE id = {usuario_id}"
    if "OR" in usuario_id or "=" in usuario_id:
        return "Erro: Injeção de SQL detectada!"
    return f"Dados do usuário {usuario_id}"

def verificar_permissoes(usuario, recurso):
    """Simula a verificação de permissões de um usuário para acessar determinado recurso."""
    permissoes = {
        'admin': ['dados_sensitivos', 'usuarios'],
        'joao': ['usuarios'],
        'maria': ['usuarios'],
    }
    if recurso in permissoes.get(usuario, []):
        return "Acesso permitido"
    return "Acesso negado"

___


import unittest

# Função de teste para consulta de dados do usuário
class TestAuditoriaSeguranca(unittest.TestCase):

    def test_injecao_sql(self):
        """Teste para verificar proteção contra injeção de SQL."""
        resultado = consulta_dados_usuario("1 OR 1=1")
        self.assertEqual(resultado, "Erro: Injeção de SQL detectada!")

    def test_consulta_valida(self):
        """Teste para verificar consulta válida sem vulnerabilidade de SQL."""
        resultado = consulta_dados_usuario("1")
        self.assertNotEqual(resultado, "Erro: Injeção de SQL detectada!")
    
    def test_acesso_permitido_admin(self):
        """Teste para verificar se o admin pode acessar dados sensíveis."""
        resultado = verificar_permissoes("admin", "dados_sensitivos")
        self.assertEqual(resultado, "Acesso permitido")
    
    def test_acesso_negado_usuario_comum(self):
        """Teste para verificar se um usuário comum tem acesso negado a dados sensíveis."""
        resultado = verificar_permissoes("joao", "dados_sensitivos")
        self.assertEqual(resultado, "Acesso negado")

    def test_acesso_permitido_usuario(self):
        """Teste para verificar se um usuário comum tem acesso permitido ao recurso correto."""
        resultado = verificar_permissoes("joao", "usuarios")
        self.assertEqual(resultado, "Acesso permitido")

# Executar os testes
if __name__ == "__main__":
    unittest.main()

___

    def test_acesso_nao_autorizado(self):
        """Teste para verificar se um usuário não autorizado não consegue"""
___


Com essa modificação, o teste verificará se um usuário sem as permissões adequadas (neste caso, "ana") não consegue acessar informações sensíveis.

#### Conclusão:
Nesta aula, os alunos aprenderam sobre a importância dos testes automatizados na auditoria de software, como esses testes podem ser utilizados para garantir conformidade, segurança e integridade do sistema. Na atividade prática, eles implementaram um conjunto de testes automatizados usando Python e o framework `unittest`, verificando proteção contra injeção de SQL e controle de acesso. Essa abordagem permite automatizar partes críticas do processo de auditoria, garantindo eficiência e consistência na detecção de vulnerabilidades.

