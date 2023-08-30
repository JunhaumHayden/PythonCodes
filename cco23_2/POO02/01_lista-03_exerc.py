#Crie a classe Imóvel, que possui um endereço e um preço.
#• Crie uma classe Novo, que herda Imovel e possui um adicional no preço. 
#Crie métodos de acesso e impressão deste valor adicional.
#• Crie uma classe Velho, que herda Imovel e possui um desconto de 15% no preço. 
#Crie métodos de acesso e impressão para este desconto.



class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco
    
    def imprimeInfo(self):
        print("Endereço:", self.endereco)
        print("Preço:", self.preco)


class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional
    
    def getAdicional(self):
        return self.adicional
    
    def imprimeAdicional(self):
        print("Adicional:", self.adicional)


class Velho(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)
        self.desconto = 0.15 * preco
    
    def getDesconto(self):
        return self.desconto
    
    def imprimeDesconto(self):
        print("Desconto:", self.desconto)


# Exemplo de uso
imovel_novo = Novo("Rua A, 123", 150000, 20000)
imovel_novo.imprimeInfo()
imovel_novo.imprimeAdicional()

imovel_velho = Velho("Rua B, 456", 100000)
imovel_velho.imprimeInfo()
imovel_velho.imprimeDesconto()
