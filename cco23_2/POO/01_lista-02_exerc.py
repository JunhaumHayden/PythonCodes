#Crie uma classe chamada Ingresso que possui um valor em reais e um método imprimeV alor().
#• Crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso VIP (com o #adicional incluído).
#• Crie uma classe Normal, que herda Ingresso e possui um método que imprime: "Ingresso Normal".
#• Crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos para acessar e imprimir esta localização) e uma #classe CamaroteSuperior, que é mais cara (possui valor adicional). Esta última possui um método para retornar o valor do ingresso. #Ambas as classes herdam a classe VIP.


class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    
    def imprimeValor(self):
        print("Valor do Ingresso:", self.valor)


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional
    
    def valorIngressoVIP(self):
        return self.valor + self.adicional


class Normal(Ingresso):
    def imprimeTipo(self):
        print("Ingresso Normal")


class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao
    
    def imprimeLocalizacao(self):
        print("Localização:", self.localizacao)


class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao
    
    def valorIngressoCamaroteSuperior(self):
        return self.valorIngressoVIP()
    
    def imprimeLocalizacao(self):
        print("Localização:", self.localizacao)


# Exemplo de uso
ingresso_normal = Normal(50)
ingresso_normal.imprimeValor()
ingresso_normal.imprimeTipo()

ingresso_vip = VIP(70, 20)
print("Valor do Ingresso VIP:", ingresso_vip.valorIngressoVIP())

camarote_inferior = CamaroteInferior(100, 30, "Inferior Leste")
camarote_inferior.imprimeLocalizacao()
print("Valor do Ingresso Camarote Inferior:", camarote_inferior.valorIngressoVIP())

camarote_superior = CamaroteSuperior(120, 40, "Superior Oeste")
camarote_superior.imprimeLocalizacao()
print("Valor do Ingresso Camarote Superior:", camarote_superior.valorIngressoCamaroteSuperior())
