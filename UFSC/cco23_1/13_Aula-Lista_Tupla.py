##Aluno: Carlos Benedito Hayden de Albuquerque Junior
##matricula: 23100455
##Lista de Exercicios Lista e Tupla


# print("="*30)
# print("    Questao 01")
# print("="*30)

# alunos=[]

#     #Funcao para solicitar as nums e checar os valores das nums atraves
#     # do laco de repetição while com o paremetro True
# def check_nums():
#     while True:
#         num= int(input("Informe a num: "))
#             #Teste do valor da num com a estrutura condicional IF
#         if 0 <= num <= 10:
#                 #Caso a condicao retorne true retorna o 
#                 # valor da variavel num e finaliza o laço
#             return(num)
#             break
#         else:
#                 #Caso retorne false informa o erro e repete o laço
#             print("num não esta entre 0 e 10, Digite novamente: ")
# #main
#     #Inicia-se solicitando onumero de vezes que será entrado com os dados
# n = int(input("Informe a quatidade de alunos: "))

#     #laco de repeticao com FOR para repetir de acordo com o valor 
#     # na variavel n
# for i in range(n):
#     nome = input("Digite o nome do aluno {}: ".format(i+1))
#         #Para cada entrada de nums faz-se uma chamada na funcao 
#         # check_nums e cada num é armazenada em uma variavel
#     num1 = (check_nums())
#     num2 = (check_nums())
#     num3 = (check_nums())
#         #Adiciona-se os valores das variaveis na lista alunos 
#         # com a funcao .append e passando os todos valores em 
#         # como uma unica lista a cada iteracao
#     alunos.append((nome, num1, num2, num3))
    

#     #Laco de repeticao com FOR para iterar sobre a lista alunos
#     #A cada iteracao ira atribuir o primeiro elemento da lista
#     # a variavel nome e os demais a lista nums
# for aluno in alunos:
#     nome = aluno[0]
#     nums = aluno[1:]
#     # Calcula a média das nums do aluno
#     media = sum(nums) / len(nums)
        
#      # Encontra a maior e a menor num do aluno
#      #Estacia-se duas variaveis auxiliares que 
#      # receberam o primeiro elemento da lista nums
#     maior_num = nums[0]
#     menor_num = nums[0]
#      #Laco de repeticao com FOR para iterar sobre a lista nums
#      # o indice num recebe os elementos da lista nums
#     for num in nums:
#          #Estrutura consicional para verificar se o elemnto percorrido 
#          # pelo FOR e maior ou menor que o da variavel e caso retorne 
#          # TRUE altera o valor das variaveis 
#         if num > maior_num:
#             maior_num = num
#         if num < menor_num:
#             menor_num = num
    
         
#         # Calcula a diferença entre a maior e a menor num
#     diferenca = maior_num - menor_num
    
#         # Imprime os resultados para o aluno
#     print("Aluno: {}".format(nome))
#     print("Média: {:.2f}".format(media))
#     print("Maior num: {:.2f}".format(maior_num))
#     print("Menor num: {:.2f}".format(menor_num))
#     print("Diferença entre a maior e a menor num: {:.2f}".format(diferenca))
#     print()

# print("="*30)
# print("    Programa encerrado!")
# print("="*30)
    
##Lista de Exercicios Lista e Tupla
##Questão 02


# print("="*30)
# print("    Questao 02")
# print("="*30)   

# # Declara-se variáveis globais
# nums = []
# # Laco de repeticao com WHILE 
# # para receber os valores do usuario e 
# # inserir na lista nums. 
# # Criterio de parada 0 (ZERO)
# while True:
#     num = int(input("Digite um número inteiro (Zero para encerrar): "))
#     if num == 0:
#         break
#     else:
#         nums.append(num)
#  # Variavel auxiliar para marcar se há repetição ou não.
#  # Recebe valor inicial FALSE e caso encontre valor 
#  # repetido recebe o valor TRUE
# repetidos = False
#  #Laco de repeticao com FOR para percorrer a lista nums
# for i in range(len(nums)):
#      # Laco de repeticao com FOR para 
#      # percorre a lista apartir da posicao 
#      # atual do elemento (i + 1) da lista nums em que o loop 
#      # FOR anterior (com variavel de indice i) esta.
#     for j in range(i+1, len(nums)):
#          #Estrutura condicional com IF para 
#          # comparar o valor do elemento de indice i (elemento atual 
#          # do FOR com variavel de indice i) com os elementos a 
#          # direita da lista numero (elemento percorrido pelo FOR 
#          # de indice j)
#         if nums[i] == nums[j]:
#             repetidos = True
#             break

