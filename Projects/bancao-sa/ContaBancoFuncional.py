menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def main_menu(value):
        match value:
            case "d":
                valor = float(input("Informe o valor do depósito: "))
                print(depositar(valor))
                return "depositar"
                
            case "s":
                valor = float(input("Informe o valor do saque: "))
                print(sacar(valor))
                return "Saque"
            case "e":
                imprimir_extrato()
                return "Extrato"
            case "q":
                  return "false"
            case _:
                return "Opção inválida!"

def adicionar_numero_saques():
     global numero_saques
     numero_saques += 1

def adicionar_ao_extrato(entrada):
     global extrato
     extrato += entrada
             
def depositar(valor):
    if valor > 0:
        global saldo
        saldo += valor
        adicionar_ao_extrato(f"Depósito: R$ {valor:.2f}\n")
        return "Operaçao Realizada com sucesso!"

    else:
        return "Operação falhou! O valor informado é inválido."
    
def sacar(valor):
    global saldo
    global limite
    global LIMITE_SAQUES
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente."

    elif excedeu_limite:
        return "Operação falhou! O valor do saque excede o limite."

    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques excedido."

    elif valor > 0:
        saldo -= valor
        adicionar_ao_extrato(f"Saque: R$ {valor:.2f}\n")
        adicionar_numero_saques()
        return "Operaçao Realizada com sucesso!"

    else:
        return "Operação falhou! O valor informado é inválido."
    

def imprimir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

if __name__ == "__main__":
    while True:

        opcao = input(menu).lower()
        flag = main_menu(opcao)
        if flag == "false":
             print("Programa será encerrado...\nVolte Sempre que precisar\nBancão SA\nCom você...\n   Pra você...\n      Por você!")
             break
        elif flag != "Opção inválida!":
             continue
        else:
             print(flag)
             print ("Tente novamente!")

