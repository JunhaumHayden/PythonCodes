# class Cliente():
#     """Classe Clientes"""
#     def __init__(self, nome, endereco, data_nascimento, cnh, cartao_credito, contato):
#         self.nome = nome
#         self.endereco = endereco
#         self.data_nascimento = data_nascimento
#         self.cnh = cnh
#         self.cartao_credito = cartao_credito
#         self.contato = contato
    
#     def idade(self):
#         from datetime import datetime
#         hoje = datetime.now()
#         nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
#         idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
#         return idade
    
#     def __str__(self):
#         print(f"Cliente: {self.nome}")
#         print(f"Data nascimento: {self.data_nascimento}")
#         print(f"Idade: {self.idade()}")
#         print(f"Contato: {self.contato}")

# class Locadora():
#     """Classe Locadora"""
#     def alugar_veiculo(self, cliente, veiculo):
#         if cliente.idade() < 21:
#             print("Desculpe, você não possui idade suficiente para alugar um veículo.")
#             return
#         seguro_adicional = veiculo.calcular_seguro()
        
#         cliente.__str__()
#         print(f"Veículo alugado: {veiculo.modelo}")
#         print(f"Valor do aluguel: R${seguro_adicional + veiculo.preco_aluguel}")
#         print("Aluguel realizado com sucesso!")


class Veiculo:
    def __init__(self, modelo, categoria):
        self.modelo = modelo
        self.categoria = categoria
    
    def calcular_seguro(self):
        if self.categoria == "sedan":
            return 100
        elif self.categoria == "suv":
            return 150
        elif self.categoria == "compacto":
            return 80
        else:
            return 0

class Cliente:
    """Classe Clientes"""
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
    
    def __str__(self):
        print(f"Cliente: {self.nome}")
        print(f"Data nascimento: {self.data_nascimento}")
        print(f"Idade: {self.idade()}")
        print(f"Contato: {self.contato}")

class Locadora:
    """Classe Locadora"""
    def alugar_veiculo(self, cliente, veiculo):
        if cliente.idade() < 21:
            print("Desculpe, você não possui idade suficiente para alugar um veículo.")
            return
        
        seguro_adicional = veiculo.calcular_seguro()
        
        cliente.__str__()
        print(f"Veículo alugado: {veiculo.modelo}")
        print(f"Valor do aluguel: R${seguro_adicional + veiculo.preco_aluguel}")
        print("Aluguel realizado com sucesso!")

# Restante do código permanece o mesmo
