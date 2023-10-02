# P1
#Aluno: Carlos Benedito Hayden de Albuquerque Junior
#Turme: INE5404-02208A (20232) - Programação Orientada a Objetos II
#
#
# O programa apresentado é um sistema de estoque com um modulo de autenticação simples e um modulo operacional.
# - O main é composto por um menu interativo que solicita o login e senha para autenticar o usuário e apresenta o menu de acordo com o perfil do usuario (Cliente com permissao apenas para consultas ou  Funcionario com permissao para altear o Estoque).
# - O programa inicializa demonstrando as operaçoes de criação, edição, consulta , remoção das informações de cada modulo e somente isso solicita o login e senha.
# - Há o login e senha de cada tipo de usuario na tela de inicio para facilitar o uso.
# - O menu apresenta as opçoes e o usuario deve digitar o numero da opcao correspondente que deseja acessar. Opçoes que necesitam de interaçao do usuario sao explicados na tela do menu.
# Foi utilizado a biblioteca Datetime inicializada no inicio do programa, assim como as classes do modulo de autenticaçao.
# -- Modulo de Autenticaçao:
# No modulo de Autenticacao libera o acesso ao Modulo Estoque. Há duas classes principais: Sistema e Aplicacao:

# -Classe Sistema:
# É responsável por gerenciar usuários e suas credenciais (usuário, senha e perfil).
# Inicializa com alguns usuários e senhas predefinidos atraves da funcao inicializarAutent para ser possivel usar o programa.
# Possui métodos para autenticar usuários, criar novos usuários, excluir usuários e imprimir a lista de usuários.
# -Classe Aplicacao:
# Representa a aplicação interativa que interage com o sistema de autenticação.
# 
# -- Modulo Estoque:
# No modulo estoque sao realiza as operaçoes. Nele há as listas com as informações de mercadorias e entrada e saída de mercadorias. São 7 classes:
# -Classe Usuário:
# Possui atributos comuns a todos os tipos de usuários, como nome e CPF.
# Utilizada como classe base para as classes Cliente e Funcionario, que herdam seus atributos.
# -Classe Cliente:
# Herda da classe Usuário e adiciona atributos específicos, como endereço e data de nascimento.
# Pode realizar operações relacionadas a mercadorias, como consulta, compra e devolução.
# -Classe Funcionário:
# Herda da classe Usuário e adiciona atributos específicos, como número de matrícula.
# Pode realizar operações de gerenciamento de estoque, como registro de entrada e saída de mercadorias.
# -Classe Estoque:
# Armazena informações sobre as mercadorias disponíveis, como código (SKU - stock keeping unit), nome, quantidade e preço.
# Permite adicionar, remover e alterar mercadorias no estoque.
# -Classe EntradaSaida:
# Registra operações de entrada (compra), saída (venda), alteraçao (atualizar informações) e exclusão de mercadorias.
# Mantém o controle de data, hora, tipo de operação (entrada, saída, alteração e exclusão), quantidade e mercadoria envolvida.
# Permite a listagem de operações registradas.
# - Classe RegistroOperacao:
# Registra informações sobre cada operação realizada, incluindo a data, hora e usuário responsável.
# Utilizada pelas classes EntradaSaida e Estoque para registrar quem realizou cada operação.
# --As principais interações entre as classes incluem:
# O cliente pode consultar mercadorias.
# O funcionário pode gerenciar o estoque, registrar entrada e saída de mercadorias e atualizar informações sobre as mercadorias.
# As operações de entrada e saída são registradas na classe EntradaSaida, que utiliza a classe RegistroOperacao para manter informações sobre o usuário responsável.
# O estoque mantém a lista de mercadorias disponíveis, com operações de adição, remoção e alteração.
# O programa segue uma lógica de controle de estoque simples, onde os clientes podem consultar mercadorias, os funcionários podem gerenciar o estoque e todas as operações são registradas para fins de controle e histórico.




from datetime import datetime

from classAutent import Sistema
from classAutent import Aplicacao


class Usuario:
    """Classe principal para instanciar usuarios"""
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        

