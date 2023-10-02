#from class_Autentica import Usuario
#from class_Autentica import Funcionario
from class_Autentica import Sistema
from class_sistema import Veiculo
from class_sistema import Cliente
from class_sistema import OrdemServico
from class_sistema import Servico


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
    
    clientes.append(Cliente('Bia', 'Pessoa Física', 'bia@example.com'))
    clientes.append(Cliente('Ana', 'Pessoa Física', 'ana@example.com'))


    # Criando um veículos
    veiculos.append(Veiculo('BCD234', 'ModeloBIaz', 'MarcaBiaCar', 'Pequeno'))

    veiculos.append(Veiculo('ABC123', 'ModeloAnaX', 'MarcaAnaCar', 'Pequeno'))
    veiculos.append(Veiculo('ABC234', 'Modelo123', 'OutraMarcaAnaCar', 'Médio'))

    

    # Associando veículos ao cliente
    clientes[0].setveiculo(veiculos[0])
    
    clientes[1].setveiculo(veiculos[1])
    clientes[1].setveiculo(veiculos[2])

    

    # Criando uma ordem de serviço
    os1 = OrdemServico('OS001', '2023-09-17', veiculos[0], clientes[0])
    os1.adicionar_item_servico(servicos[0], 50.0, 10)
    os1.calcular_total_ordem()
    print('****Total da ordem****:', os1.total_ordem)

    os2 = OrdemServico('OS002', '2023-09-17', veiculos[1], clientes[1])
    os2.adicionar_item_servico(servicos[1], 30.0, 10)
    os2.calcular_total_ordem()
    print('****Total da ordem****:', os1.total_ordem)

    # Add servicos em uma OS ABERTA
    os1.adicionar_item_servico(servicos[1], 35.0, 10)
    os1.calcular_total_ordem()
    print('Serviço adicionado\n__Total da ordem__:', os1.total_ordem)
    #os1.__str__()

    os2.adicionar_item_servico(servicos[2], 15.0, 10)
    os2.calcular_total_ordem()
    print('Serviço adicionado\n__Total da ordem__:', os2.total_ordem)
    #os2.__str__()




     # Pesquisando veículos do cliente
    print("Veículos associados ao cliente:")
    for veiculo in clientes[0].getveiculo():
        print("Placa:", veiculo.placa)
        print("Modelo:", veiculo.modelo)
        print("Marca:", veiculo.marca)
        print("Categoria:", veiculo.categoria)
        print("---------------------")

   

    # Pesquisando veículos do cliente
    print("Veículos associados ao cliente:")
    for veiculo in clientes[1].getveiculo():
        print("Placa:", veiculo.placa)
        print("Modelo:", veiculo.modelo)
        print("Marca:", veiculo.marca)
        print("Categoria:", veiculo.categoria)
        print("---------------------")

  

    # Fechar a ordem de serviço
    os1.setstatus('FECHADA')

    os1.setstatus('CANCELADA')

    os1.setstatus('ABERTA')

