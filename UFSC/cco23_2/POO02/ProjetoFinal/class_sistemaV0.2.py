import datetime
import random
import uuid
import pandas as pd

class Veiculo:
    def __init__(self, placa, modelo, marca, categoria):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.categoria = categoria

    def to_dict(self):
        return {'Placa': self.placa, 'Modelo': self.modelo, 'Marca': self.marca, 'Categoria': self.categoria}

    def __str__(self):
        return f"Placa: {self.placa}, Modelo: {self.modelo}, Marca: {self.marca}, Categoria: {self.categoria}"

class Cliente:
    def __init__(self, nome, tipo, info_contato):
        self.nome = nome
        self.tipo = tipo
        self.info_contato = info_contato
        self.veiculos = []

    def to_dict(self):
        return {'Nome': self.nome, 'Tipo': self.tipo, 'Contato': self.info_contato}

    def __str__(self):
        return f"Nome: {self.nome}, Tipo: {self.tipo}, Contato: {self.info_contato}"

class Servico:
    def __init__(self, descricao, valor_padrao):
        self.descricao = descricao
        self.valor_padrao = valor_padrao

    def to_dict(self):
        return {'Descrição': self.descricao, 'Valor': self.valor_padrao}

    def __str__(self):
        return f"Descrição: {self.descricao}, Valor: {self.valor_padrao}"

class OrdemServico:
    def __init__(self, veiculo, cliente):
        self.data = datetime.datetime.today()
        self.numero = self.gerar_numero()
        self.veiculo = veiculo
        self.cliente = cliente
        self.estado = 'ABERTA'
        self.total_ordem = 0
        self.taxa_desconto = 0
        self.itens_servico = []

    def to_dict(self):
        return {
            'Número OS': self.numero,
            'Estado': self.estado,
            'Data': self.data,
            'Cliente': self.cliente.to_dict(),
            'Veículo': self.veiculo.to_dict(),
            'Itens de Serviço': [item['servico'].to_dict() for item in self.itens_servico],
            'Total da Ordem': self.total_ordem,
            'Taxa de Desconto': self.taxa_desconto
        }

    def __str__(self):
        return f"**Ordem de Serviço**\nNúmero OS: {self.numero}\nEstado: {self.estado}\nData: {self.data}\n" \
               f"Cliente: {self.cliente}\nVeículo: {self.veiculo}\nTotal da Ordem: {self.total_ordem}\n" \
               f"Taxa de Desconto: {self.taxa_desconto}"

    def gerar_numero(self):
        data_formatada = self.data.strftime("%Y%m%d_%H%M")
        numero_aleatorio = str(random.randint(10, 99))
        identificador_unico = str(uuid.uuid4().hex)[:2]
        numero_gerado = f"{data_formatada}_{numero_aleatorio}_{identificador_unico}"
        return numero_gerado

    def adicionar_item_servico(self, servico, valor_personalizado, pontuacao_acumulada):
        if self.estado == 'FECHADA' or self.estado == 'CANCELADA':
            print(f'Ordem de serviço {self.estado}.')
            print('Esta Ordem de Serviço não pode ser alterada.')
        else:
            self.itens_servico.append(
                {'servico': servico, 'valor_personalizado': valor_personalizado, 'pontuacao_acumulada': pontuacao_acumulada})

    def calcular_total_ordem(self):
        self.total_ordem = sum(item['valor_personalizado'] for item in self.itens_servico) - self.taxa_desconto

    def fechar_ordem(self):
        self.estado = 'FECHADA'

    def cancelar_ordem(self):
        self.estado = 'CANCELADA'

def mostrar_ordens_servico(ordens):
    df = pd.DataFrame.from_dict([os.to_dict() for os in ordens])
    print(df)

def load_user(user_id):
        import json
        try:
            with open("./pythonCode/cco23_2/POO02/ProjetoFinal/user_info.json", "r") as file:
                user_load = json.load(file)
            
        except ValueError:
                print("Erro", "Arquivo 'usuarios.json' não encontrado.")
        
            
        

        #user_load = {}
        for user_id, data in user_load.items():
            #user_load[user_id] = Cliente(data["nome"], data["tipo"], data["contato"])
            print((data["nome"]), (data["tipo"]), (data["contato"]))
            return (data["nome"]), (data["tipo"]), (data["contato"])

        return
# Exemplo de uso
if __name__ == '__main__':
    
    # Criando clientes
    cliente1 = Cliente('João da Silva', 'Pessoa Física', 'joao@example.com')
    cliente2 = Cliente('Maria Souza', 'Pessoa Jurídica', 'maria@example.com')
    #cliente1 = Cliente(load_user(1))
    #cliente2 = Cliente(load_user(2))

    # Criando veículos
    veiculo1 = Veiculo('ABC123', 'ModeloXYZ', 'MarcaCar', 'Pequeno')
    veiculo2 = Veiculo('DEF456', 'Modelo123', 'OutraMarca', 'Médio')

    # Criando serviços
    servico1 = Servico('Lavação completa', 50.0)
    servico2 = Servico('Lavação motor', 30.0)

    # Criando ordens de serviço
    os1 = OrdemServico(veiculo1, cliente1)
    os1.adicionar_item_servico(servico1, 50.0, 10)
    os1.calcular_total_ordem()
    os1.fechar_ordem()

    os2 = OrdemServico(veiculo2, cliente2)
    os2.adicionar_item_servico(servico2, 30.0, 5)
    os2.calcular_total_ordem()
    os2.cancelar_ordem()

    os3 = OrdemServico(veiculo1, cliente1)
    os3.adicionar_item_servico(servico1, 50.0, 10)
    os3.adicionar_item_servico(servico2, 30.0, 5)
    os3.calcular_total_ordem()

    # Mostrando as ordens de serviço
    mostrar_ordens_servico([os1, os2, os3])