class Cliente(Usuario):
    """Classe para instanciar clientes"""
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf)
        self.endereco = endereco

    
    def __str__(self):
        super().__str__()
        print(f"Endereço: {self.endereco}")
        


class Funcionario(Usuario):
    """Classe para instanciar funcionarios"""
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo


    def __str__(self):
        super().__str__()
        print(f"Cargo: {self.cargo}")


class Mercadoria:
    """Classe para instanciar mercadorias"""
    def __init__(self, sku, nome, quantidade, preco):
        self.sku = sku
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"SKU: {self.sku}, Nome: {self.nome}, Quantidade: {self.quantidade}, Preço Unitário: {self.preco}"


class RegistroOperacao:
    """Classe para registrar data/hora e usuario responsavel pela movimentação de cada operacao no estoque"""
    def __init__(self, data_hora, usuario):
        self.data_hora = data_hora
        self.usuario = usuario

    def __str__(self):
        return str(f"Data/Hora: {self.data_hora}, Usuário: {self.usuario.nome}")

class EntradaSaida:
    """Classe para registrar operacoes de entrada e saida do estoque"""
    def __init__(self, mercadoria, quantidade, tipo, registro_operacao):
        self.mercadoria = mercadoria
        self.quantidade = quantidade
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.registro_operacao = registro_operacao

    def __str__(self):
        return f"Tipo: {self.tipo}, {self.registro_operacao}, Mercadoria: {self.mercadoria}, Quantidade: {self.quantidade}"
        


class Estoque:
    """Classe para instanciar o estoque"""
    def __init__(self):
        self.mercadorias = []
        self.registros = []  # Registros de entrada/saída

    def adicionar_mercadoria(self, mercadoria):
        self.mercadorias.append(mercadoria)

    def registrar_entrada(self, sku_mercadoria, quantidade, usuario):
        for mercadoria in self.mercadorias:
            if mercadoria.sku == sku_mercadoria:
                mercadoria.quantidade += quantidade
                registro = RegistroOperacao(datetime.now(), usuario)
                entrada = EntradaSaida(mercadoria, quantidade, 'Entrada', registro)
                self.registros.append(entrada)
                return True
        return False

    def registrar_saida(self, sku_mercadoria, quantidade, usuario):
        for mercadoria in self.mercadorias:
            if mercadoria.sku == sku_mercadoria:
                if mercadoria.quantidade >= quantidade:
                    mercadoria.quantidade -= quantidade
                    registro = RegistroOperacao(datetime.now(), usuario)
                    saida = EntradaSaida(mercadoria, quantidade, 'Saida', registro)
                    self.registros.append(saida)
                    return True
                else:
                    return False
        return False

    def listar_mercadorias(self):
        for mercadoria in self.mercadorias:
            a = mercadoria.preco
            b = mercadoria.quantidade
            print(f'{mercadoria}, Valor total: {a * b}')
        

    def listar_registros(self):
        for registro in self.registros:
            print(registro)
            print('------------------\n')

    def excluir_mercadoria(self, codigo_mercadoria, usuario):
        for mercadoria in self.mercadorias:
            if mercadoria.sku == codigo_mercadoria:
                self.mercadorias.remove(mercadoria)
                # Registra a operação de exclusão
                registro = RegistroOperacao(datetime.now(), usuario)
                exclusao = EntradaSaida(mercadoria, 0, 'Exclusao', registro)
                self.registros.append(exclusao)
                return
        print("Mercadoria não encontrada.")

    def alterar_mercadoria(self, codigo_mercadoria, nova_quantidade, novo_preco, usuario): #novo_nome,  
        for mercadoria in self.mercadorias:
            if mercadoria.sku == codigo_mercadoria:
                # Atualiza os valores da mercadoria
                #mercadoria.nome = novo_nome
                mercadoria.quantidade = nova_quantidade
                mercadoria.preco = novo_preco
                # Registra a operação de alteração
                registro = RegistroOperacao(datetime.now(), usuario)
                alteracao = EntradaSaida(mercadoria, nova_quantidade, 'Alteracao', registro)
                self.registros.append(alteracao)
                return
        print("Mercadoria não encontrada.")



