#Item04 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram
#lidas. Imprima as consoantes.

import random

def gerar_vetor_caracteres():
    letras = 'abcdefghijklmnopqrstuvwxyz'
    vetor = [random.choice(letras) for _ in range(10)]
    return vetor

def contar_consoantes(vetor):
    consoantes = [char for char in vetor if char.lower() not in 'aeiou']
    return len(consoantes), consoantes

# Função principal
def main():
    vetor = gerar_vetor_caracteres()
    print("Vetor de caracteres:", vetor)

    total_consoantes, consoantes = contar_consoantes(vetor)
    
    print("Total de consoantes lidas:", total_consoantes)
    print("Consoantes:", ', '.join(consoantes))

if __name__ == "__main__":
    main()
