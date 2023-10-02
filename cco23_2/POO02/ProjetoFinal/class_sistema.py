import datetime

class Veiculo:
    """Classe para instanciar veiculos"""
    def __init__(self, placa, modelo, marca, categoria):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.categoria = categoria

    def __str__(self):
        print(f"Placa: {self.placa}")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Categoria: {self.categoria}")

    def getplaca(self):
        return self.placa    
    def setplaca(self,placa):
        self.placa = placa
    
    def getmodelo(self):
        return self.placa    
    def setmodelo(self,modelo):
        self.modelo = modelo
    
    def getmarca(self):
        return self.marca    
    def setmarca(self,marca):
        self.placa = marca
    
    def getcategoria(self):
        return self.categoria    
    def setcategoria(self,categoria):
        self.placa = categoria
    

class Cliente:
    """Classe para instanciar Clientes"""
    def __init__(self, nome, tipo, info_contato):
        self.nome = nome
        self.tipo = tipo  # Pessoa Física ou Jurídica
        self.info_contato = info_contato
        self.veiculos = []  # Lista para armazenar os veículos associados ao cliente

    def getveiculo(self):
        return self.veiculos
    def setveiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def getnome(self):
        return self.nome    
    def setnome(self,nome):
        self.nome = nome

    def gettipo(self):
        return self.tipo    
    def settipo(self,tipo):
        self.tipo = tipo

    def getinfo_contato(self):
        return self.info_contato    
    def setinfo_contato(self,info_contato):
        self.info_contato = info_contato


    def __str__(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Contato: {self.info_contato}")
        

class Servico:
    """Classe para instanciar os serviços"""
    def __init__(self, descricao, valor_padrao):
        self.descricao = descricao
        self.valor_padrao = valor_padrao

    def getdescricao(self):
        return self.descricao    
    def setdescricao(self,descricao):
        self.descricao = descricao

    def getvalor_padrao(self):
        return self.valor_padrao    
    def setvalor_padrao(self,valor_padrao):
        self.valor_padrao = valor_padrao

    def __str__(self):
        print(f"Descrição: {self.descricao}")
        print(f"Valor: {self.valor_padrao}")
        

class OrdemServico:
    """Classe para instanciar Ordens de Servicos"""
    def __init__(self, numero, data, veiculo, cliente):
        self.numero = numero
        self.data = datetime.datetime.today()
        self.veiculo = veiculo
        self.cliente = cliente
        self.estado = 'ABERTA'
        self.total_ordem = 0
        self.taxa_desconto = 0
        self.itens_servico = []

    def getstatus(self):
        return self.estado    
    def setstatus(self,estado):
        if self.estado == 'FECHADA' or self.estado == 'CANCELADA':
            print(f'Ordem de serviço {self.estado}.')
            print('Esta Ordem de Serviço não pode ser alterada.')
        else:
            self.estado = estado

    def gettotal_ordem(self):
        return self.total_ordem    
    def settotal_ordem(self,total):
        if self.estado == 'FECHADA' or self.estado == 'CANCELADA':
            print(f'Ordem de serviço {self.estado}.')
            print('Esta Ordem de Serviço não pode ser alterada.')
        else:
            self.total_ordem = total

    def gettaxa_desconto(self):
        return self.taxa_desconto    
    def settaxa_desconto(self,desconto):
        if self.estado == 'FECHADA' or self.estado == 'CANCELADA':
            print(f'Ordem de serviço {self.estado}.')
            print('Esta Ordem de Serviço não pode ser alterada.')
        else:
            self.taxa_desconto = desconto

    def adicionar_item_servico(self, servico, valor_personalizado, pontuacao_acumulada):
        if self.estado == 'FECHADA' or self.estado == 'CANCELADA':
            print(f'Ordem de serviço {self.estado}.')
            print('Esta Ordem de Serviço não pode ser alterada.')
        else:
            self.itens_servico.append({'servico': servico, 'valor_personalizado': valor_personalizado, 'pontuacao_acumulada': pontuacao_acumulada})

    def calcular_total_ordem(self):
        self.total_ordem = sum(item['valor_personalizado'] for item in self.itens_servico) - self.taxa_desconto

    def fechar_ordem(self):
        self.estado = 'FECHADA'

    def cancelar_ordem(self):
        self.estado = 'CANCELADA'

    def __str__(self):
       
        print('*'*20)
        print(f"OS: {self.numero}")
        print(f"Estado: {self.estado}")
        print(f"Data: {self.data}")
        print('\n   Cliente: ')
        self.cliente.__str__()
        print('\n   Veiculo: ')
        self.veiculo.__str__()
        print('-'*20)
        print('-'*20)
        
        print('\n   Descrição dos serviços: ')
        print('-'*20)
        cont = 1
        for item in self.itens_servico:
            print(f'Item {cont}: ')
            print("  Descrição:", item['servico'].descricao)
            print("  Valor Personalizado:", item['valor_personalizado'])
            print("  Pontuação Acumulada:", item['pontuacao_acumulada'])
            print('*'*20)
            cont +=1
        print('-'*20)
        print(f"Valor: {self.total_ordem}")
        print(f"Descontos: {self.taxa_desconto}")
        print('*'*20)

#main
if __name__ == '__main__':
    # Exemplo de uso
    # Criando um veículo
    meu_veiculo = Veiculo('ABC123', 'ModeloXYZ', 'MarcaCar', 'Pequeno')

    # Criando um cliente
    cliente1 = Cliente('João da Silva', 'Pessoa Física', 'joao@example.com')

    # Criando um serviço
    servico1 = Servico('Lavação completa', 50.0)
    servico2 = Servico('Lavação motor', 30.0)

    # Criando uma ordem de serviço
    os1 = OrdemServico('OS001', '2023-09-17', meu_veiculo, cliente1)
    os1.adicionar_item_servico(servico1, 50.0, 10)
    os1.calcular_total_ordem()
    print('****Total da ordem****:', os1.total_ordem)

    # Fechar a ordem de serviço
    os1.setstatus('FECHADA')

    print('Estado da ordem:\n')
    os1.__str__()

    os1.adicionar_item_servico(servico2, 30.0, 10)
    os1.calcular_total_ordem()
    print('__Total da ordem__:', os1.total_ordem)
    os1.__str__()

    os1.setstatus('CANCELADA')

    os1.setstatus('ABERTA')

    # Criando um cliente com dois veiculos
    cliente1 = Cliente('João da Silva', 'Pessoa Física', 'joao@example.com')

    # Criando veículos
    veiculo1 = Veiculo('ABC123', 'ModeloXYZ', 'MarcaCar', 'Pequeno')
    veiculo2 = Veiculo('DEF456', 'Modelo123', 'OutraMarca', 'Médio')

    # Associando veículos ao cliente
    cliente1.adicionar_veiculo(veiculo1)
    cliente1.adicionar_veiculo(veiculo2)

    # Pesquisando veículos do cliente
    print("Veículos associados ao cliente:")
    for veiculo in cliente1.pesquisar_veiculos():
        print("Placa:", veiculo.placa)
        print("Modelo:", veiculo.modelo)
        print("Marca:", veiculo.marca)
        print("Categoria:", veiculo.categoria)
        print("---------------------")