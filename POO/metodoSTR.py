class Bicicleta:
    def __init__(self, cor, modelo, valor):
        self.cor = cor
        self.modelo = modelo
        self.valor = valor

    # #ToString manual
    # def __str__(self) -> str:
    #     return f"Bicileta: cor = {self.cor}, modelo = {self.modelo}, valor = {self.valor}"
    #ToString automatizado   
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    # ''.join() para o separador da lista
    # ListComprheension para interar sobre o dicionario
    

b1 = Bicicleta("red", "caloi", "2000")
print(b1)