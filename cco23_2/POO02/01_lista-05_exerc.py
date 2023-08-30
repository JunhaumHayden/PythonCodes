#Crie a seguinte hierarquia de classes:
#• Uma interface para representar qualquer forma geométrica, definindo métodos para cálculo do perímetro e cálculo da área da forma;
#• Uma classe abstrata para representar quadriláteros. Seu construtor deve receber os tamanhos dos 4 lados e o método de cálculo do #perímetro já pode ser implementado;
#• Classes para representar retângulos e quadrados. A primeira deve receber o tamanho da base e da altura no construtor, enquanto a #segunda deve receber apenas o tamanho do lado;
#• Uma classe para representar um círculo. Seu construtor deve receber o tamanho do raio.
#No programa principal, pergunte ao usuário quantas formas ele deseja criar. Em seguida, para cada forma, pergunte se deseja criar um #quadrado, um retângulo ou um círculo, solicitando os dados necessários para criar a forma. Todas as formas criadas devem ser #rmazenadas em um vetor. Finalmente, imprima: (a) os dados (lados ou raio); (b) os perímetros; e (c) as áreas de todas as formas.





from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_perimetro(self):
        pass
    
    @abstractmethod
    def calcular_area(self):
        pass


class Quadrilatero(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4
        
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3 + self.lado4


class Retangulo(Quadrilatero):
    def __init__(self, base, altura):
        super().__init__(base, altura, base, altura)
        
    def calcular_area(self):
        return self.lado1 * self.lado2


class Quadrado(Quadrilatero):
    def __init__(self, lado):
        super().__init__(lado, lado, lado, lado)
        
    def calcular_area(self):
        return self.lado1 ** 2


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)


def main():
    formas = []
    num_formas = int(input("Quantas formas você deseja criar? "))
    
    for _ in range(num_formas):
        tipo = input("Qual forma você deseja criar? (quadrado/retangulo/circulo) ").lower()
        if tipo == "quadrado":
            lado = float(input("Digite o tamanho do lado: "))
            forma = Quadrado(lado)
        elif tipo == "retangulo":
            base = float(input("Digite o tamanho da base: "))
            altura = float(input("Digite o tamanho da altura: "))
            forma = Retangulo(base, altura)
        elif tipo == "circulo":
            raio = float(input("Digite o tamanho do raio: "))
            forma = Circulo(raio)
        else:
            print("Tipo de forma inválido. Tente novamente.")
            continue
        
        formas.append(forma)
    
    for i, forma in enumerate(formas, start=1):
        print(f"Forma {i}:")
        print("Perímetro:", forma.calcular_perimetro())
        print("Área:", forma.calcular_area())
        print()

# Chama o método main
main()
