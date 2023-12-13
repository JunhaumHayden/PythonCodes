#from class_Autentica import Usuario
#from class_Autentica import Funcionario
from class_Autentica import *
from class_sistema import *
import json
import random
import uuid
from datetime import datetime

#from class_sistema import Cliente
#from class_sistema import OrdemServico
#from class_sistema import Servico
#from sistemaGUI import *



servicos = []
clientes = []
veiculos = []
oss = []
#Lista que receberá os dados do sistema
sistema = Sistema()
id = 0



#Funcao - Exemplo de uso
def inicializarSitema():
    # Criando serviços existentes no sistema
    
    servicos.append(Servico('Lavação completa', 50.0))
    servicos.append(Servico('Lavação motor', 30.0))
    servicos.append(Servico('Aspiração', 20.0))

    # Criando um cliente
    
    clientes.append(Cliente(gerar_id(),'Bia', 'Pessoa Física', 'bia@example.com'))
    clientes.append(Cliente(gerar_id(),'Ana', 'Pessoa Física', 'ana@example.com'))


    # Criando um veículos
    veiculos.append(Veiculo('BCD234', 'ModeloBIaz', 'MarcaBiaCar', 'Pequeno'))

    veiculos.append(Veiculo('ABC123', 'ModeloAnaX', 'MarcaAnaCar', 'Pequeno'))
    veiculos.append(Veiculo('ABC234', 'Modelo123', 'OutraMarcaAnaCar', 'Médio'))

    

    # Associando veículos ao cliente
    clientes[0].setveiculo(veiculos[0])
    
    clientes[1].setveiculo(veiculos[1])
    clientes[1].setveiculo(veiculos[2])

    
    # Criando ordens de serviço
    oss.append(OrdemServico(veiculos[0], clientes[1]))
    oss[0].adicionar_item_servico(servicos[1], 50.0, 10)
    oss[0].calcular_total_ordem()
    oss[0].fechar_ordem()

    oss.append(OrdemServico(veiculos[2], clientes[0]))
    oss[1].adicionar_item_servico(servicos[2], 30.0, 5)
    oss[1].calcular_total_ordem()
    oss[1].cancelar_ordem()

    oss.append(OrdemServico(veiculos[1], clientes[1]))
    oss[2].adicionar_item_servico(servicos[1], 50.0, 10)
    oss[2].adicionar_item_servico(servicos[2], 30.0, 5)
    oss[2].calcular_total_ordem()

    # Pesquisando veículos do cliente
    print("Veículos associados ao cliente:")
    for veiculo in clientes[1].getveiculo():
        print("Placa:", veiculo.placa)
        print("Modelo:", veiculo.modelo)
        print("Marca:", veiculo.marca)
        print("Categoria:", veiculo.categoria)
        print("---------------------")

def inicializarAutent():
    # Adicionar usuários e funcionários
    sistema.adicionar_usuario("user1", "pwd1","0000")
    sistema.adicionar_usuario("user2", "pwd2","0001")
    sistema.adicionar_funcionario("employee1", "password3")


    # Autenticar e acessar o ambiente
    #print("Autenticando usuários e acessando seus ambientes:")


def new_order():
    print("  Criar Nova Ordem de Serviço")
    cliente_id = input("Digite o ID do Cliente: ")
    cliente_encontrado = None
    for cliente in clientes:
        if isinstance(cliente, Cliente) and cliente.get_cliente_id() == cliente_id:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        # Selecionar Veículo pelo Placa
        placa_veiculo = input("Digite a Placa do Veículo: ")
        veiculo_encontrado = None
        for veiculo in cliente_encontrado.getveiculo():
            if veiculo.getplaca() == placa_veiculo:
                veiculo_encontrado = veiculo
                break

        if veiculo_encontrado:
            # Criar a Ordem de Serviço
            nova_os = OrdemServico(veiculo_encontrado, cliente_encontrado)

            # Adicionar Serviços à Ordem de Serviço
            print("Adicionar Serviços à Ordem de Serviço:")
            printing("Vamos Adicionar Serviços Personalizados à Ordem de Serviço:")
            while True:
                descricao_servico = input("Digite a descrição do serviço (ou 'exit' para sair): ")
                if descricao_servico.lower() == 'exit':
                    break
                 # Adicionar o serviço à Ordem de Serviço
                novo_servico = Servico(descricao_servico, 0.0)
                valor_personalizado = float(input("Digite o valor personalizado para o serviço: "))
                pontuacao_acumulada = int(input("Digite a pontuação acumulada para o serviço: "))
                nova_os.adicionar_item_servico(novo_servico, valor_personalizado, pontuacao_acumulada)

            # Calcular o total da Ordem de Serviço
            nova_os.calcular_total_ordem()

            # Adicionar a nova OS à lista de OSs
            oss.append(nova_os)
            printing("Vamos Adicionar Serviços Padrão à Ordem de Serviço:")
            for servico in servicos:
                    print(servico)
                    print('\n')
                    control = input('Deseja incluir servico? (1 - sim e qualquer tecla para não incluir: )')
                    if control == '1':
                        servico.getdescricao
                        nova_os.adicionar_item_servico(servico.getdescricao(), servico.getvalor_padrao, 3.0)

            # Calcular o total da Ordem de Serviço
            nova_os.calcular_total_ordem()

            # Adicionar a nova OS à lista de OSs
            oss.append(nova_os)

            print("Nova Ordem de Serviço criada com sucesso!")
        else:
            print(f"Veículo com placa {placa_veiculo} não encontrado para o Cliente com ID {cliente_id}")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado")