#Lista que receberá os dados do sistema
####item: Armazenar (em listas) as informações de clientes, mercadorias e funcionários, assim como a entrada e saída de mercadorias.

#Modulo Autenticacao
app = Aplicacao()
#Modulo Estoque
estoque = Estoque()
clientes = []
funcionarios = []



def printing(msg):
    print("="*30)
    print(f"{msg}")
    print("="*30)
    print( )

# Funcoes para Casos de uso
def inicializarAutent():
    
    
    # Autenticar como usuário
    #app.autenticar_usuario('user1', 'senha1')
    #app.acessar_ambiente()  # Saída: Bem-vindo ao ambiente do usuário.

    # Autenticar como funcionário
    #app.autenticar_usuario('employer1', 'senha_func1')
    #app.acessar_ambiente()  # Saída: Bem-vindo ao ambiente do funcionário.
    
    ####Item: Criação, Edição, consulta , remoção das informações  e login;
    printing('Casos de Uso do Modulo de autenticacao: \nImprimindo Usuarios já existentes que foram criados na inicialização: \n')
    app.sistema.imprimir_usuarios()

    # Criar um novo usuário
    printing('Criando Novo Usuario do Modulo de autenticacao:')
    app.sistema.criar_usuario('novo_usuario', 'nova_senha', 'usuario')
    app.sistema.imprimir_usuarios()

    # Excluir um usuário existente
    printing('Excluindo usuario do Modulo de autenticacao: \n')
    app.sistema.excluir_usuario('user2')
    app.sistema.imprimir_usuarios()

    # Excluir um usuário nao existente
    printing('Excluindo usuario nao existente do Modulo de autenticacao')
    app.sistema.excluir_usuario('usuario2')
    app.sistema.imprimir_usuarios()
    printing('Fim de casos de uso Modulo autenticacao\n\n')

def inicializarEstoque():
    printing('Criando Usuarios para o Modulo Estoque')
    # Criando Clientes 
    clientes.append(Cliente('Ana', "123456789", 'ana@mail.com'))
    clientes.append(Cliente('Bia', "123456789", 'bia@email.com'))
    clientes.append(Cliente('Dani', "123456789", 'dani@email.com'))

    printing('Listando dados de clientes')
    print(clientes[0].nome)  # Atributo herdado da classe Usuario
    print(clientes[0].endereco)  # Atributo próprio da classe Cliente
    print(clientes[1].nome)  # Atributo herdado da classe Usuario
    print(clientes[1].endereco)  # Atributo próprio da classe Cliente
    print(clientes[2].nome)  # Atributo herdado da classe Usuario
    print(clientes[2].endereco)  # Atributo próprio da classe Cliente

    printing('Excluindo usuarios')
    print(f'lista com {len(clientes)} clientes')
    clientes.pop(2)
    print(f'Apos a exclusão a lista com {len(clientes)} clientes (ver codigo)')


    # Criando funcionarios
    funcionarios.append(Funcionario('Zara', "123456789", 'estoquista'))
    funcionarios.append(Funcionario('Xuxa', "123456789", 'vendedor'))
    funcionarios.append(Funcionario('Wanda', "123456789", 'compras'))

    
    printing('Listando dados de funcionarios')
    print(funcionarios[0].nome)  # Atributo herdado da classe Usuario
    print(funcionarios[0].cargo)  # Atributo próprio da classe Funcionario
    print(funcionarios[1].nome)  # Atributo herdado da classe Usuario
    print(funcionarios[1].cargo)  # Atributo próprio da classe Funcionario
    print(funcionarios[2].nome)  # Atributo herdado da classe Usuario
    print(funcionarios[2].cargo)  # Atributo próprio da classe Funcionario

    printing('Excluindo usuarios')
    print(f'lista com {len(funcionarios)} funcionarios')
    funcionarios.pop(2)
    print(f'Apos a exclusão a lista com {len(funcionarios)} funcionarios\n')


    # Adicionando mercadorias que serão armazenados em uma lista dentro da classe Estoque
    printing('Criando mercadorias e adicionando no estoque\n')
    mercadoria1 = Mercadoria("001", "Produto A", 10, 100.0)
    estoque.adicionar_mercadoria(mercadoria1)

    mercadoria1 = Mercadoria("002", "Produto B", 15, 150.0)
    estoque.adicionar_mercadoria(mercadoria1)

    mercadoria1 = Mercadoria("003", "Produto c", 5, 400.0)
    estoque.adicionar_mercadoria(mercadoria1)

    printing("Mercadorias no estoque:")
    estoque.listar_mercadorias()

    # Registrando entrada e saída
    printing('Movimentanto o estoque: entrada SKU001, Saida SKU002, Alterar preco SKU002, Excluir SKU003')
    estoque.registrar_entrada("001", 5, funcionarios[0])
    estoque.registrar_saida("002", 3, funcionarios[1])
    estoque.alterar_mercadoria("002", 30, 270.0, funcionarios[0])
    estoque.excluir_mercadoria("003", funcionarios[1])

    # Listando mercadorias no estoque e registros
    print("Mercadorias no estoque:")
    estoque.listar_mercadorias()

    print("\nRegistros de operações:")
    estoque.listar_registros()

