from random import randint


class Geral:
    def __init__(self):
        pass

    def fimDaTela(self):
        print(f"""{'-='*5}FIM DA TELA{'-='*5}\n""")


class Funcionario(Geral):
    def __init__(self):
        self.setSalary
        self.setCodigo()
        self.gerente = False

    def setCodigo(self):
        with open("codigos.txt", "r") as arquivo:
            temp = arquivo.read()
            aux = temp
            temp = temp.split(",")
            read = []
            for i in temp:
                if not i == "":
                    i = i.split("/")
                    read.append(i[0])
                    read.append(i[1])
            if self.nome not in read:
                arquivo.close()
                codigo = "23" + str(randint(100, 200))
                with open("codigos.txt", "w") as arquivo:
                    arquivo.write(f"{aux}{self.nome}/{codigo},")
                    self.codigo = codigo
                    arquivo.close()
            else:
                self.codigo = read[read.index(f"{self.nome}") + 1]

    def ger_Demitir(self, funcionario):
        if isinstance(funcionario, Cliente):
            print("Você não pode demitir um cliente.")
        elif self.gerente:
            ordem = input(
                f"Você deseja mesmo demitir o funcionario {funcionario.nome}? (s/n) "
            ).upper()
            while not (ordem == "S" or ordem == "N"):
                ordem = input(
                    f"Essa resposta '{ordem}' é indevida. Insira outra: "
                ).upper()
            if ordem == "S":
                nome_antigo = funcionario.nome
                funcionario.setNome()
                while funcionario.nome == nome_antigo:
                    funcionario.setNome()
                print(
                    f"\nO funcionário {nome_antigo} foi demitido e o trabalhador {funcionario.nome} foi alocado.\n"
                )
            else:
                print(f"Ok, {self.nome}. Boa tarde.")
        else:
            print(f"{self.nome}, você não tem permissões de gerente.")


class Visitante(Geral):
    def __init__(self):
        with open("contador.txt", "r") as arquivo:
            temp = arquivo.read()
            self.visitante = int(temp) + 1
            arquivo.close()
        with open("contador.txt", "w") as arquivo:
            arquivo.write(str(self.visitante % 11))
            arquivo.close()

    def checaSorte(self):
        self.sorte = False
        if self.visitante == 10:
            self.sorte = True


class Gerente(Funcionario):
    def __init__(self):
        self.setNome()
        self.setSalary()
        Funcionario.__init__(self)
        self.gerente = True

    def setSalary(self):
        self.salario = 5000 + 0.05 * (randint(0, 10)) * 5000

    def setNome(self):
        possiveisNomes = ["Leonard", "Sheldon", "Howard", "Rajesh"]
        self.nome = possiveisNomes[randint(0, 3)]

    def getInfos(self, atendente, caixa):
        list = [atendente, caixa, self]
        print(" ")
        for i in list:
            print(f"{type(i).__name__}: {i.nome} / {i.codigo} / R${i.salario}")
        print(" ")


class Caixa(Funcionario):
    def __init__(self):
        self.setNome()
        self.setSalary()
        Funcionario.__init__(self)

    def setSalary(self):
        self.salario = 3000

    def setNome(self):
        possiveisNomes = ["Mario", "Johnny", "Wellington", "Barrabás", "Samuel"]
        self.nome = possiveisNomes[randint(0, 4)]

    def checaCliente(self, cliente):
        cliente.confiavel = 1
        chance = randint(1, 20)
        if chance == 1:
            cliente.confiavel = 0
            if cliente.sorte:
                print(
                    f"Como você não é um cliente confiável, você perdeu a sua promoção."
                )
                self.sorte = False

    def setgetPreco(self, cliente):
        diaria = (cliente.carro).split(",")
        diaria = diaria[1]
        dias = int(
            input(
                f"\nCaixa {self.nome}:\n{cliente.nome}, você deseja alugar o carro por quantos dias? "
            )
        )

        infos = cliente.carro.split(";")
        infos2 = infos[0].split(",")

        print(
            f"\nAqui está o seu orçamento:\n\nPreço entrada da classe {infos[2]}: + R${infos[1]}.00"
        )
        print(f"Preço por diária {infos2[0]}: + R${infos2[1]}.00")
        print(f"Diárias: {dias}")
        if cliente.confiavel == 0:
            print(
                f"Preço {infos2[0]} para {dias} dias COM MULTA: + R${int(infos2[1])*dias*1.3}.00"
            )
            print("--" * 20)
            print(f"Total: + R${int(infos[1])+(int(infos2[1])*dias*1.3)}.00")
        else:
            print(f"Preço {infos2[0]} para {dias} dias: + R${int(infos2[1])*dias}.00")
            total = int(infos[1]) + (int(infos2[1]) * dias)
            if cliente.sorte:
                print(f"Desconto de 10% por sorte: - R${total*0.1}")
                total *= 0.9
            print("--" * 10)
            print(f"Total: = R${total:.2f}")

    def getSalarios(self, gerente, atendente):
        print(f"\nSalário do Gerente {gerente.nome}: {gerente.salario}")
        print(f"Salário do Caixa {self.nome}: {self.salario}")
        print(f"Salário do Atendente {atendente.nome}: {atendente.salario}\n")