# if repetidos:
#     print()
#     print("*"*40)
#     print("  Há números repetidos na lista.")
#     print("*"*40)       
# else:
#     print()
#     print("*"*40)
#     print("  Não há números repetidos na lista.")
#     print("*"*40)
# print("="*30)
# print("    Programa encerrado!")
# print("="*30)


##Lista de Exercicios Lista e Tupla
##Questão 03


# print("="*30)
# print("    Questao 03")
# print("="*30)   

# nums = (12, 5, 9, 4, 7, 15, 8, 20, 11, 2)

# def index1():
#     maior_num = nums[0]
#     maior_pos = 0
#     menor_num = nums[0]
#     menor_pos = 0

#     for num in nums:
            
#         if num > maior_num:
#             maior_num = num
#             maior_pos = nums.index(num)
#         if num < menor_num:
#             menor_num = num
#             menor_pos = nums.index(num)
#     print(f"Metodo 01 o Maior é : {maior_pos}")
#     print(f"Metodo 01 o Menor é : {menor_pos}")
#     print()
 
# def index2():
#     maior = 0
#     for i in range(len(nums)):
#         if nums[i] > nums[maior]:
#             maior = i

    
#     menor = 0
#     for i in range(len(nums)):
#         if nums[i] < nums[menor]:
#             menor = i

    
#     print(f'Metodo 02 o maior número é {nums[maior]} e está na posição {maior}.')
#     print(f'Metodo 02 o menor número é {nums[menor]} e está na posição {menor}.')



# metodo1 = index1()
# metodo2 = index2()

# print("="*30)
# print("    Programa encerrado!")
# print("="*30)


##Lista de Exercicios Lista e Tupla
##Questão 04


# print("="*30)
# print("    Questao 04")
# print("="*30) 

# N = int(input("Digite o tamanho da lista: "))
# X = []

# for i in range(N):
#     num = int(input("Digite um número: "))
#     X.append(num)

# K = int(input("Digite um número para multiplicar pelos elementos de X: "))

#  # Criar uma nova lista contendo o resultado da multiplicação 
#  # de cada elemento num da lista X por K.

#  # A estrutura básica de uma list comprehension é a seguinte:
#  # nova_lista = [expressão for elemento in lista_original]
#  # Nesse caso específico, a expressão é num*K ou seja, o elemento 
#  # original da lista X multiplicado por K. O FOR indica que essa 
#  # expressão deve ser aplicada a cada elemento num de X. Por fim, a lista 
#  # resultante é criada com todos os valores calculados pela expressão.
# lista_resultante = [num*K for num in X]

# print("Lista resultante:", lista_resultante)

# print("="*30)
# print("    Programa encerrado!")
# print("="*30)


##Lista de Exercicios Lista e Tupla
##Questão 05


# print("="*30)
# print("    Questao 05")
# print("="*30) 

# X = list(range(20))  # cria a lista X com valores de 0 a 19
# print("Lista original:", X)

# # trocando as posições
# for i in range(len(X)//2):
#     aux = X[i]
#     X[i] = X[len(X)-i-1]
#     X[len(X)-i-1] = aux

# print("Lista após a troca:", X)

# print("="*30)
# print("    Programa encerrado!")
# print("="*30)


##Lista de Exercicios Lista e Tupla
##Questão 06


print("="*30)
print("    Questao 06")
print("="*30) 

saltos = []

while True:
    nome = input("Nome do atleta: ")
    aux = nome.upper()
    if aux == 'O':
        break
    
    print("Digite os resultados dos saltos de", nome)
    
    for i in range(5):
        salto = float(input("Salto {}: ".format(i+1)))
        saltos.append(salto)
    
    saltos.sort()
    
    print("Saltos:", saltos)
    print("Melhor salto:", saltos[-1], "m")
    print("Pior salto:", saltos[0], "m")
    media = sum(saltos[1:4])/3
    print("Média dos demais saltos:", round(media, 2), "m")
    
    print("Resultado final:")
    print(nome, ":", round(media, 2), "m")
    
    saltos = [] # limpa a lista de saltos para o próximo atleta


print("="*30)
print("    Programa encerrado!")
print("="*30)