#Funcao auxiliar para apresentacao dos menus
def printing(msg):
    print("="*30)
    print(f"{msg}")
    print("="*30)
    print( )


# #Funcao com Menu de interacao visao usuario
def menu_usuario(client_id):
    print(client_id)

    
    while True: 
    
        printing("    Menu do Cliente")
    
        while True:
            #Tratamento de excecao
            try:
                
                n = int(input(' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05 \n 0 - #Encerrar \n Opção: '))
                
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de fornecer os valores corretos.")

        for _ in range(7):
            print()

        if n == 0:
            printing("    Programa Encerrado")
            break
        elif n == 1:
            while True:
                while True:
                    try:
                        printing("    Menu Ordem de Serviço")
                        control = int(input(' 1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5 - Encerrar OS \n 0 - volta \n: '))
                        break
                    except ValueError:
                        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                if control == 0:
                    break
                elif control == 1:
                    printing("  Consultar Ordem de serviço")
                    oss[0].__str__()
                    
                    
                    
                
                elif control == 2:
                    printing("  Cadastrar Ordem de serviço")
                    new_order()
                    
                elif control == 3:
                    printing("  Adicionar Serviços")
                    oss[3].adicionar_item_servico(servicos[2], 15.0, 10)
                    oss[3].calcular_total_ordem()
                    print('Serviço adicionado\n__Total da ordem__:', oss[3].total_ordem)
                    
                    
                    #printing('opcao03')
                elif control == 4:
                    printing("  Cancelar OS")
                    oss[3].setstatus('CANCELADA')
                    oss[3].__str__()
                    printing('opcao04')
                    
                elif control == 5:
                    print("  Encerrar OS")
                    printing('Procure Um Funcionario!')
                
                else:
                    print('tente outra vez')
                
        
        elif n == 2:
            while True:
                printing("  Cadastrar Veiculo")
                print
                lista = list()
                car = ["placa", "modelo", "marca", "categoria"]
                for i in car:
                    print(i)
                    i == 'categoria'
                    print('------------')
                    if i == 'categoria':
                        while True:
                        #Tratamento de excecao
                            try:
                                c = int(input('Informe a categoria: \n 1 - Pequeno\n 2 - medio\n 3 - SUV / Caminhotene: \n'))
                                break
                            except ValueError:
                                print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                        if c == 1:
                            lista.append('Pequeno')
                        if c == 2:
                            lista.append('medio')
                        if c == 3:
                            lista.append('SUV / Caminhotene')
                        
                    else:
                        
                        elemento = input(f"Digite {i}: ")
                        lista.append(elemento)

                printing(f'tamanho da lista antes: {len(veiculos)}')
                veiculos.append(Veiculo(lista[0], lista[1],lista[2],lista[3]))
                printing(f'tamanho da lista depois: {len(veiculos)}')

                clientes[client_id].setveiculo(veiculos[len(veiculos) - 1])
                #clientes[client_id].setveiculo(len(veiculos) - 1)
                printing(f'tamanho da lista antes: {len(veiculos)}')
                #lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
                info_veiculos = []
                cont =1
                for veiculo in clientes[client_id].veiculos:
                    info_veiculo = f"Placa: {veiculo.placa}, Modelo: {veiculo.modelo}, Marca: {veiculo.marca}, Categoria: {veiculo.categoria}"
                    info_veiculos.append(info_veiculo)

                    print(f"Veiculo {cont}:\nPlaca: {veiculo.placa}, \nModelo: {veiculo.modelo}, \nMarca: {veiculo.marca}, \nCategoria: {veiculo.categoria}\n\n")
                    cont +=1
                    
                #return info_veiculos
                break
            
                
                
            # menu financeiro         
        elif n == 3:
            while True:
                
                control = (input(' 1 - consultar veiculos \n 2- Informacoes Financeiras \n 3 - Alterar mensalidade \n 0 - Voltar \n: '))
                if control == '0':
                    break
                if control == '1':
                    cont = 1
                    printing("  Consultar Veiculos")
                    printing('opcao01')
                    print("Veículos associados ao cliente:")
                    for veiculo in clientes[client_id].getveiculo():
                        print(f"Veiculo {cont}:\nPlaca: {veiculo.placa}, \nModelo: {veiculo.modelo}, \nMarca: {veiculo.marca}, \nCategoria: {veiculo.categoria}\n\n")
                        cont +=1
                        print("---------------------")
        
                    
                elif control == '2':
                    printing("  info_financeira")
                    printing('opcao02')
                    
                    
                elif control == '3':
                    printing("  Alterar mensalidade")
                    printing('opcao03')
                    
                    
                else:
                    print('tente outra vez')
                

        # Menu Administrativo
        elif n == 4:
        
            printing('opcao04')
            

        
        elif n == '5':
            print(" Lotação por curso")
            printing('opcao05')

            print("404 Page Not Found")
            print()
            print()
            print('The page youre looking for cant be found')
            print()
            print('a code 0x80244019 or as the message WU_E_PT_HTTP_STATUS_NOT_FOUND.')  

        else:
            print('Opção Inválida! Tente novamente...')  

