from class_sistema import *
from sistemaGUI import *

#lista para instanciar os servicos
servicos = []

clientes = []
veiculos = []
oss = []




#Funcao - Exemplo de uso
def inicializarSitema():
    # Criando serviços existentes no sistema
    
    servicos.append(Servico('Lavação completa', 50.0))
    servicos.append(Servico('Lavação motor', 30.0))
    servicos.append(Servico('Aspiração', 20.0))

    # Criando um cliente
    
    #clientes.append(Cliente('Bia', 'Pessoa Física', 'bia@example.com'))
    #clientes.append(Cliente('Ana', 'Pessoa Física', 'ana@example.com'))


    # Criando um veículos
    veiculos.append(Veiculo('BCD234', 'ModeloBIaz', 'MarcaBiaCar', 'Pequeno'))

    veiculos.append(Veiculo('ABC123', 'ModeloAnaX', 'MarcaAnaCar', 'Pequeno'))
    veiculos.append(Veiculo('ABC234', 'Modelo123', 'OutraMarcaAnaCar', 'Médio'))

    

    # Associando veículos ao cliente
    clientes[0].setveiculo(veiculos[0])
    
    clientes[1].setveiculo(veiculos[1])
    clientes[1].setveiculo(veiculos[2])


inicializarSitema()

root = tk.Tk()
sistema = SistemaLavagemCarros(root)
root.mainloop()