#Funcao auxiliar para cadastro de estoque
def stock_enter(profile):
    lista = list()
    employer = ["o nome", "o cpf", "o cargo"]
    client = ['o nome', 'o cpf', 'o email']
    commodity = ['o SKU', 'o nome', 'a quantidade', 'o preco']

    if profile == 'cliente':
        
        for i in client:
            elemento = input(f"Digite {i}: ")
            lista.append(elemento)
        clientes.append(Cliente(lista[0], lista[1],lista[2]))
        
    elif profile == 'funcionario':
        
        for i in employer:
            elemento = input(f"Digite {i}: ")
            lista.append(elemento)
        funcionarios.append(Funcionario(lista[0], lista[1], lista[2]))

    elif profile == 'mercadoria':
        for i in commodity:
            elemento = input(f"Digite {i}: ")
            lista.append(elemento)
        mercadoria1 = Mercadoria(lista[0], lista[1], int(lista[2]), float(lista[3]))
        estoque.adicionar_mercadoria(mercadoria1)
        estoque.registrar_entrada(lista[0], int(lista[2]),select_employer())
#Funcao auxiliar para Movimentacao de estoque

def select_employer():
    elemento = 'n'
    while elemento != 's':
        for i in range(len(funcionarios)):
            elemento = input(f"Seleciona {funcionarios[i].nome}? (s ou n)").lower()
            if elemento == 's':
                return funcionarios[i]
                break

def in_out(status):
    lista = list()
    commodity = ['o SKU','a quantidade', 'o Funcionario']
    for i in commodity:
        if i == 'o Funcionario':
            while elemento != 's':
                employer_choice = select_employer()
                lista.append(employer_choice)
                break
        else:        
            elemento = input(f"Digite {i}: ")
            lista.append(elemento)
    if status == 'in':
        estoque.registrar_entrada(lista[0], int(lista[1]),lista[2])
    elif status == 'out':
        estoque.registrar_saida(lista[0], int(lista[1]),lista[2])
    elif status == 'off':
        estoque.excluir_mercadoria(lista[0],lista[2])

            
#Funcao Auxiliar para criacao de login e senha
def cria_login(profile):
    print('Passo 01: \nCriar Login e senha:')
    user=input('Informe um Usuario: ')
    password=input('Informe uma Senha: ')
    print('Passo 02: \nPreencher Cadastro: ')
    app.sistema.criar_usuario(user, password, profile)
    
def menu_usuario():
    while True: 
    
        printing("    Menu Usuario")
        while True:
            #Tratamento de excecao
            try:
                n = int(input(' 1 - Consulta lista de Estoque \n 2 - Consulta Item Estoque \n 0 - #Encerrar \n Opção: '))
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
        for _ in range(7):
            print()


        if n == 0:
            printing("  ---LOGOUT---")
            break
        elif n == 1:
            printing("  Consulta lista de Estoque")
            print("Mercadorias no estoque:")
            estoque.listar_mercadorias()
            
        elif n == 2:
            printing("  Consulta lista de Estoque")
            print("Mercadorias no estoque:")
            
            sku = input('Informe o SKU ou nome: ')
            for mercadoria in estoque.mercadorias:
                if mercadoria.sku == sku or mercadoria.nome == sku:
                    print(f'{mercadoria}')
                
                
                    
           

        else:
            print('Opção Inválida! Tente novamente...') 
            