class Atendente(Funcionario):
    def __init__(self):
        self.setNome()
        self.setSalary()
        Funcionario.__init__(self)

    def setSalary(self):
        self.salario = 2500 + 0.02 * (randint(0, 60)) * 2500

    def setNome(self):
        atendentesNomes = ["João", "Mauro", "Jonathan", "Alex"]
        self.nome = atendentesNomes[randint(0, 3)]


class Cliente(Visitante):
    def __init__(self):
        Visitante.__init__(self)
        self.nome = input(
            f"""{'-='*5}TELA DE CLIENTE{'-='*5}\nBoa tarde, como você se chama? """
        )
        self.checaSorte()
        if self.sorte:
            print(
                f"ALERTA! As luzes piscaram pra você e você ganhou um desconto de 10%. Você foi nosso centésimo cliente hoje."
            )

    def setTipoDeCarro(self, atendente):
        print(
            f"\nAtendente {atendente.nome}:\nSr(a) {self.nome}, nós da Aluga&Roda possuímos 5 tipos de carros.\nSelecione qual você deseja: "
        )
        ordem = input(
            f"1 - Econômico 2 - Compacto\n3 - Médio     4 - Recomendação\n5 - SUV\nInforme o desejado: "
        )
        aux = ["1", "2", "3", "4", "5"]
        while ordem not in aux:
            ordem = input(f"Essa resposta '{ordem}' é inválida. Insira novamente: ")
        self.classeDoCarro = int(ordem) - 1

    def setCarro(self, atendente):
        arquivos = [
            "Econômicos150",
            "Compactos120",
            "Médios200",
            "Recomendações200",
            "SUV300",
        ]
        info = arquivos[self.classeDoCarro]
        arquivo = "carros/" + info[: len(info) - 3] + ".txt"
        print(
            f"\nAtendente {atendente.nome}:\nDentro da classe de carros {info[:len(info)-3]} temos as seguintes opções: "
        )
        with open(arquivo, "r") as file:
            temp = (file.read()).split("/")
            count = 0
            for i in temp:
                count += 1
                i = i.split(",")
                print(f"{count} - {i[0]}, R${i[1]},00 por dia")
            aux = [str(i + 1) for i in range(count)]
            ordem = input("Informe o desejado: ")
            while ordem not in aux:
                ordem = input(f"Essa resposta '{ordem}' é inválida. Insira novamente: ")
            self.carro = (
                temp[int(ordem) - 1] + ";" + info[-3:] + ";" + info[: len(info) - 3]
            )


def decideCaminho():
    pergunta = input(
        "Insira o caminho que deseja seguir:\n1 - Gerente 2 - Caixa\nX - Terminar\nInsira sua resposta: "
    )
    respostas = ["1", "2", "X"]
    if not (pergunta.isnumeric()):
        pergunta = pergunta.upper()
    while pergunta not in respostas:
        pergunta = input(f"Essa resposta '{pergunta}' não é válida. Insira outra: ")
    if pergunta == "X":
        print("\nObrigado por testar o sistema.")
        return pergunta
    return int(pergunta)


c1 = Cliente()
a1 = Atendente()
c1.setTipoDeCarro(a1)
c1.setCarro(a1)
ca1 = Caixa()
ca1.checaCliente(c1)
ca1.setgetPreco(c1)
c1.fimDaTela()
g1 = Gerente()
while True:
    aux = decideCaminho()
    if aux == 1:
        print(f"""\n{'-='*5}TELA DE GERENTE({g1.nome}){'-='*5}""")
        pergunta = input(
            f"Você deseja:\n1 - Informações dos funcionários 2 - Demitir o atendente {a1.nome}\nInsira: "
        )
        if pergunta == "1":
            g1.getInfos(a1, ca1)
        else:
            g1.ger_Demitir(a1)
    if aux == 2:
        print(f"""\n{'-='*5}TELA DE CAIXA{'-='*5}""")
        pergunta = input("Você deseja:\n1 - Salário dos colaboradores\nInsira: ")
        if pergunta == "1":
            ca1.getSalarios(g1, a1)
    if aux == "X":
        break