# #Funcao com Menu de interacao visao funcionario
def menu_func():

    #Menu de interacao
    while True: 

        printing("    Menu Funcionario")
        
        n = input(' 1 - Dados de Cadastro \n 2 - Ordem de Serviço \n 3 - Menu 03 \n 4 - Menu 04 \n 5 - Menu 05 \n 0 - Encerrar \n Opção: ')
        for _ in range(7):
            print()

        if n == '0':
            printing("    LOGOUT.....")
            break
        elif n == '1':
            while True:
                printing("    Menu Dados de Cadastro")
                control = (input(' 1 - Cadastrar novo cliente \n 2- Cadastrar serviço \n 3 - Alterar valores \n 4 - Alterar Cliente \n 5- Listar Clientes \n 0 - volta \n: '))
                if control == '0':
                    break
                elif control == '1':
                    printing("  Dados de Cadastro")
                    user=input('Informe um Usuario: ')
                    password=input('Informe uma Senha: ')
                    new_id = gerar_id()
                    sistema.adicionar_usuario(user, password, new_id)

                    lista = list()
                    user = ['id', 'nome', 'tipo', 'info_contato']
                    for i in user:
                        
                        if i == 'tipo':
                            while True:
                            #Tratamento de excecao
                                try:
                                    c = int(input('Informe o tipo: \n 1 - Pessoa Fisica\n 2 - Pessoa Juridica\n'))
                                    break
                                except ValueError:
                                    print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                            if c == 1:
                                lista.append('Pessoa Fisica')
                            if c == 2:
                                lista.append('Pessoa Juridica')
                        elif i == 'id':
                            lista.append(new_id)

                        else:
                            
                            elemento = input(f"Digite {i}: ")
                            lista.append(elemento)

                    clientes.append(Cliente(lista[0], lista[1],lista[2],lista[3]))
                        
                    for id in clientes:
                        #print(id.id)
                        #print(new_id)
                        #print(id.id == new_id)
                        
                        if id.id == new_id:
                            print('Cadastro Concluido com Sucesso\n')
                            print(id)
                
                elif control == '2':
                    printing("  Cadastrar serviço")
                    service=input('Informe a descricao do serviço: \n')
                    pay=float(input('Informe o valor: R$ '))
                    servicos.append(Servico(service, pay))

                    
                elif control == '3':
                    printing("  Alterar valores dos Serviços")
                    for service in servicos:
                        printing(service)
                        print('\n')
                        print('\n')
                        control = input('Deseja alterar o valor deste servico? (1 - sim e qualquer tecla para não: )')
                        if control == '1':
                            pay = float(input('Informe o movo valor: R$'))
                            service.setvalor_padrao(pay)

                    
                elif control == '4':
                    printing("  Alterar Dados de Cliente")
                    for cliente in clientes:
                        printing(cliente)
                        print('\n')
                        print('\n')
                        control = input('Deseja alterar este cliente? (1 - Nome 2 - Contado e qualquer tecla para não alterar: )')
                        if control == '1':
                            name = input('Informe o novo nome: ')
                            cliente.setnome(name)
                            print(f'Nome alterado para {cliente.getnome()}')
                        elif control == '2':
                            name = input('Informe o novo contato: ')
                            cliente.setinfo_contato(name)
                            print(f'Nome alterado para {cliente.getinfo_contato()}')
                
                elif control == '5':
                    printing("  Listar Cliente")
                    for cliente in clientes:
                        printing(cliente)

                else:
                    print('tente outra vez')
                
        
        elif n == '2':
            while True:
                while True:
                    try:
                        printing("    Menu Ordem de Serviço")
                        control = int(input(' 1 - Consultar Todas OS \n 2 - Consultar OS pelo Numero\n 3 - Gerar OS \n 4 - Adicionar Serviços \n 5 - Cancelar OS \n 6 - Encerrar OS \n 0 - volta \n: '))
                        break
                    except ValueError:
                        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                if control == 0:
                    break
                elif control == 1:
                    printing("  Consultar Todas as Ordem de serviço")
                    for os in oss:
                        printing(os)


                elif control == 2:
                    printing("  Consultar por Numero da Ordem de serviço")
                    num = input('Informe o numero da Ordem de Serviço: ')
                                
                    for os in oss:
                        if num == os.numero:
                            printing(os)
                    else:
                        print('Ordem de Servico não encontrada!')
                                    
                elif control == 3:
                    printing("  Abrir Nova Ordem de serviço")
                    new_order()
                    
                elif control == 4:
                    printing("  Adicionar Serviços")
                    oss[3].adicionar_item_servico(servicos[2], 15.0, 10)
                    oss[3].calcular_total_ordem()
                    print('Serviço adicionado\n__Total da ordem__:', oss[3].total_ordem)
                    
                    
                    #printing('opcao03')
                elif control == 5:
                    printing("  Cancelar OS")
                    oss[3].setstatus('CANCELADA')
                    oss[3].__str__()
                    printing('opcao04')
                    
                elif control == 5:
                    print("  Encerrar OS")
                    printing('Procure Um Funcionario!')
                
                else:
                    print('tente outra vez')
                






            
                
                
            # menu financeiro         
        elif n == '3':
            while True:
                printing("  Menu Consultas")
                control = (input(' 1 - Informações Cadastrais \n 2 - Alteracao de notas \n 3 - Alterar curso \n 4 - Encerrar matricula \n 0 - volta \n: '))
                if control == '0':
                    break
                
                elif control == '1':
                    t = input('deseja imprimir a lista de clientes? (S ou N): ')
                    print(f'Opção escolhida: {t}')
                    printing('opcao01 do menu02')
                    if t == 's':
                        printing("  Lista de todos os Cliente")
                        printing('opcao S')

                        for i in range(len(2)):
                                printing(f'ID: {i}')
                                
                                
                                #clientes[i].__str__()
                    else:
                        print("  Consulta por ID")
                        
                    
                
                elif control == '2':
                    printing("  Cadastrar de notas")
                    while True:
                    #Tratamento de excecao
                        try:
                            N = int, input('1 - Alterar nota da Avaliação 02\n 2 - Alterar nota da Avaliação02\n : ')
                            break
                        except ValueError:
                            print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                    if n == '1':
                        printing('opcao01')
                        #cad = altera_nota01()
                    if n == '2':
                        printing('opcao02')
                    
                    
                elif control == '3':
                    printing("  Alterar curso")
                    printing('opcao03')
                
                    
                elif control == '4':
                    printing("  Encerrar matricula")
                    printing('opcao04')
                
                else:
                    printing('tente outra vez')
            





            
                

        # Menu Administrativo
        elif n == '4':
        
            printing('opcao04')
            while True:
                
                control = (input('1 - Informacoes cadastrais \n 2- Informacoes Financeiras \n 3 - Alterar mensalidade \n 4 - Calcular desconto \n 5 - Calcular mensalidade \n 0 - volta \n: '))
                if control == '0':
                    break
                if control == '1':
                    printing("  Informacoes cadastrais")
                    printing('opcao01')
        
                    
                elif control == '2':
                    printing("  info_financeira")
                    printing('opcao02')
                    
                    
                elif control == '3':
                    printing("  Alterar mensalidade")
                    printing('opcao03')
                    
                elif control == '4':
                    printing('opcao04')
                    
                elif control == '5':
                    printing('opcao05')
                    
                else:
                    print('tente outra vez')
            

        
        elif n == '5':
            print(" Lotação por curso")
            printing('opcao05')

            print("404 Page Not Found")
            print()
            print()
            print('The page youre looking for cant be found')
            print()
            print('a code 0x80244019 or as the message WU_E_PT_HTTP_STATUS_NOT_FOUND.')


