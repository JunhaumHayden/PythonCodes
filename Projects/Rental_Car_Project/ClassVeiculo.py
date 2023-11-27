class Veiculo():
    def __init__(self, modelo, categoria):
        self.modelo = modelo
        self.categoria = categoria
    
    def calcular_tarifa(self):
        pass

    def calcular_seguro(self):
        if self.categoria == "sedan":
            return 100
        elif self.categoria == "SUV":
            return 150
        elif self.categoria == "compacto":
            return 80
        else:
            return 0

class Sedan(Veiculo):
    def calcular_tarifa(self):
        return 100

class SUV(Veiculo):
    def calcular_tarifa(self):
        return 150

class Compacto(Veiculo):
    def calcular_tarifa(self):
        return 80
    