def inicializarAutent():
    # Adicionar usuários e funcionários
    sistema.adicionar_usuario("user1", "password1")
    sistema.adicionar_usuario("user2", "password2")
    sistema.adicionar_funcionario("employee1", "password3")

    # Autenticar e acessar o ambiente
    print("Autenticando usuários e acessando seus ambientes:")

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
    
        printing("    Menu Usuario")
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
                        control = int(input(' 1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5- Encerrar OS \n 0 - volta \n: '))
                        break
                    except ValueError:
                        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                if control == 0:
                    break
                elif control == 1:
                    printing("  Consultar Ordem de serviço")
                    os2.__str__()
                    
                    
                    
                
                elif control == 2:
                    printing("  Cadastrar Oredem de serviço")
                    os3 = OrdemServico('OS003', '2023-09-17', veiculos[1], clientes[1])
                    os3.adicionar_item_servico(servicos[1], 30.0, 10)
                    os3.calcular_total_ordem()
                    print('****Total da ordem****:', os3.total_ordem)
                    pass


                    #while True:
                    #Tratamento de excecao
                        #try:
                        #    N = int, input('1 - 01 Avaliação\n 2 - 02 Avaliação\n : ')
                        #    break
                        #except ValueError:
                        #    print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                    #if n == '1':
                    #    printing('opcao01 do menu02')
                    #if n == '2':
                    #    printing('opcao02 do menu02')
                    
                elif control == 3:
                    printing("  Adicionar Serviços")
                    os3.adicionar_item_servico(servicos[2], 15.0, 10)
                    os3.calcular_total_ordem()
                    print('Serviço adicionado\n__Total da ordem__:', os3.total_ordem)
                    os3.__str__()
                    
                    #printing('opcao03')
                elif control == 4:
                    printing("  Cancelar OS")
                    os3.setstatus('CANCELADA')
                    os3.__str__()
                    printing('opcao04')
                    
                elif control == 5:
                    print("  Encerrar OS")
                    printing('opcao04')
                
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
                        #veiculos_existentes = len(clientes[id].getveiculos())
                        #veiculo1 = Veiculo('ABC123', 'ModeloAnaX', 'MarcaAnaCar', 'Pequeno')
                        #clientes[client_id].setveiculo(veiculo1)
                        elemento = input(f"Digite {i}: ")
                        lista.append(elemento)

                printing(f'tamanho da lista antes: {len(veiculos)}')
                veiculos.append(Veiculo(lista[0], lista[1],lista[2],lista[3]))
                printing(f'tamanho da lista antes: {len(veiculos)}')

                clientes[client_id].setveiculo(veiculos[len(veiculos) - 1])
                #clientes[client_id].setveiculo(len(veiculos) - 1)
                printing(f'tamanho da lista antes: {len(veiculos)}')
                #lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
                print(clientes[client_id].getveiculo())
                break
            
                
                
            # menu financeiro         
        elif n == 3:
            while True:
                
                control = (input(' 1 - consultar veiculos \n 2- Informacoes Financeiras \n 3 - Alterar mensalidade \n 4 - Calcular desconto \n 5 - Calcular mensalidade \n 0 - Voltar \n: '))
                if control == '0':
                    break
                if control == '1':
                    printing("  Consultar Veiculos")
                    printing('opcao01')
                    print("Veículos associados ao cliente:")
                    for veiculo in clientes[client_id].getveiculo():
                        print("Placa:", veiculo.placa)
                        print("Modelo:", veiculo.modelo)
                        print("Marca:", veiculo.marca)
                        print("Categoria:", veiculo.categoria)
                        print("---------------------")
        
                    
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
        
        n = input(' 1 - Menu 01 \n 2 - Menu 02 \n 3 - Menu 03 \n 4 - Menu 04 \n 5 - Menu 05 \n 0 - Encerrar \n Opção: ')
        for _ in range(7):
            print()

        if n == '0':
            printing("    LOGOUT.....")
            break
        elif n == '1':
            while True:
                printing("    Menu Dados de Cadastro")
                control = (input(' 1 - Cadastrar novo cliente \n 2- Cadastrar serviço \n 3 - Alterar valores \n 4 - Alterar Cliente \n 5- Encerrar OS \n 0 - volta \n: '))
                if control == '0':
                    break
                elif control == '1':
                    printing("  Dados de Cadastro")
                    user=input('Informe um Usuario: ')
                    password=input('Informe uma Senha: ')
                    sistema.adicionar_usuario(user, password)
                    
                    
                
                elif control == '2':
                    printing("  Cadastrar serviço")
                    while True:
                    #Tratamento de excecao
                        try:
                            N = int, input('1 - 01 Avaliação\n 2 - 02 Avaliação\n : ')
                            break
                        except ValueError:
                            print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                    if n == '1':
                        printing('opcao01 do menu02')
                    if n == '2':
                        printing('opcao02 do menu02')
                    
                elif control == '3':
                    printing("  Alterar valores")
                    printing('opcao03')
                elif control == '4':
                    printing("  Alterar Cliente")
                    printing('opcao04')
                    
                elif control == '5':
                    print("  Encerrar OS")
                    printing('opcao04')
                
                else:
                    print('tente outra vez')
                
        
        elif n == '2':
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
            
                
                
            # menu financeiro         
        elif n == '3':
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
                

        # Menu Administrativo
        elif n == '4':
        
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



#inicializarSitema()


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
       
        if a == 1:
            if user == "user1":
                menu_usuario(0)
            elif user == "user2":
                menu_usuario(1)
        elif a == 2:
            menu_func()
        flag = input("Deseja continuar? ? (s ou n)").lower()
        if flag == 'n':

            #print("if")
            break
        else:
            #print("else")
            continue


    # Tentar acessar ambiente de funcionário com credenciais de usuário
    #print("\nTentativa de acessar ambiente de funcionário com credenciais de usuário:")
    #sistema.autenticar_e_acessar_ambiente("user1", "password3")

    # Autenticar e acessar ambiente do funcionário
    #print("\nFuncionário 1:")
    #sistema.autenticar_e_acessar_ambiente("employee1", "password3")
