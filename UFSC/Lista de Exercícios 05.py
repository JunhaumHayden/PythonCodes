#    #Estruturas de Repetição (Revisão IF, FOR, WHILE)
#    #Aula 27/03/2023
    
     #Exercício 1099

# #############################################################################    
#    #Lista de Exercícios 05
# #1 - beecrowd | 1113
# #Ascending and Descending

#print("="*40)
#print("      Ascending and Descending")
#print("="*40)

#Entrada para verificação
#n1 = int(input("digite o primeiro numero: "))
#n2 = int(input("digite o segundo numero: "))

#if n1 > n2:
#    print("Decrescente")
#elif n1 < n2:
#    print("Crescente")
#else:
#    print("São iguais")

# #############################################################################
#  #2 beecrowd | 1099
# #Sum of Consecutive Odd Numbers II

# print("="*50)
# print("      Sum of Consecutive Odd Numbers II")
# print("="*50)

# #Entrada para verificação: numero de vezes que se repetirá
# n = int(input("digite o numero de testes a realizar: "))

# #Utilizando laço de repetição FOR para repetir o numero de vez da variavel n atraves da função range
# for i in range(n):
#     #Entrada para verificação do intervalo de análise
#     x, y = map(int, input("digite os numeros para o teste: ").split())

#     # Para garantir que x seja sempre o menor número
#     if x > y:
#         x, y = y, x #Caso x seja maior troca os valores

#     soma = 0 #instancia uma variavel para receber a soma dos numeros impares
#     for j in range(x+1, y): #utiliza um laço de repetição FOR para percorrer o intervalo através da função range
#         if j % 2 != 0: #Condição para numero impar através do resto diferente de 0 da divisão por 2
#             soma += j #Soma o numero impar a variavel soma

#     print(soma)

# #############################################################################
#  #3 - beecrowd | 1021
# #Carnaval

# print("="*40)
# print("      Carnaval")
# print("="*40)


# #Entrada para verificação
# valor = float(input("Informe o valor: "))
# #Converte valor para centavos
# centavos = int(valor * 100)
# #Variaveis com os valores das notas e moedas em centavos
# notas = [10000, 5000, 2000, 1000, 500, 200]
# moedas = [100, 50, 25, 10, 5, 1]

# print("NOTAS:")
# #Laço de repetição com FOR para percorrer a variavel notas 
# # e cada iteração passará para o proximo valor
# for nota in notas: 
#     #variavel que vai receber a divisão inteira do valor de entrada (em centavos) 
#     # pelo valor de cada nota 
#     quantidade = centavos // nota 
#     #para atualizar o valor restante (subtrair o valor da nota a cada iteração)
#     centavos -= quantidade * nota
#     print("{} nota(s) de R$ {:.2f}".format(quantidade, nota/100))
#     #Laço finaliza na ultima nota

#     #Laço identico ao de cima com o valor para os centavos
# print("MOEDAS:")
# for moeda in moedas: #Laço de repetição com FOR para percorrer a quantidade de moedas
#     quantidade = centavos // moeda
#     centavos -= quantidade * moeda
#     print("{} moeda(s) de R$ {:.2f}".format(quantidade, moeda/100))

#############################################################################
 #beecrowd | 1247
#Coast Guard

#print("="*40)
#print("      Stop thief! Stop thief!")
#print("="*40)

##Entrada para verificação: 3 numeros inteiros

    
#D, VF, VG = map(int, input("Informe:\n Distancia entre o fugitivo e a Guarda: \n Velocidade do fugitivo: \n Velocidade da Guarda: \n(separados por espaços): ").split())



    #Calculo da distância ate a interceptação com o fugitivo
#distancia_fugitivo = ((D ** 2) + 144) ** 0.5
    
    #calculo do tempo do fugitivo até o limite de aguas internacionais
#tempo_fugitivo = 12 / VF
    
    #Calculo do tempo da guarda até o ponto de interceptação com o fugitivo
#tempo_guarda = distancia_fugitivo / VG

    #Condição de verificação do tempo de deslocamento usando IF para comparar os tempos
#if tempo_guarda <= tempo_fugitivo:
#    print("S")
#else:
#    print("N")
    
# #############################################################################
#  #beecrowd | 1708
# #Lap

# print("="*30)
# print("      Final Lap")
# print("="*30)

# #Loop de repetição com while para verificar as entradas
# while True:
   
#      x, y = map(int, input("Informe o tempo em segundos, do piloto 1 e 2: ").split())
#      #Teste com IF para verificar se o tempo informado esta dentro da faixa
#      if 1 <= x < y <= 10000:
#           #Caso esteja, este loop é interrompido
#           break
#      else:
#           #Caso não esteja, pede-se para digitar novamente
#           print("Valores fora da faixa permitida. Tente novamente.")
    
# #Declara-se uma variavel para receber o numero de voltas
# lap = 1
# #Loop de repetição com while para verificar a diferença de tempo entre os pilotos
# #Caso a diferença de tempo entre o piloto 2 e o piloto 1 seja menor que o tempo que o 
# # piloto 1 leva para dar uma volta no circuito, incrementa a variavel lap e 
# # verifica-se novamente a diferença de tempo entre os pilotos
# while (y * lap) - (x * lap) < x:

