#Item01 & 02 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os em ordem, na ordem inversa, armazene os
#Item05 - números pares no vetor PAR e os números IMPARES no vetor impar e os numeros primos.
#Item07 - que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import random
import math

def ler_vetor_manual():
    vetor = []
    print("Digite os números inteiros:")
    for i in range(5):
        numero = int(input(f"Digite o {i + 1}º número inteiro: "))
        vetor.append(numero)
    return vetor

def gerar_vetor_aleatorio():
    vetor = [random.randint(1, 100) for _ in range(5)]
    return vetor

def mostrar_vetor(vetor):
    print("Os números no vetor são:")
    for num in vetor:
        print(num)

def mostrar_vetor_inverso(vetor):
    print("Os números no vetor, na ordem inversa, são:")
    for i in range(len(vetor) - 1, -1, -1):
        print(vetor[i])

def separar_pares_impares(vetor):
    pares = []
    impares = []
    for num in vetor:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

def is_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = math.isqrt(num) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

def separar_primos(vetor):
    primos = [num for num in vetor if is_primo(int(num))]
    return primos

def calcular_soma(vetor):
    result = 0
    for num in vetor:
        result += num
    return result
    #return sum(vetor) #Simplificando codigo com a funcao sum

def calcular_multiplicacao(vetor):
    result = 1
    for num in vetor:
        result *= num
    return result

def calcular_soma_quadrados(vetor):
    soma_quadrados = sum(num ** 2 for num in vetor)
    return soma_quadrados

#Funcao auxiliar para apresentacao dos menus
def printing(msg):
    print("="*30)
    print(f"{msg}")
    print("="*30)
    print( )

# Função principal
def main():
    print("Escolha uma opção:")
    print("1. Informar os números manualmente")
    print("2. Gerar números automaticamente")
    
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        vetor = ler_vetor_manual()
    elif opcao == 2:
        vetor = gerar_vetor_aleatorio()
    else:
        print("Opção inválida. Encerrando o programa.")
        return
    

    printing('Apresentando Vetor')
    mostrar_vetor(vetor)

    printing('Ordem Inversa')
    mostrar_vetor_inverso(vetor)

    printing('Pares e impares')
    par , impar = separar_pares_impares(vetor)
    print('Numeros pares da lista:\n', par)
    print('Numeros pares da lista:\n', impar)

    printing('Numeros primos:')
    primos = separar_primos(vetor)
    print(primos)

    print("Soma dos números:", calcular_soma(vetor))
    print("Multiplicação dos números:", calcular_multiplicacao(vetor))

    printing('Soma dos Quadrados:')
    print("Vetor:", vetor)
    print("Soma dos quadrados dos elementos:", calcular_soma_quadrados(vetor))


if __name__ == "__main__":
    main()
