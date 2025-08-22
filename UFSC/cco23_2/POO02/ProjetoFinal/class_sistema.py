import datetime
from datetime import datetime
import random
import uuid
import tkinter as tk
from tkinter import ttk
import pandas as pd



class Veiculo:
    """Classe para instanciar veiculos"""
    def __init__(self, placa, modelo, marca, categoria):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.categoria = categoria
        
    def to_dict(self):
        return {'Placa': self.placa, 'Modelo': self.modelo, 'Marca': self.marca, 'Categoria': self.categoria}

    def __str__(self):
        return f"Placa: {self.placa}\nModelo: {self.modelo}\nMarca: {self.marca}\nCategoria: {self.categoria}"
        

    # Métodos getters e setters    

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
    def __init__(self,id, nome, tipo, info_contato):
        self.id = id
        self.nome = nome
        self.tipo = tipo  # Pessoa Física ou Jurídica
        self.info_contato = info_contato
        self.veiculos = []  # Lista para armazenar os veículos associados ao cliente

    # Métodos getters e setters
    def get_cliente_id(self):
        return self.id

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


    def to_dict(self):
        return {'Nome': self.nome, 'Tipo': self.tipo, 'Contato': self.info_contato}

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nTipo: {self.tipo}\nContato: {self.info_contato}"
        

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
        #print(f"Descrição: {self.descricao}")
        #print(f"Valor: {self.valor_padrao}")
        return f"Descrição: {self.descricao}\n Valor: {self.valor_padrao}"
    
    def to_dict(self):
        return {'Descrição': self.descricao, 'Valor': self.valor_padrao}

        

class OrdemServico:
    """Classe para instanciar Ordens de Servicos"""
    def __init__(self, veiculo, cliente):
        self.data_os = datetime.today()
        self.numero = self.gerar_numero()
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



    def to_dict(self):
        return {
            'Número OS': self.numero,
            'Estado': self.estado,
            'Data': self.data_os,
            'Cliente': self.cliente.to_dict(),
            'Veículo': self.veiculo.to_dict(),
            'Itens de Serviço': [item['servico'].to_dict() for item in self.itens_servico],
            'Total da Ordem': self.total_ordem,
            'Taxa de Desconto': self.taxa_desconto
            }        

    def gerar_numero(self):
        data_formatada = self.data_os.strftime("%Y%m%d_%H%M")
        numero_aleatorio = str(random.randint(10, 99))
        identificador_unico = str(uuid.uuid4().hex)[:2]  # Dois primeiros dígitos do UUID
        numero_gerado = f"{data_formatada}_{numero_aleatorio}{identificador_unico}"
        return numero_gerado

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

    @staticmethod
    def pesquisar_ordem_servico(numero_os, lista_ordens_servico):
        for ordem in lista_ordens_servico:
            if ordem.numero == numero_os:
                return ordem
        return None

    def __str__(self):
       
        print('*'*20)
        print(f"OS: {self.numero}")
        print(f"Estado: {self.estado}")
        print(f"Data: {self.data_os}")
        print(f'\n   Cliente: \n{self.cliente.__str__()}')
        print(f'\n   Veiculo: \n{self.veiculo.__str__()}')
        print('-'*20)
        print('-'*20)
        
        print('\n   Descrição dos serviços: ')
        print('-'*30)
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
        print('\n')
        return f"**Ordem de Serviço**\nNúmero OS: {self.numero}\nEstado: {self.estado}\nData: {self.data_os}\n" \
               f"Cliente: {self.cliente}\nVeículo: {self.veiculo}\nTotal da Ordem: {self.total_ordem}\n" \
               f"Taxa de Desconto: {self.taxa_desconto}"



    
   


#main
if __name__ == '__main__':
   
    # Exemplo de uso

    servicos = []
    clientes = []
    veiculos = []
    oss = []


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

    for ordem in clientes[1].getveiculo():
        print("Placa:", veiculo.placa)
        print("Modelo:", veiculo.modelo)
        print("Marca:", veiculo.marca)
        print("Categoria:", veiculo.categoria)
        print("---------------------")








   
