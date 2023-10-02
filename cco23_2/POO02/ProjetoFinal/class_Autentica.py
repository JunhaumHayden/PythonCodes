



class Usuario:
    """Classe para instanciar Usuarios comuns ao sistema"""
    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

    def autenticar(self, username, senha):
        return self.username == username and self.senha == senha

    def acessar_ambiente(self):
        print("Bem-vindo ao ambiente do usuário!")
        return 1


    def __str__(self) -> str:
        pass


class Funcionario:
    """Classe para instanciar Usuarios com acesso privilegiado ao sistema"""
    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

    def autenticar(self, username, senha):
        return self.username == username and self.senha == senha

    def acessar_ambiente(self):
        print("Bem-vindo ao ambiente do funcionário!")
        return 2

        


class Sistema:
    def __init__(self):
        self.usuarios = {}  # Dicionário para armazenar usuários e senhas
        self.funcionarios = {}  # Dicionário para armazenar funcionários e senhas

    def adicionar_usuario(self, username, senha):
        self.usuarios[username] = Usuario(username, senha)

    def adicionar_funcionario(self, username, senha):
        self.funcionarios[username] = Funcionario(username, senha)

    def autenticar_e_acessar_ambiente(self, username, senha):
        if username in self.usuarios:
            perfil = self.usuarios[username]
            if perfil.autenticar(username, senha):
                a = perfil.acessar_ambiente()
                
                return a
            else:
                print("Autenticação falhou para o perfil de usuário.")
        elif username in self.funcionarios:
            perfil = self.funcionarios[username]
            if perfil.autenticar(username, senha):
                a = perfil.acessar_ambiente()
                
                return a
            else:
                print("Autenticação falhou para o perfil de funcionário.")
        else:
            print("Perfil não encontrado.")

    def __str__(self):
        print(self.usuarios)
        pass
        #super().__str__()
        #for i in range(len(usuarios)):
        #    print("="*30)
        #   print(f'ID: {i}')
        #    print("="*30)
                            
#main - APP

if __name__ == '__main__':
    pass
    # Autenticar e acessar ambiente do usuário
    inicializarAutent()
    inicializarSitema()
    while True:
        print('-'*30)
        print("Para Usuario: user1, password1")
        print("Para Funcionario: employee1, password3")
        print('-'*30)
        print("\nUsuário 1:")
        user=input("Login: ")
        password=input("Senha: ")
        a = sistema.autenticar_e_acessar_ambiente(user, password)
        print(a)
        if a == 1:
            menu_usuario()
        elif a == 2:
            menu_func()
        flag = input("Deseja continuar? ? (s ou n)").lower()
        if flag == 'n':

            #print("if")
            break
        else:
            #print("else")
            continue

