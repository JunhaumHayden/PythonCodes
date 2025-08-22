import tkinter as tk
from tkinter import messagebox
import pandas as pd
import datetime
import random
import uuid

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
        return f"Placa: {self.placa}, Modelo: {self.modelo}, Marca: {self.marca}, Categoria: {self.categoria}"
        

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
    def __init__(self, nome, tipo, info_contato):
        self.nome = nome
        self.tipo = tipo  # Pessoa Física ou Jurídica
        self.info_contato = info_contato
        self.veiculos = []  # Lista para armazenar os veículos associados ao cliente

    # Métodos getters e setters

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
        return f"Nome: {self.nome}, Tipo: {self.tipo}, Contato: {self.info_contato}"
        

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
        return f"Descrição: {self.descricao}, Valor: {self.valor_padrao}"
    
    def to_dict(self):
        return {'Descrição': self.descricao, 'Valor': self.valor_padrao}

        

class OrdemServico:
    """Classe para instanciar Ordens de Servicos"""
    def __init__(self, veiculo, cliente):
        self.data_os = datetime.datetime.today()
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
        numero_gerado = f"{data_formatada}_{numero_aleatorio}_{identificador_unico}"
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

    def __str__(self):
       
        print('*'*20)
        print(f"OS: {self.numero}")
        print(f"Estado: {self.estado}")
        print(f"Data: {self.data_os}")
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
        return f"**Ordem de Serviço**\nNúmero OS: {self.numero}\nEstado: {self.estado}\nData: {self.data_os}\n" \
               f"Cliente: {self.cliente}\nVeículo: {self.veiculo}\nTotal da Ordem: {self.total_ordem}\n" \
               f"Taxa de Desconto: {self.taxa_desconto}"
    # ... (mesmo código)

# Classe ConsultaOrdemServico (com as correções)
class ConsultaOrdemServico:
    def __init__(self, root, ordens):
        self.root = root
        self.root.title("Consulta de Ordem de Serviço")

        self.ordens = ordens

        # Criar widgets
        self.label_numero = tk.Label(root, text="Número da Ordem de Serviço:")
        self.entry_numero = tk.Entry(root)

        self.button_abrir = tk.Button(root, text="Abrir Ordem", command=self.abrir_ordem)
        self.button_consultar = tk.Button(root, text="Consultar", command=self.consultar_ordens)
        self.button_sair = tk.Button(root, text="Sair", command=root.destroy)

        # Posicionar widgets
        self.label_numero.grid(row=0, column=0, padx=10, pady=10)
        self.entry_numero.grid(row=0, column=1, padx=10, pady=10)
        self.button_abrir.grid(row=1, column=0, columnspan=2, pady=10)
        self.button_consultar.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_sair.grid(row=3, column=0, columnspan=2, pady=10)

    def abrir_ordem(self):
        numero_os = self.entry_numero.get()
        if not numero_os:
            messagebox.showwarning("Aviso", "Por favor, digite o número da Ordem de Serviço.")
            return

        ordem_encontrada = None
        for ordem in self.ordens:
            if ordem.numero == numero_os:
                ordem_encontrada = ordem
                break

        if ordem_encontrada:
            self.mostrar_detalhes(ordem_encontrada)
        else:
            messagebox.showerror("Erro", f"Ordem de Serviço com número {numero_os} não encontrada.")

    def consultar_ordens(self):
        if not self.ordens:
            messagebox.showinfo("Informação", "Não há ordens de serviço disponíveis.")
            return

        df = pd.DataFrame.from_dict([os.to_dict() for os in self.ordens])
        ConsultaOrdemServico.mostrar_dataframe(df)

    @staticmethod
    def mostrar_dataframe(df):
        top = tk.Toplevel()
        top.title("Consulta de Ordens de Serviço")

        text = tk.Text(top)
        text.insert(tk.END, df)
        text.pack()

    @staticmethod
    def mostrar_detalhes(ordem):
        top = tk.Toplevel()
        top.title(f"Detalhes da Ordem de Serviço - Número {ordem.numero}")

        text = tk.Text(top)
        text.insert(tk.END, str(ordem))
        text.pack()

# Exemplo de uso
if __name__ == '__main__':
    # Criar ordens de exemplo
    os1, os2, os3 = criar_ordens_exemplo()

    root = tk.Tk()
    consulta_os = ConsultaOrdemServico(root, [os1, os2, os3])
    root.mainloop()