def menu_func():
    while True: 
    
        printing("    Menu Funcionario")
        while True:
            #Tratamento de excecao
            try:
                n = int(input(' 1 - Menu Estoque \n 2 - Menu Usuarios \n 0 - #Encerrar \n Opção: '))
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
        for _ in range(7):
            print()


        if n == 0:
            printing("  ---Logout---")
            break
        elif n == 1:
            
            
            while True:
                printing("  Menu Estoque")
                control = (input(' 1 - Listar Estoque \n 2 - Cadastrar Nova Mercadoria \n 3 - Entrada no Estoque \n 4 - Saida de Estoque \n 5 - Listar de Registros de Movimentacao \n 6 - Excluir do Estoque \n 0 - volta \n: '))
                if control == '0':
                    break
                elif control == '1':
                    printing("  Listar Estoque")
                    print("Mercadorias no estoque:")
                    estoque.listar_mercadorias()
                    

                elif control == '2':
                    printing("  Cadastrar Nova Mercadoria")
                    stock_enter('mercadoria')

                    
                elif control == '3':
                    printing("  Entrada no Estoque")
                    in_out('in')
                    

                elif control == '4':
                    printing("  Saida no Estoque")
                    in_out('out')

                elif control == '5':
                    printing("  Listar de Registros de Movimentacao")
                    estoque.listar_registros()

                elif control == '6':
                    printing("  Excluir do Estoque")
                    in_out('off')
                else:
                    print('tente outra vez')
            
          
        elif n == 2:
            
            while True:
                printing("    Menu Usuarios")
                control = (input(' 1 - Cadastrar novo cliente \n 2 - Cadastrar Novo funcionario \n 3 - Excluir Clientes \n 4 - Listas de Usuários \n 0 - volta \n: '))
                if control == '0':
                    break
                elif control == '1':
                    printing("  Cadastrar novo cliente")
                    cria_login('usuario')
                    stock_enter('cliente')                  

                elif control == '2':
                    printing("  Cadastrar novo Funcionário")
                    cria_login('funcionario')
                    stock_enter('funcionario')
                    
                elif control == '3':
                    printing("  Excluir Clientes")
                    #Excluir usuario do sistema
                    user=input('Informe um Usuario: ')
                    app.sistema.excluir_usuario(user)
                    print('------------------------\n')
                    app.sistema.imprimir_usuarios()

                elif control == '4':
                    printing("  Listas de perfil de acesso ao sistema:")
                    app.sistema.imprimir_usuarios()
                    for i in range(len(clientes)):
                            printing(f'ID: {i}')
                            clientes[i].__str__()
                    printing("  Listas de funcionários")
                    #app.sistema.imprimir_usuarios()
                    for i in range(len(funcionarios)):
                            printing(f'ID: {i}')
                            funcionarios[i].__str__()
                    
                
                else:
                    print('tente outra vez')

        else:
            print('Opção Inválida! Tente novamente...') 


#main - APP
if __name__ == '__main__':
    pass
    # Autenticar e acessar ambiente do usuário
    inicializarAutent()
    inicializarEstoque()
    while True:
        print('-'*30)
        print("Para Usuario: user1, senha1")
        print("Para Funcionario: employer1, sf1")
        print('-'*30)
        print("\nUsuário 1:")
        user=input("Login: ")
        password=input("Senha: ")
        a = app.autenticar_usuario(user, password)
       
        if a == 'usuario':
            menu_usuario()
        elif a == 'funcionario':
            menu_func()
        flag = input("Deseja continuar? ? (s ou n)").lower()
        if flag == 'n':
            printing('  Programa Encerrado!!')
            break
        else:
            continue
