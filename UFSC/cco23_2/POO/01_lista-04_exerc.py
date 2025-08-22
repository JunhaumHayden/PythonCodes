#Crie uma classe de Teste com o método main. Neste método:
#• Crie um assistente administrativo e um técnico. 
#Imprima o número de matrícula e o nome de cada um deles.
#• Crie um ingresso. Peça para o usuário digitar 1 para normal e 2 para VIP. Conforme a escolha do usuário, diga se o ingresso é do #tipo normal ou VIP. Se for VIP, peça para ele digitar 1 para camarote superior e 2 para camarote inferior. Conforme a escolha do #usuário, diga se que o VIP é camarote superior ou inferior. Imprima o valor do ingresso.
#• crie um imóvel. Peça para o usuário digitar 1 para novo e 2 para velho. Conforme a definição do usuário, imprima o valor final #do imóvel.

class Assistente:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
    
    def exibeDados(self):
        print("Matrícula:", self.matricula)
        print("Nome:", self.nome)


class Tecnico(Assistente):
    def __init__(self, matricula, nome):
        super().__init__(matricula, nome)
        

class Administrativo(Assistente):
    def __init__(self, matricula, nome, turno, adicional_noturno):
        super().__init__(matricula, nome)
        self.turno = turno
        self.adicional_noturno = adicional_noturno
    
    def exibeDados(self):
        super().exibeDados()
        print("Turno:", self.turno)
        print("Adicional Noturno:", self.adicional_noturno)


class Ingresso:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def imprimeTipo(self):
        if self.tipo == 1:
            print("Ingresso: Normal")
        elif self.tipo == 2:
            print("Ingresso: VIP")


class VIP(Ingresso):
    def __init__(self, tipo, camarote):
        super().__init__(tipo)
        self.camarote = camarote
    
    def imprimeTipo(self):
        super().imprimeTipo()
        if self.camarote == 1:
            print("Tipo: Camarote Superior")
        elif self.camarote == 2:
            print("Tipo: Camarote Inferior")


class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo
        self.preco = 0
    
    def calculaPreco(self):
        if self.tipo == 1:
            self.preco = 150000
        elif self.tipo == 2:
            self.preco = 100000


class Novo(Imovel):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.calculaPreco()
        self.adicional = 20000
    
    def imprimePreco(self):
        print("Preço Final:", self.preco + self.adicional)


class Velho(Imovel):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.calculaPreco()
        self.desconto = 0.15 * self.preco
    
    def imprimePreco(self):
        print("Preço Final:", self.preco - self.desconto)


class Teste:
    @staticmethod
    def main():
        matricula_tecnico = input("Digite a matrícula do Técnico: ")
        nome_tecnico = input("Digite o nome do Técnico: ")
        tecnico = Tecnico(matricula_tecnico, nome_tecnico)
        print("Técnico:")
        tecnico.exibeDados()
        
        matricula_administrativo = input("Digite a matrícula do Administrativo: ")
        nome_administrativo = input("Digite o nome do Administrativo: ")
        turno_administrativo = input("Digite o turno do Administrativo (dia/noite): ")
        adicional_noturno = input("Digite o adicional noturno do Administrativo: ")
        administrativo = Administrativo(matricula_administrativo, nome_administrativo, turno_administrativo, adicional_noturno)
        print("Administrativo:")
        administrativo.exibeDados()
        
        tipo_ingresso = int(input("Digite 1 para Normal ou 2 para VIP: "))
        ingresso = None
        if tipo_ingresso == 1:
            ingresso = Ingresso(tipo_ingresso)
        elif tipo_ingresso == 2:
            tipo_camarote = int(input("Digite 1 para Camarote Superior ou 2 para Camarote Inferior: "))
            ingresso = VIP(tipo_ingresso, tipo_camarote)
        print("Ingresso:")
        ingresso.imprimeTipo()
        
        tipo_imovel = int(input("Digite 1 para Novo ou 2 para Velho: "))
        imovel = None
        if tipo_imovel == 1:
            imovel = Novo(tipo_imovel)
        elif tipo_imovel == 2:
            imovel = Velho(tipo_imovel)
        print("Imóvel:")
        imovel.imprimePreco()


# Chama o método main da classe de Teste
Teste.main()
