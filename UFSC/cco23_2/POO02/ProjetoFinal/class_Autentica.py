
class Funcionario:
     
     """Classe para instanciar funcionários"""
     def __init__(self, username, password):
        self.username = username
        self.password = password

     def get_username(self):
        return self.username
     def set_username(self, username):
        self.username = username

     def get_password(self):
        return self.password
     def set_password(self, password):
        self.password = password

     def autenticar(self, username, senha):
        return self.username == username and self.senha == senha

     def acessar_ambiente(self):
        print("Bem-vindo ao ambiente do funcionário!")
        return 2


class Usuario(Funcionario):
    """Classe para instanciar clientes"""
    def __init__(self, username, password, cliente_id):
        super().__init__(username, password)
        self.cliente_id = cliente_id

    def get_cliente_id(self):
        return self.cliente_id
    
    def set_cliente_id(self, cliente_id):
        self.cliente_id = cliente_id

    def autenticar(self, username, senha):
        return self.password == username and self.senha == senha

    def acessar_ambiente(self):
        print("Bem-vindo ao ambiente do usuário!")
        return 1


    def __str__(self) -> str:
        pass
        


class Sistema:
    def __init__(self):
        self.usuarios = {}  # Dicionário para armazenar usuários e senhas
        self.funcionarios = {}  # Dicionário para armazenar funcionários e senhas

    def adicionar_usuario(self, username, senha, id):
        self.usuarios[username] = Usuario(username, senha, id)

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
            return 'Perfil não encontrado.'

    def __str__(self):
        print(self.usuarios)
        
                            
#main - APP

if __name__ == '__main__':
    pass

    #Instanciando class Sistema com uma lista vazia
    sistema = Sistema()


    sistema.set
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