# #Funcao com Menu de cadastro
def cadastro():
    pass
    lista = list()
    inst = ["o nome", "a idade", "o cpf", "o telefone", "curso", "o salario"]
    alun = ['o nome', 'a idade', 'o cpf', 'o telefone', 'o nome do responsavel', 'curso', 'O valor da mensalidade']

    while True:
        n = input(' tipo: 1 - aluno, 2 - Instrutor: ').lower()
        if n == 'aluno' or n == '1':
            lista.append('Aluno')
            
            for i in alun:
                if i == 'curso':
                    c = sel_curso()
                    lista.append(c)

                elif i == 'O valor da mensalidade':
                    lista.append(c[1])

                else:
                    elemento = input(f"Digite {i}: ")
                    lista.append(elemento)
            #print(lista)
            Flage = False
            while Flage == False:
                b = input('Aluno Bolsista? (s ou n)').lower()
                if b == 's':
                    valor = input('Qual a porcentagem? ')
                    lista.append(valor)
                    clientes.append(Scholarship(lista[0],lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7]),int(lista[8])))
                    lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
                    Flage = True
                
                elif b == 'n':
                    clientes.append(Students(lista[0], lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7])))
                    lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
                    Flage = True
                else:
                    
                    print('Opção Invalida!')
            break
                

        elif n == 'instrutor' or n == '2':
            lista.append('Instrutor')
            
            for i in inst:
                print(i)
                i == 'curso'
                if i == 'curso':
                    c = sel_curso()
                    lista.append(c[0])
                else:
                    elemento = input(f"Digite {i}: ")
                    lista.append(elemento)
            clientes.append(Instructor(lista[0], lista[1],int(lista[2]),lista[3],lista[4],lista[5],int(lista[6])))
            lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
            break
        else:
            
            print('Opção invalida, tente novamente!')
