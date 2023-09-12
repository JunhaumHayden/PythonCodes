class Cliente:
    def __init__(self, nome, endereco, data_nascimento, cnh, cartao_credito, contato):
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.cnh = cnh
        self.cartao_credito = cartao_credito
        self.contato = contato
    
    def idade(self):
        from datetime import datetime
        hoje = datetime.now()
        nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade

class Veiculo:
    def __init__(self, modelo, categoria, preco_diaria):
        self.modelo = modelo
        self.categoria = categoria
        self.preco_diaria = preco_diaria
        self.alugado = False

    def get_diaria(self):
        return self.preco_diaria    
    def set_diaria(self,diaria):
        self.preco_diaria = diaria 
    
class Locadora:
    def __init__(self):
        self.clientes = []
        self.veiculos = []
    
    def cadastrar_cliente(self, nome, endereco, data_nascimento, cnh, cartao_credito, contato):
        cliente = Cliente(nome, endereco, data_nascimento, cnh, cartao_credito, contato)
        self.clientes.append(cliente)
    
    def cadastrar_veiculo(self, modelo, categoria, preco_diaria):
        veiculo = Veiculo(modelo, categoria, preco_diaria)
        self.veiculos.append(veiculo)
    
    def alugar_veiculo(self, cliente, veiculo, dias_aluguel, seguro):
        if cliente.idade() < 21:
            print("Desculpe, você não possui idade suficiente para alugar um veículo.")
            return
        
        if veiculo.alugado:
            print("Veículo já alugado.")
            return
        
        valor_aluguel = veiculo.preco_diaria * dias_aluguel
        
        if seguro:
            #valor_aluguel += dias_aluguel * 20
            if veiculo.categoria == 'compacto':
                valor_aluguel += dias_aluguel * 5
                #print('compacto R$5,00')
            elif veiculo.categoria == 'SUV':
                valor_aluguel += dias_aluguel * 15
                #print('SUV R$15,00')
            elif veiculo.categoria == 'sedan':
                valor_aluguel += dias_aluguel * 10
                #print('Sedan R$10,00')
       
            


        
        veiculo.alugado = True
        print(f"Cliente: {cliente.nome}")
        print(f"Veículo alugado: {veiculo.modelo}")
        print(f"Total a pagar: R${valor_aluguel}")
        print("Aluguel realizado com sucesso!")

# Exemplo de uso:
locadora = Locadora()

locadora.cadastrar_cliente("Ana", "Rua A", "10/01/1990", "123456", "1234-5678", "joao@gmail.com")
locadora.cadastrar_cliente("Bia", "Rua B", "10/01/1991", "123456", "1234-5678", "ana@gmail.com")
locadora.cadastrar_veiculo("Civic", "sedan", 100.0)
locadora.cadastrar_veiculo("EcoSport", "SUV", 120.0)
locadora.cadastrar_veiculo("Uno", "compacto", 80.0)


#######Funcoes de alteracao de listas

def cadastro():
    lista = list()
    cliente = ['O nome', 'O endereco', 'A data de nascimento(dia/mes/ano)', 'CNH', 'cartao_credito', 'contato']
    carro = ['o modelo', 'a Categoria', 'O valor da diaria']

    while True:
        print('Informe a opção: ')
        n = input('tipo: 1 - Cliente, 2 - Veiculo: ').lower()
        decora('')
        if n == 'cliente' or n == '1':
            
            for i in cliente:
                    elemento = input(f"Digite {i}: ")
                    lista.append(elemento)
            locadora.cadastrar_cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5],)
            decora('Cliente Cadastrado com sucesso!')
            break
                

        elif n == 'veiculo' or n == '2':
            
            for i in carro:
                elemento = input(f"Digite {i}: ")
                lista.append(elemento)
            locadora.cadastrar_veiculo(lista[0], lista[1],float(lista[2]))
            decora('Veiculo Cadastrado com sucesso')

            break
        else:
            
            print('Opção invalida, tente novamente!')



