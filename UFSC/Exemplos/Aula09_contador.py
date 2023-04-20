"""
Exerc 13)
Faça um programa que tenha uma função chamada contador(),
que tenha 3 parâmetros: inicio, fim e passo, e realize a contagem.
Seu programa terá que realizar 3 contagens através da função criada.
a) 1 a 10 de 1 em 1
b) 10 a 0 de 2 em 2
c) uma contagem personalizada
"""

def contador(i,f,p):
    print(f"Contagem de {i} até {f} de {p} em {p}.")
    
    if (p < 0) :
        p *= -1
    
    if (p==0):
        p=1
        
    if i<f:
        cont = i
        while (cont <= f):
            print(f"{cont}",end=" ")
            cont += p
        print(" Fim! ")
    else:
        cont = i
        while (cont >= f):
            print(f"{cont}",end=" ")
            cont -= p
        print(" Fim! ")
    
#programa principal
contador(1,10,1)
contador(10,0,2)
print("Contagem personalizada: ")
ini,fim, pas = [int(x) for x in input("Digite inicio, fim e passo: ").split()]
contador(ini,fim,pas)
