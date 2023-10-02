class Sistema:
    def __init__(self):
        self.usuarios = {
            'usuario1': {'senha': 'senha1', 'perfil': 'usuario'},
            'usuario2': {'senha': 'senha2', 'perfil': 'usuario'},
            'funcionario1': {'senha': 'senha_func1', 'perfil': 'funcionario'}
        }

    def autenticar(self, usuario, senha):
        if usuario in self.usuarios and self.usuarios[usuario]['senha'] == senha:
            return self.usuarios[usuario]['perfil']
        else:
            return None

class Aplicacao:
    def __init__(self):
        self.sistema = Sistema()
        self.usuario_autenticado = None

    def autenticar_usuario(self, usuario, senha):
        perfil = self.sistema.autenticar(usuario, senha)
        if perfil:
            self.usuario_autenticado = perfil
            print(f'Autenticação bem-sucedida para o perfil: {perfil}')
        else:
            print('Usuário ou senha incorretos. Tente novamente.')

    def acessar_ambiente(self):
        if self.usuario_autenticado == 'usuario':
            print('Bem-vindo ao ambiente do usuário.')
        elif self.usuario_autenticado == 'funcionario':
            print('Bem-vindo ao ambiente do funcionário.')
        else:
            print('Faça a autenticação primeiro.')

# Exemplo de uso
app = Aplicacao()

# Autenticar como usuário
app.autenticar_usuario('usuario1', 'senha1')
app.acessar_ambiente()  # Saída: Bem-vindo ao ambiente do usuário.

# Autenticar como funcionário
app.autenticar_usuario('funcionario1', 'senha_func1')
app.acessar_ambiente()  # Saída: Bem-vindo ao ambiente do funcionário.
