#Lista de Exercircio 01 - Aula 02
#Estrutura Sequencial

#PROBLEM 1003
#Ler dois inteiros e realizar a soma

#a = int(input("Digite um valor: "))
#b = int(input("Digite outro valor: "))

#soma = a+b
#print("A soma entre os valores é:" , soma)

#PROBLEM 1004
#Ler dois inteiros e realizar a multiplicação

#a = int(input("Digite um valor: "))
#b = int(input("Digite outro valor: "))

#prod = a*b
#print("O produto entre os valores é:" , prod)


#PROBLEM 1005
#Ler dois numeros decimais e realizar a média

#a = float(input("Digite a primeira nota: "))
#b = float(input("Digite a segunda nota: "))

#media = ((a*3.5)+(b*7.5))/11
#print("A média é {:.5f}:".format(media))

#PROBLEM 1006
#Ler três numeros decimais e realizar a média

#a = float(input("Digite a primeira nota: "))
#b = float(input("Digite a segunda nota: "))
#c = float(input("Digite a terceira nota: "))

#media = ((a*2)+(b*3)+(c*5))/10
#print("A média é {:.1f}:".format(media))

#PROBLEM 1006
#Ler três numeros decimais e realizar a média

#a = float(input("Digite a primeira nota: "))
#b = float(input("Digite a segunda nota: "))
#c = float(input("Digite a terceira nota: "))

#media = ((a*2)+(b*3)+(c*5))/10

#PROBLEM 1007
#Ler quatro numeros inteiros e calcular a diferença do produto entre A e B com o produto entre C e D

# a = int(input("Digite a primeiro numero: "))
# b = int(input("Digite a segundo numero: "))
# c = int(input("Digite a terceir0 numero: "))
# d = int(input("Digite a quarto numero: "))

# media = (a * b - c * d)
# print("DIFERENCA = ", media)
    
#PROBLEM 1008
#Ler o número de um funcionário, seu número de horas trabalhadas 
# em um mês e o valor que ele recebe por hora. Imprima o número do 
# funcionário e o salário que ele receberá no final do mês, com duas casas 
# decimais.

# a = int(input("Digite o número do funcionário: "))
# b = int(input("Digite o número de horas trabalhadas: "))
# c = float(input("Digite o valor por hora trabalhada: "))


# salary = (b * c)
# print("NUMBER = ", a)
# print("SALARY = U$", salary)

#PROBLEM 2374
#Escreva um programa que, dada a pressão desejada digitada pelo 
#motorista e a pressão do pneu lida pela bomba, indica a diferença 
#entre a pressão desejada e a pressão lida.

# n = int(input("Digite a pressão desejada: "))
# m = int(input("Ler a pressão da bomba: "))

# pressao = (n - m)
# print(pressao)

#PROBLEM 2413
#Escreva um programa que, dada a pressão desejada digitada pelo 
#motorista e a pressão do pneu lida pela bomba, indica a diferença 
#entre a pressão desejada e a pressão lida.

# n = int(input("Digite número de pessoas que clicaram no terceiro link da busca: "))

# link = ((n * 2) * 2)
# print(link)

#PROBLEM 1012
#Area 

# a = float(input("Digite o valor de A: "))
# b = float(input("Digite o valor de B: "))
# c = float(input("Digite o valor de C: "))
# PI = 3.14159


# triangulo = (a*c)/2
# circulo = PI*c**2
# trapezio = ((a+b)*c)/2
# quadrado = b**2
# retangulo = a*b

# print(f"TRIANGULO : {triangulo:,.3f}")
# print(f"CIRCULO : {circulo:,.3f}")
# print(f"TRAPEZIO : {trapezio:,.3f}")
# print(f"QUADRADO : {quadrado:,.3f}")
# print(f"RETANGUL : {retangulo:,.3f}")

#PROBLEM 1020
#Age in Days

# dias = int(input("Digite a quantidade de dias: "))

# anos = int(dias/365)
# dias -= anos*365

# meses = int(dias/30)
# dias -= meses*30

# print(f"{anos} ano(s)")
# print(f"{meses} mes(es)")
# print(f"{dias} dia(s)")

#PROBLEM 1015
#Distance Between Two Points

# x1 = float(input("Digite valor de x1: "))
# y1 = float(input("Digite valor de y1: "))
# x2 = float(input("Digite valor de x2: "))
# y2 = float(input("Digite valor de y2: "))         

# distancia = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
# print(f"{distancia:0.4f}")

#PROBLEM 1019
#Time Conversion

# seg = int(input("Digite valor em segundos: "))

# min = int(seg/60)
# seg -= min*60
# horas = int(min/60)
# min -= horas*60

# print(f"{horas}:{min}:{seg}")

#PROBLEM 1019
#Fuel Spent

# t = int(input("Digite o tempo de viagem em horas: "))
# v = int(input("Digite a velocidade media em Km/h: "))

# litro = (v*t)/12
# print(f"{litro:.3f}")

#PROBLEM 1019
#Fuel Spent

# distancia = int(input("Digite a distancia em Km: "))
# combustivel = float(input("Digite a quantidade de combustivel gasto: "))

# consumo = distancia / combustivel
# print(f"{consumo:.3f} km/l")

#PROBLEM 1019
#Fuel Spent

# nome = input("Digite o nome: ")
# sal = float(input(f"Digite o salario de {nome}: "))
# vendas = float(input(f"Digite o total de vendas de {nome}: "))

# bonus = float(vendas * (15/100))

# total = sal + bonus

# print(f"TOTAL = R$ {total:.2f}")