#Funcao de selecao seguro de veiculo
def sel_seg(i):
    seguro = input('Deseja fazer seguro? ').lower()
    if seguro == 's':
        seg = True
        
        if locadora.veiculos[i].categoria == 'compacto':
            # 
            print('compacto R$5,00')
        elif locadora.veiculos[i].categoria == 'SUV':
            
            print('SUV R$15,00')
        elif locadora.veiculos[i].categoria == 'sedan':
            
            print('Sedan R$10,00')
    else:
        print('Seguro não contratado')
        seg = False
    return seg

#Funcao de selecao de veiculo
def sel_carro():
    for i in range(len(locadora.veiculos)):
        elemento = input(f"Seleciona {locadora.veiculos[i].modelo}? (s ou n)").lower()
        if elemento == 's':
            seg = sel_seg(i)
            break
    print(f'Veiculo escolhido: {locadora.veiculos[i].modelo} com o valor da diaria de: {locadora.veiculos[i].preco_diaria} ')
    return i, seg

#Funcao de selecao da quantidade de diarias
def sel_diaria():
    d = int(input('Informe a quantidade de diarias: '))
    return d

def sel_cliente():
    print('Escolha um cliente na lista de cadastro: \n')
    for i in range(len(locadora.clientes)):
        elemento = input(f"O Motorista será {locadora.clientes[i].nome}? (s ou n)").lower()
        if elemento == 's':
            break

    return i


#Função para alterar os valores das diarias
def sel_valorDiaria():
    n = input(' 1 - Alterar \n 2 - Consultar \n Opção: ')
    for _ in range(4):
        print()

    if n == '1':
        for i in range(len(locadora.veiculos)):
            elemento = input(f"Seleciona {locadora.veiculos[i].modelo}? (s ou n)").lower()
            if elemento == 's':
                diaria = float(input('Informe o novo valor: '))
                locadora.veiculos[i].set_diaria(diaria)
                decora(" Valor Alterado")
                print(f'Valor da diaria alterado para {locadora.veiculos[i].get_diaria()}')
                break
            
    elif n == '2':
        for i in range(len(locadora.veiculos)):
            elemento = input(f"Seleciona {locadora.veiculos[i].modelo}? (s ou n)").lower()
            if elemento == 's':
                #diaria = float(input('Informe o novo valor: '))
                vd = locadora.veiculos[i].get_diaria()
                for _ in range(4):
                    print()
                for _ in range(4):
                    print()
                print(f'O valor da diaria é de R$ {vd}')
                #decora(" Valor Alterado")
                #print(f'Valor da diaria alterado para {locadora.veiculos[i].get_diaria()})
                break
            
        





#Funcao auxiliar de formatação de saida
def decora(text):
    print("="*30)
    print(" ", text)
    print("="*30)
    print( )
    print( )
    
    return




#cliente = locadora.clientes[0]
#veiculo, seg = sel_carro() 
#locadora.alugar_veiculo(cliente, locadora.veiculos[veiculo], sel_diaria(), seg)


#Menu de interacao
while True: 
    pass
    
    decora( " Menu principal" )
   
    n = input(' 1 - Alugar \n 2 - Cadastrar \n 3 - Cadastrar Valores \n 0 - Encerrar \n Opção: ')
    for _ in range(4):
        print()

    if n == '0':
        decora(" PROGRAMA ENCERRADO")
        break
    elif n == '1':
        cliente = locadora.clientes[sel_cliente()]
        veiculo, seg = sel_carro() 

        locadora.alugar_veiculo(cliente, locadora.veiculos[veiculo], sel_diaria(), seg)

    elif n == '2':

        decora(" Cadastro Cliente / Veiculo")
        cadastro()
        
    elif n == '3':

        decora("Alteração de valores")
        sel_valorDiaria() 

        #print("404 Page Not Found")
        #rint()
        #print()
        #print('The page youre looking for cant be found')
        #print()
        #print('a code 0x80244019 or as the message WU_E_PT_HTTP_STATUS_NOT_FOUND.')
        pass
    else:
        decora("Opção inválida!")
        print("Digite novamente!")
        print()
        print()