#     lap += 1
# #Caso a diferença de tempo entre os dois pilotos seja maior que o tempo que o piloto 1 
# # leva para dar uma volta o loop é interropido e 
# # imprimi-se o numero da volta.
# print(f"O piloto 1 ultrapassou o piloto 2 na volta {lap}")


# #############################################################################
# #beecrowd | 2418
# #Carnaval

# print("="*30)
# print("      Carnaval")
# print("="*30)

# while True:
   
#      n1, n2, n3, n4, n5 = map(float, input("Informe as notas da agremiação: ").split())
#      #Teste com IF para verificar se os valores informados esta dentro da faixa
#      if 5.0 <= n1 <= 10.0:
#           if 5.0 <= n2 <= 10.0:
#               if 5.0 <= n3 <= 10.0:
#                   if 5.0 <= n4 <= 10.0:
#                       if 5.0 <= n5 <= 10.0:
#                         #Caso estejam, este loop é interrompido
#                         break
#      else:
#           #Caso não estejam, pede-se para digitar novamente
#         print("Valores fora da faixa permitida. Tente novamente.")
 

# menor = min(n1, n2, n3, n4, n5)
# maior = max(n1, n2, n3, n4, n5)
# soma = n1 + n2 + n3 + n4 + n5
# #teste com IF para o menor valor
# if menor == n1:
#     soma = soma - menor
#     menor = min(n2, n3, n4, n5)
# elif menor == n2:
#     soma = soma - menor
#     menor = min(n1, n3, n4, n5)
# elif menor == n3:
#     soma = soma - menor
#     menor = min(n1, n2, n4, n5)
# elif menor == n4:
#     soma = soma - menor
#     menor = min(n1, n2, n3, n5)
# else:
#     soma = soma - menor
#     menor = min(n1, n2, n3, n4)
# #teste com IF para o maior valor
# if maior == n1:
#     soma = soma - maior
#     maior = max(n2, n3, n4, n5)
# elif maior == n2:
#     soma = soma - maior
#     maior = max(n1, n3, n4, n5)
# elif maior == n3:
#     soma = soma - maior
#     maior = max(n1, n2, n4, n5)
# elif maior == n4:
#     soma = soma - maior
#     maior = max(n1, n2, n3, n5)
# else:
#     soma = soma - maior
#     maior = max(n1, n2, n3, n4)

# media = soma / 3

# print("{:.1f}".format(media))

# #############################################################################
#  #4 - beecrowd | 2187
# #Bits trocados

# print("="*30)
# print("      Bits trocados")
# print("="*30)

# #variável para guardar o número do teste
# teste = 1

# #loop principal
# while True:
# # ler o valor solicitado pelo cliente
#     while True:
   
#      valor = int(input("Informe o valor: "))
#      #Teste com IF para verificar se o valor informado esta dentro da faixa
#      if 0 <= valor <= 10000:
#           #Caso estejam, este loop é interrompido
#         break
#      else:
#           #Caso não estejam, pede-se para digitar novamente
#         print("Valores fora da faixa permitida. Tente novamente.")

# # verificar se o valor é zero, encerrando o programa
#     if valor == 0:
#         print("programa encerrado pelo usuário")
#         break

# # inicializar as variáveis com o número de notas de cada tipo
#     num_notas_50 = num_notas_10 = num_notas_5 = num_notas_1 = 0

# # verificar quantas notas de B$50,00 são necessárias
#     if valor >= 50:
#         num_notas_50 = valor // 50
#         valor -= num_notas_50 * 50

# # verificar quantas notas de B$10,00 são necessárias
#     if valor >= 10:
#         num_notas_10 = valor // 10
#         valor -= num_notas_10 * 10

# # verificar quantas notas de B$5,00 são necessárias
#     if valor >= 5:
#         num_notas_5 = valor // 5
#         valor -= num_notas_5 * 5

# # a quantidade de notas de B$1,00 será o valor restante
#     num_notas_1 = valor

# # imprimir o resultado
#     print(f"Teste {teste}")
#     print(f"{num_notas_50} {num_notas_10} {num_notas_5} {num_notas_1}\n")
#     teste += 1


# #############################################################################
#  #Exercicio 16
# #Ordenação

# print("="*40)
# print("      pedra, papel ou tesoura")
# print("="*40)

# while True:
#     jogador1 = input("Jogador 1: pedra, papel ou tesoura? ")
#     jogador2 = input("Jogador 2: pedra, papel ou tesoura? ")

#     if jogador1 == jogador2:
#         print("Empate!")
#     elif jogador1 == "pedra" and jogador2 == "tesoura" or jogador1 == "tesoura" and jogador2 == "papel" or jogador1 == "papel" and jogador2 == "pedra":
#         print("Jogador 1 venceu!")
#     else:
#         print("Jogador 2 venceu!")

#     continuar = input("Deseja continuar jogando? (S/N) ")
#     if continuar.upper() != "S":
#         break

# #############################################################################
#  #Exercicio 17
# #Ordenação

# print("="*30)
# print("      bubble sort")
# print("="*30)

# # leitura dos valores
# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))
# c = int(input("Digite o terceiro número: "))

# # ordenação
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b

# # saída
# print("Os números em ordem crescente são:", a, b, c)

