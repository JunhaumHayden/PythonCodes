# P1
#Aluno: Carlos Benedito Hayden de Albuquerque Junior
#Turme: INE5404-02208A (20232) - Programação Orientada a Objetos II
#


class Sistema:
    """Classe para controle de acesso de usuarios ao sistema"""
    def __init__(self):
        self.usuarios = {
            'user1': {'senha': 'senha1', 'perfil': 'usuario'},
            'user2': {'senha': 'senha2', 'perfil': 'usuario'},
            'employer1': {'senha': 'sf1', 'perfil': 'funcionario'}
        }

    def autenticar(self, usuario, senha):
        if usuario in self.usuarios and self.usuarios[usuario]['senha'] == senha:
            return self.usuarios[usuario]['perfil']
        else:
            return None

    def criar_usuario(self, usuario, senha, perfil):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = {'senha': senha, 'perfil': perfil}
            print(f'Usuário {usuario} com o perfil {perfil} criado com sucesso.')
        else:
            print('Usuário já existe. Escolha outro nome de usuário.')

    def excluir_usuario(self, usuario):
        if usuario in self.usuarios:
            del self.usuarios[usuario]
            print(f'Usuário {usuario} excluído com sucesso.')
        else:
            print('Usuário não encontrado.')

    def imprimir_usuarios(self):
        print("Lista de Usuários:")
        for usuario, info in self.usuarios.items():
            print(f"Usuário: {usuario}, Perfil: {info['perfil']}")


class Aplicacao:
    """Classe para autenticar e exibir ambiente dos usuarios no sistema"""
    def __init__(self):
        self.sistema = Sistema()
        self.usuario_autenticado = None

    def autenticar_usuario(self, usuario, senha):
        perfil = self.sistema.autenticar(usuario, senha)
        if perfil:
            self.usuario_autenticado = perfil
            print(f'Autenticação bem-sucedida para o perfil: {perfil}')
            return perfil
            
        else:
            print('Usuário ou senha incorretos. Tente novamente.')

    def acessar_ambiente(self):
        if self.usuario_autenticado == 'usuario':
            print('Bem-vindo ao ambiente do usuário.')
            return self.usuario_autenticado
        elif self.usuario_autenticado == 'funcionario':
            print('Bem-vindo ao ambiente do funcionário.')
            return self.usuario_autenticado
        else:
            print('Faça a autenticação primeiro.')



#main - APP

if __name__ == '__main__':
    # Exemplo de uso

    app = Aplicacao()

    # Autenticar como usuário
    app.autenticar_usuario('user1', 'senha1')
    app.acessar_ambiente()  # Saída: Bem-vindo ao ambiente do usuário.

    # Autenticar como funcionário
    app.autenticar_usuario('employer1', 'senha_func1')
    app.acessar_ambiente()  # Saída: Bem-vindo ao ambiente do funcionário.

    # Criar um novo usuário
    app.sistema.criar_usuario('novo_usuario', 'nova_senha', 'usuario')
    app.sistema.imprimir_usuarios()

    # Excluir um usuário
    app.sistema.excluir_usuario('user2')
    app.sistema.imprimir_usuarios()

    app.sistema.excluir_usuario('usuario2')
    app.sistema.imprimir_usuarios()