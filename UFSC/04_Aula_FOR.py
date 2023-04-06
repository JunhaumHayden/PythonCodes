#    #Estruturas de Repetição (for)
#    #Exercircio 01


#print("="*60)
#print("      Calcule quais são os anos bissextos")
#print("="*60)


##Entrada dos anos para verificação
#ini = int(input("Informe o ano inicial: "))
#fim=int(input("Informe o ano final: "))

##verificação da condição de ano bissexto
#div1 = ini%4 == 0
#div2 = ini%100 == 0
#div3 = ini%400 == 0

#if div1 or div2 or div2:
#    for i in range(ini, (fim + 1), 4):
#        print(f"{i} é ano bissexto.")

#else:
#    print(f"{ini} não é um ano bissexto")
    
    
    
#    #Exercircio 02
    
#print("="*30)
#print("      NUMERO IMPARES")
#print("="*30)
    
#ini = int(input("Informe o primeiro numero: "))
#fim=int(input("Informe o ultimo numero: "))

##Condição para iniciar em um numero impar

#if (ini%2 == 0):
#    ini = ini+1

    
#iteração dos numeros impares    
#for i in range(ini, (fim + 1), 2):
#    print(f"{i} é numero impar.")



#    #Exercircio 03
    
# print("="*30)
# print("      CALCULAR DESCONTO")
# print("="*30)
  

# # # ler as dados dos alunos
# maior_nota = 0
# nome_maior_nota = ""
# mensalidade_maior_nota = 0

# # loop para ler as informações dos alunos
# for i in range(5):
#     # lendo as informações do aluno
#     nome = input("Informe o nome do aluno: ")
#     nota = float(input("Informe a nota do aluno: "))
#     mensalidade = float(input("Informe o valor da mensalidade: "))

#     # verificando se a nota do aluno é maior que a maior nota até o momento
#     if nota > maior_nota:
#         # atualizando a maior nota e as informações do aluno com a maior nota
#         maior_nota = nota
#         nome_maior_nota = nome
#         mensalidade_maior_nota = mensalidade

# # calculando o desconto de 30% na mensalidade do aluno com a maior nota
# desconto = 0.3 * mensalidade_maior_nota
# mensalidade_com_desconto = mensalidade_maior_nota - desconto

# print("Aluno com a maior nota:", nome_maior_nota)
# print("Mensalidade sem desconto:", mensalidade_maior_nota)
# print("Mensalidade com desconto de 30%:", mensalidade_com_desconto)


# #    #Exercircio 04

# print("="*30)
# print("      IMPAR ou PAR")
# print("="*30)
  

# pares = 0
# impares = 0

# for i in range(10):
#     num = int(input("Informe um número inteiro: "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print("Quantidade de números pares:", pares)
# print("Quantidade de números ímpares:", impares)

# #    #Exercircio 05 / 06

# print("="*30)
# print("      PRIMO É PARENTE")
# print("="*30)
  
# numero = int(input("Informe um número inteiro: "))

# if numero < 2:
#     print("O número não é primo.")
# else:
#     eh_primo = True
#     for divisor in range(2, numero):
#         if numero % divisor == 0:
#             eh_primo = False
#             break
#     if eh_primo:
#         print("O número é primo.")
#     else:
#         print("O número não é primo.")
#         for i in range(2, numero):
#             if numero % i == 0:
#                 print(i)

#    #Exercircio 07

# print("="*30)
# print("      SENSO DA TURMA")
# print("="*30)

# n = int(input("Informe o número de pessoas na turma: "))
# idades = []
# soma_idades = 0

# for i in range(n):
#     idade = int(input("Informe a idade da pessoa {}: ".format(i+1)))
#     idades.append(idade)
#     soma_idades += idade

# media_idades = soma_idades / n

# if media_idades <= 25:
#     print("A turma é jovem, com média de idade de {:.1f} anos.".format(media_idades))
# elif media_idades <= 60:
#     print("A turma é adulta, com média de idade de {:.1f} anos.".format(media_idades))
# else:
#     print("A turma é idosa, com média de idade de {:.1f} anos.".format(media_idades))

# #    #Exercircio 08

# print("="*30)
# print("      SOMA INTERVALO")
# print("="*30)

# num1 = int(input("Informe o primeiro número inteiro: "))
# num2 = int(input("Informe o segundo número inteiro: "))

# if num1 < num2:
#     inicio = num1
#     fim = num2
# else:
#     inicio = num2
#     fim = num1

# soma = 0
# for i in range(inicio, fim+1):
#     print(i)
#     soma += i

# print("A soma dos números do intervalo é:", soma)

# #    #Exercircio 09

# print("="*30)
# print("      A TABUADA É")
# print("="*30)

# numero = int(input("Informe um número inteiro de 1 a 10 para gerar a tabuada: "))

# if numero < 1 or numero > 10:
#     print("Número inválido. O número deve ser entre 1 e 10.")
# else:
#     print("Tabuada de", numero, ":")
#     for i in range(1, 11):
#         resultado = numero * i
#         print("-", numero, "x", i, "=", resultado)


# #    #Exercircio 10

# print("="*40)
# print("    SAIBA O SEU CONCEITO NESSE SEMESTRE")
# print("="*40)


# soma_notas = 0
# nota_mais_alta = 0
# nome_mais_alta = ""


# for i in range(1, 6):
#     nome = input("Digite o nome do aluno " + str(i) + ": ")
#     nota = float(input("Digite a nota do aluno " + str(i) + ": "))
#     soma_notas += nota
    
   
#     if nota > nota_mais_alta:
#         nota_mais_alta = nota
#         nome_mais_alta = nome
        
# media = soma_notas / 5


# print("A média das notas da turma é:", media)

# print("O aluno com a nota mais alta é:", nome_mais_alta)

# if nota_mais_alta >= 5.75:
#     print("O aluno", nome_mais_alta, "foi aprovado!")
# elif nota_mais_alta >= 2.75:
#     print("O aluno", nome_mais_alta, "está em recuperação.")
# else:
#     print("O aluno", nome_mais_alta, "foi reprovado.")

#     #    #Exercircio 12

# print("="*30)
# print("    VAI DAR PRAIA")
# print("="*30)

# n = int(input("Informe o número de praias a serem cadastradas: "))
# dist_total = 0
# maior_dist = 0
# praias_entre_15_20 = 0
# nome_maior_dist = ''

# for i in range(n):
#     nome = input(f"Informe o nome da {i+1}ª praia: ")
#     dist = int(input(f"Informe a distância da {i+1}ª praia (em km) até o centro da cidade: "))
    
#     # atualiza a distância total
#     dist_total += dist
    
#     # verifica se a praia atual é a mais distante do centro
#     if dist > maior_dist:
#         maior_dist = dist
#         nome_maior_dist = nome
    
#     # verifica se a praia atual está entre 15 e 20 km do centro
#     if dist >= 15 and dist <= 20:
#         praias_entre_15_20 += 1

# # calcula a distância média das praias
# dist_media = round(dist_total/n, 1)

# # imprime os resultados
# print(f"A praia mais distante do centro é {nome_maior_dist}, a uma distância de {maior_dist} km.")
# print(f"Existem {praias_entre_15_20} praias entre 15 e 20 km do centro.")
# print(f"A distância média das praias é de {dist_media} km.")
