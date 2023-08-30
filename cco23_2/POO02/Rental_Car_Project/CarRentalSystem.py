from ClassVeiculo import Veiculo
from ClassVeiculo import Sedan
from ClassVeiculo import SUV
from ClassVeiculo import Compacto

from ClassClient import Cliente
from ClassClient import Locadora



def mainV():
    print("Bem-vindo à Locadora AloCar!")
    modelo = input("Digite o modelo do veículo: ")
    categoria = input("Digite a categoria do veículo (sedan/suv/compacto): ").lower()
    
    if categoria == "sedan":
        veiculo = Sedan(modelo, categoria)
    elif categoria == "suv":
        veiculo = SUV(modelo, categoria)
    elif categoria == "compacto":
        veiculo = Compacto(modelo, categoria)
    else:
        print("Categoria inválida.")
        return
    
    tarifa = veiculo.calcular_tarifa()
    print(f"Modelo: {veiculo.modelo}")
    print(f"Categoria: {veiculo.categoria}")
    print(f"Tarifa: R${tarifa:.2f}")

# Chama o método main
#mainV()




def mainC():
    print("Bem-vindo à Locadora AloCar!")
    
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa) do cliente: ")
    cnh = input("Digite o número da CNH do cliente: ")
    cartao_credito = input("Digite o número do cartão de crédito do cliente: ")
    contato = input("Digite as informações de contato do cliente: ")
    
    cliente = Cliente(nome, endereco, data_nascimento, cnh, cartao_credito, contato)
    
    modelo = input("Digite o modelo do veículo: ")
    categoria = input("Digite a categoria do veículo (sedan/suv/compacto): ").lower()
    
    if categoria == "sedan":
        veiculo = Sedan(modelo, categoria)
    elif categoria == "suv":
        veiculo = SUV(modelo, categoria)
    elif categoria == "compacto":
        veiculo = Compacto(modelo, categoria)
    else:
        print("Categoria inválida.")
        return
    
    locadora = Locadora()
    locadora.alugar_veiculo(cliente, veiculo)

# Chama o método main
mainC()
