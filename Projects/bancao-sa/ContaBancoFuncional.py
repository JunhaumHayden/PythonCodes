import textwrap


def apresenta_menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
             
def depositar(saldo, valor, extrato, /):
    """Funcao para realizar depositos"""
    #/: O uso de / antes dos parâmetros indica que todos os parâmetros após a barra são apenas posicionais e devem ser passados na ordem correta ao chamar a função, e não podem ser passados como argumentos de palavra-chave. Isso significa que a função só pode ser chamada com argumentos posicionais, e não permite o uso de argumentos de palavra-chave. Isso é útil para garantir que a função seja chamada corretamente e que os parâmetros sejam usados na ordem correta.
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        return saldo, extrato, "\n=== Depósito realizado com sucesso! ==="

    else:
        return saldo, extrato, "\n@@@ Operação falhou! O valor informado é inválido. @@@"
    
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Funcao para realizar saques"""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        return saldo, extrato, "\nOperação falhou! Você não tem saldo suficiente."

    elif excedeu_limite:
        return saldo, extrato, "\nOperação falhou! O valor do saque excede o limite."

    elif excedeu_saques:
        return saldo, extrato, "\nOperação falhou! Número máximo de saques excedido."

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, "Operaçao Realizada com sucesso!"

    else:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."
    

def imprimir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": "Rua TESTE"})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
        
        LIMITE_SAQUES = 3
        AGENCIA = "0001"

        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        usuarios = []
        contas = []
        while True:
            opcao = apresenta_menu().lower()
            match opcao:
                case "d":
                    valor = float(input("Informe o valor do depósito: "))
                    saldo, extrato, msg = depositar(saldo, valor, extrato)
                    print(msg)
                    continue
                    
                case "s":
                    valor = float(input("Informe o valor do saque: "))
                    saldo, extrato, msg = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
                    print(msg)
                    continue
                case "e":
                    imprimir_extrato(saldo, extrato=extrato)
                    continue
                case "q":
                    print("Programa será encerrado...\nVolte Sempre que precisar\nBancão SA\nCom você...\n   Pra você...\n      Por você!")
                    break
                case "nu":
                    criar_usuario(usuarios)
                case "nc":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)
                    if conta:
                        contas.append(conta)
                case "lc":
                    listar_contas(contas)
                case _:
                    print("Opção inválida!\n\nTente novamente!")
                    continue


if __name__ == "__main__":
    main()

    
