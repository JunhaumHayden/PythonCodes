##Aluno: Carlos Benedito Hayden de Albuquerque Junior
##matricula: 23100455
##Questao 03

# Utilizar função (sem o uso do return). 
# Faça um programa que contenha duas funções: 
# 1) Uma função chamada soma(inicio, fim), que receba 2 parâmetros: início, fim. 
# Estes valores representam os limites de um intervalo. 
# Esta função deve calcular a soma dos valores do intervalo indicado (incluindo os 
# valores início e fim). 
# 2) Uma função chamada subtracao(a,b), que receba dois parâmetros: a , b. 
# Esta função deve verificar qual dos 2 valores recebidos como parâmetro é o maior 
# e calcular a diferença entre o maior e o menor. 
# Os valores calculados pelas funções devem ser impressos. 
# Condição de parada: deve ser perguntado ao usuário se deseja continuar executando o 
# programa. 
# Exemplos: 
# Digite o intervalo: 3 7 Soma do intervalo = 25 
# Digite 2 valores: 20 30 Diferença = 10 
# Deseja continuar? S 
# Digite o intervalo: 1 2 Soma do intervalo = 3 
# Digite 2 valores: 4 67 Diferença = 63 
# Deseja continuar? N 


print("="*30)
print("    Questao 03")
print("="*30)

def soma(inicio, fim):
    soma = 0
    fim += 1 # +1 para o FOR somar o ultimo elemento
    for i in range(inicio,fim):
        #print(i)
        soma = soma + i
    print(soma)
        
def subtracao(a,b):
    if a<b:
        aux = b
        b = a
        a = aux
    print(a - b)

while True:
    
    soma1, soma2 = map(int, input("Informe o intervalo: ").split())
    #soma2= int(input("Informe o segundo numero da soma: "))
    total_soma = soma(soma1, soma2)
    total_soma


    sub1, sub2 = map(int,input("Informe dois valores: ").split())
#sub2= int(input("Informe o segundo numero da subtracao: "))
    total_subtra = subtracao(sub1, sub2)
    total_subtra
    continuar = input("Deseja continuar? (S/N) ")
    if continuar.upper() != "S":
        break
   
print("="*30)
print("    Fim do programa")
print("="*30)    
