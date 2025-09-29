#    #Aula 08, 09
#    #Aula 03/04/2023
#     #Lista de Exercícios - Funções
#     #Exercício 1099

###########################################################################
##  #URI Online Judge | 1048
##  #Salary Increase
#print("="*30)
#print("      Salary Increase")
#print("="*30)
#
###Declaração da função para calculo do percentual
#def aumento(val_sal):
#    ##Declaração das variaveis
#    percentual = 0
#    ganho = float(0)
#    novo_sal = float(0)
#    ##Casos de testes utilizando IF, ELFI e ELSE
#    if val_sal <= 400:
#        percentual = 15
#        ganho = val_sal * (percentual/100)
#        novo_sal = val_sal + ganho
#                
#    elif val_sal <= 800:
#        percentual = 12
#        ganho = val_sal * (percentual/100)
#        novo_sal = val_sal + ganho
#    elif val_sal <= 1200:
#        
#        percentual = 10
#        ganho = val_sal * (percentual/100)
#        novo_sal = val_sal + ganho
#    elif val_sal <= 2000:
#        
#        percentual = 7
#        ganho = val_sal * (percentual/100)
#        novo_sal = val_sal + ganho
#    else:
#        percentual = 4
#        ganho = val_sal * (percentual/100)
#        novo_sal = val_sal + ganho
#    ##Imprime os resultados  
#    print(f"Novo salario: {val_sal:,.2f}")
#    print(f"Reajuste ganho: {ganho:,.2f}")
#    print (f"percentual: {percentual} %")
#    
# #Entrada para verificação com a chamada da função  
#aumento(float(input("Informe o valor do salario: ")))

# ###########################################################################
# #  #beecrowd | 2057
# #  #Time Zone
# print("="*30)
# print("      Time Zone")
# print("="*30)

# def viagem (s,t,f):
#     #Ajuste do horario de chegada
#     s +=f
#     #Teste do horario de chegada negativa
#     if s < 0:
#         s += 24

#     #Calcular a hora de chegada
#     destino = (s + t)
#     #Teste da hora de chegada maior que 24
#     if destino >= 24:
#         destino -= 24
#     print(destino)
    

# partida, tempo, fuso = map(int,input("Informe o primeiro numero").split())
# viagem(partida, tempo, fuso)  

# ##########################################################################
#   #beecrowd | 1150
#   #Exceeding Z
# print("="*30)
# print("      Exceeding Z")
# print("="*30)

# x = int(input("Informe o primeiro numero: "))
# z = int(input("Informe o segundo numero: "))
# while z <= x:
#     z = int(input("Informe o terceiro numero: "))

# soma = x
# contador = 1

# while soma <= z:
#     x += 1
#     soma += x
#     contador += 1

# print(contador)

# ##########################################################################
#   #beecrowd | 1115
#   #Quadrant
# print("="*30)
# print("      Quadrant")
# print("="*30)

# def quadrante (x,y):
    
#     if x > 0 and y > 0:
#         print("primeiro")
#     elif x < 0 and y > 0:
#         print("segundo")
#     elif x < 0 and y < 0:
#         print("terceiro")
#     else:
#         print("quarto")

# while True:
#     coord01, coord02 = map(int, input("Informe as coordenadas: ").split())

#     if coord01 == 0 or coord02 == 0:
#         print("="*36)
#         print("      Programa finalizado")
#         print("="*36)
#         break
# #coord01, coord02 = map(int, input("Informe as coordenadas: ").split())
#     quadrante(coord01, coord02)

# ##########################################################################
#   #beecrowd | 2378
#   #Elevator
# print("="*30)
# print("      Elevator")
# print("="*30)


# def peso(n, c):
#     # # Leitura dos valores de entrada
#     # n, c = map(int, input().split())

#     # Variável que irá armazenar a quantidade de pessoas dentro do elevador
#     pessoas_dentro = 0

#     # Variável que irá indicar se a capacidade máxima foi excedida em algum momento
#     capacidade_excedida = False

#     # Loop para processar as leituras dos sensores
#     for i in range(n):
#         s, e = map(int, input(f"Leitura {i}: pessoas saindo e entrando: ").split())
#         #Variavel para receber as pessoas que saíram
#         pessoas_dentro -= s
#            # Verificar se a capacidade máxima foi excedida antes das pessoas entrarem
#         if pessoas_dentro > c:
#             capacidade_excedida = True
#             #Variavel para receber as pessoas que entraram
#         pessoas_dentro += e
#           # Verifica se a capacidade máxima foi excedida após as pessoas entrarem
#         if pessoas_dentro > c:
#            capacidade_excedida = True
#            print('S')
#            break
#     # Imprime o resultado
#     if capacidade_excedida:
#         print(f'Descer {pessoas_dentro - c} pessoas')
#     else:
#         print('N')
      
    
# # Leitura dos valores de entrada
# n_sensor, capacidade = map(int, input("Informe o numero de leituras e a capacidade: ").split())
# peso(n_sensor, capacidade)


##########################################################################
  #beecrowd | 2378
  #Elevator
print("="*30)
print("      Elevator")
print("="*30)