# Exemplo de uso

def verifica_login():
    a = sistema.autenticar_e_acessar_ambiente(screen.username.get(), screen.password.get())
        
    
    if a == 1:               
        if screen.username.get() == "user1":
            screen.msg['text'] = 'USER1'
            screen.msg02['text'] = 'Bem-vindo ao ambiente do tela!'
            menu_usuario(0)
        elif screen.username.get() == "user2":
            menu_usuario(1)
        elif a == 2:
            print('Menu Funcionario')
            menu_func()
    else:
        screen.msg['text'] = a

def gerar_id():
    numero_aleatorio = str(random.randint(10, 99))
    identificador_unico = str(uuid.uuid4().hex)[:2]  # Dois primeiros dígitos do UUID
    numero_gerado = f"{numero_aleatorio}{identificador_unico}"
    return numero_gerado

#inicializarSitema()


#main - APP

if __name__ == '__main__':
    # Autenticar e acessar ambiente do usuário
    inicializarAutent()
    inicializarSitema()

    menu_func()
    
    while True:
        pass
        print('-'*30)
        print("Para Usuario: user1, pwd1")
        print("Para Funcionario: employee1, password3")
        print('-'*30)
        print("\nUsuário 1:")
        user=input("Login: ")
        password=input("Senha: ")

        a = sistema.autenticar_e_acessar_ambiente(user, password)
       
        if a == 1:
            if user == "user1":
                menu_usuario(0)
            elif user == "user2":
                menu_usuario(1)
        elif a == 2:
            menu_func()
        flag = input("Deseja continuar? ? (s ou n)").lower()
        if flag != 's':

            #print("if")
            break
        else:
            #print("else")
            continue



