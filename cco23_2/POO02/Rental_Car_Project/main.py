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

locadora.cadastrar_cliente("João", "Rua A", "10/01/1990", "123456", "1234-5678", "joao@gmail.com")
locadora.cadastrar_veiculo("Civic", "sedan", 100)
locadora.cadastrar_veiculo("EcoSport", "SUV", 120)
locadora.cadastrar_veiculo("Uno", "compacto", 80)


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
    lista = []
    for i in range(len(locadora.veiculos)):
        elemento = input(f"Seleciona {locadora.veiculos[i].modelo}? (s ou n)").lower()
        if elemento == 's':
            lista.append(locadora.veiculos[i].modelo)
            seg = sel_seg(i)
            
            
            break
    print(f'Veiculo escolhido: {locadora.veiculos[i].modelo} com o valor da diaria de: {locadora.veiculos[i].preco_diaria} ')
    return i, seg

#Funcao de selecao da quantidade de diarias
def sel_diaria():
    d = int(input('Informe a quantidade de diarias: '))
    return d

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
   
    n = input(' 1 - Alugar \n 2 - Cadastrar Veiculo \n 3 - Cadastrar Cliente \n 0 - Encerrar \n Opção: ')
    for _ in range(4):
        print()

    if n == '0':
        decora(" PROGRAMA ENCERRADO")
        break
    elif n == '1':
        cliente = locadora.clientes[0]
        veiculo, seg = sel_carro() 

        locadora.alugar_veiculo(cliente, locadora.veiculos[veiculo], sel_diaria(), seg)
    elif n == '2':

        decora("Cadastrar Veiculo")

        print("404 Page Not Found")
        print()
        print()
        print('The page youre looking for cant be found')
        print()
        print('a code 0x80244019 or as the message WU_E_PT_HTTP_STATUS_NOT_FOUND.')
        pass
    elif n == '3':

        decora("Cadastrar Cliente")

        print("404 Page Not Found")
        print()
        print()
        print('The page youre looking for cant be found')
        print()
        print('a code 0x80244019 or as the message WU_E_PT_HTTP_STATUS_NOT_FOUND.')
        pass
    else:
        decora("Opção inválida!")
        print("Digite novamente!")
