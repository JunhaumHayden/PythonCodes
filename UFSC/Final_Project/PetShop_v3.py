class Cliente:
    def __init__(self, raca, peso, idade, nome_animal, nome_dono, mensalidade):
        self.raca = raca
        self.peso = peso
        self.idade = idade
        self.nome_animal = nome_animal
        self.nome_dono = nome_dono
        self.mensalidade = mensalidade

    def imprimir_informacoes(self):
        print('-' * 30)
        print("Raça:", self.raca)
        print("Peso:", self.peso)
        print("Idade:", self.idade)
        print("Nome do animal:", self.nome_animal)
        print("Nome do dono:", self.nome_dono)
        print("Mensalidade:", self.mensalidade)
        print( )
        print( )

    def possui_restricao_alimentar(self):
        return self.restricao_alimentar

    def calcular_mensalidade(self, numero_banhos):
        return self.mensalidade + (25 * numero_banhos)


def cliente_mais_idoso(clientes):
    mais_idoso = None
    for cliente in clientes:
        if mais_idoso is None or cliente.idade > mais_idoso.idade:
            mais_idoso = cliente
    return mais_idoso

class ClienteVip(Cliente):
    def __init__(self, raca, peso, idade, nome_animal, nome_dono, mensalidade, restricao_alimentar):
        super().__init__(raca, peso, idade, nome_animal, nome_dono, mensalidade)
        self.restricao_alimentar = restricao_alimentar


# Exemplo de uso
clientes = []
clientes.append(Cliente("labrador", 7.5, 5, "bob", "ana", 100))
clientes.append(Cliente("poodle", 15.2, 8, "fred", "babi", 150))
clientes.append(Cliente("Golden Retriever", 20.1, 10, "Max", "clara", 200))
clientes.append(ClienteVip("Poodle", 7, 3, "Bella", "fabi", 150, True))


#Menu de interacao
while True: 

    print("="*30)
    print("    Menu principal")
    print("="*30)
    n = input(' 1 - imprime inf \n 2 - Restriçao \n 3 - mensalidade \n 4 - Mais Idoso \n 0 - Eencerrar \n : ')
    print( )
    print( )
    print( )

    if n == '0':
        print("="*30)
        print("    Programa Encerrado")
        print("="*30)
        break


    if n == '1':
        print("="*30)
        print("    Consulta Cliente")
        print("="*30)
        t = input('deseja imprimir a lista de clientes? (S ou N): ')
        print( )
        print( )
        print(f'Opeção escolhida: {t}')
        print( )
        print( )
        if t == 's':
            print("="*30)
            print("  Lista de Cliente")
            print("="*30)

            for i in range(len(clientes)):
                    print("="*30)
                    print(f'ID: {i}')
                    print("="*30)
                    
                    clientes[i].imprimir_informacoes()
        else:
            print("="*30)
            print("  Consulta por ID")
            print("="*30)
            c = int(input('Informe o Id: '))
            while c >= len(clientes):
                print("="*30)
                print('ID Invalido. Tente Novamente')
                print("="*30)
                print( )
                c = int(input('Informe o Id: '))
            else:
                print("="*30)
                print(f"  ID {c}")
                print("="*30)
                clientes[c].imprimir_informacoes()
            
            
          # Verificar se o cliente possui restrição alimentar          
    if n == '2': 
        print("="*30)
        print(" Restrição Alimentar")
        print("="*30)
        print("="*30)
            
        c = int(input('Informe o Id: '))
        while c >= len(clientes):
            print("="*30)
            print('ID Invalido. Tente Novamente')
            print("="*30)
            print( )
            c = int(input('Informe o Id: '))
        else:
            print("="*30)
            print(f"  ID {c}")
            print("="*30)
            restricao = clientes[c].restricao_alimentar
            print("Restrição alimentar:", restricao)
            print( )
            print( )
            

    # Calcular mensalidade do cliente
    if n == '3':
        print("="*30)
        print(" Calcular Mensalidade")
        print("="*30)
        c = int(input('Informe o Id: '))
        b = int(input("Banhos?: "))
        mensalidade = clientes[c].calcular_mensalidade(b)
        print("Mensalidade:", mensalidade)
        print( )
        print( )

    # Encontrar o cliente mais idoso
    if n == '4':
        print("="*30)
        print(" Calcular Mensalidade")
        print("="*30)

        mais_idoso = cliente_mais_idoso(clientes)
        print("Cliente mais idoso:")
        mais_idoso.imprimir_informacoes()
        print( )
        print( )
    else:
        print('tente novamente')