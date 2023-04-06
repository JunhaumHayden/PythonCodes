    #Estruturas de Decisão (Simples e Composta)
    #Exercircio 01

#imovel = float(input("Qual o valor do imovél? (Digite ponto ao invés de vírgula)"))
#print("{:.2f}".format(imovel))

#salario = float(input("Qual o valor do seu salário? (Digite ponto ao invés de vírgula)"))
#print("{:.2f}".format(salario))

#prazo = int(input("Em quantos anos o imóvel será pago?"))*12
#prazo= float(prazo)

#valor_prestacao = float(imovel / prazo)

#if(valor_prestacao <= (salario-(salario*0.70))):
#           print("O valor da prestação é {:.2f} emprestimo aprovado".format(valor_prestacao))
#else:
#    print("O valor da prestação é {:.2f} emprestimo negado".format(valor_prestacao))

    #Exercircio 02

# print("="*32)
# print("     MERCADINHO PREÇO CERTO")
# print("="*32)
# print()
# produtoPreco = float(input("Passe o produto no leitor: "))
# print(f"O preço do produto é: R$ {produtoPreco}")
# print("""
#    [1] - À vista dinheiro/cheque: 10% de desconto
#    [2] - À vista no cartão: 5% de desconto
#    [3] - Em até 2X no cartão: preço normal
#    [4] - 3x ou mais no cartão: 20% de juros""")

# opcaoPagamento = int(input("Informe a opção de pagamento: "))
# if opcaoPagamento == 1:
#         precoAtualizado = produtoPreco - (produtoPreco*0.10)
#         print(f"O preço atual é: R$ {precoAtualizado:,.2f}")
# elif opcaoPagamento == 2:
#         precoAtualizado = produtoPreco - (produtoPreco*0.05)
#         print(f"O preço atual é: R$ {precoAtualizado:,.2f}")
# elif opcaoPagamento == 3:
#         precoAtualizado = produtoPreco
#         print(f"O preço atual é: R$ {precoAtualizado:,.2f}")
# elif opcaoPagamento == 4:
#         precoAtualizado = produtoPreco + (produtoPreco*0.2)
#         print(f"O preço atual é: R$ {precoAtualizado:,.2f}")

 #Exercircio 03

# print("="*32)
# print("     SAIBA COMO ESTÁ SUA SAÚDE")
# print("="*32)
# print()

# m = float(input("Digite seu peso (em kg): "))
# h = float(input(f"{nome}, digite a sua primeira nota: "))

# imc = (m / (h**2))

# if imc < 18.5:
#     print(f"{nome}Sua média é: {media:.1f}. Alimente-se, você está abaixo do peso.")
# elif imc < 25:
#     print(f"{nome}Sua média é: {media:.1f}. Parabéns, você está no peso ideal.")
# elif imc < 30:
#     print(f"{nome}Sua média é: {media:.1f}. Tome cuidado, você está com sobrepeso.")
# elif imc < 40:
#     print(f"Seu imc é de : {imc:.1f}. Você está com obesidade, procure um médico.")
# else:
#     print(f"Seu imc é de {imc:.1f}. Meus pêsames, você está com obesidade mórbida.")


#Exercircio 04

# print("="*42)
# print("     CONSULTE O SEU DESEMPENHO NA USFC")
# print("="*42)
# print()

# nome = input("Digite o nome: ")
# nota1 = float(input(f"{nome}, digite a sua primeira nota: "))
# nota2 = float(input(f"{nome}, digite a sua segunda nota: "))
# nota3 = float(input(f"{nome}, digite a sua terceira nota: "))


# media = ((nota1+nota2+nota3) / 3)

# print(media)

# if media < 5:
#     print(f"{nome}, Sua média é: {media:.1f}. Você está reprovado. Esforce-se mais")
# elif media < 7:
#     print(f"{nome}, Sua média é: {media:.1f}. Você está em recuperação, Você consegue.")
# else:
#     print(f"{nome}, Sua média é: {media:.1f}. Parabéns, você está aprovado.")

#Exercircio 05

#print("="*42)
#print("     CONSULTE O SEU IMPOSTO")
#print("="*42)
#print()

#nome = (input(f"Informe o seu nome: "))
#sal = float(input(f"O salario de {nome} é: "))


#if(sal > 0 and sal <= 2000):
 #print(f"Você está Isento")
#elif(sal > 2000 and sal <= 3000):
 #resto = sal - 2000
 #resultado = resto * 0.08
 #print(f"O imposto a pagar é R$ {resultado:0.2f}")
#elif(sal > 3000 and sal < 4500):
 #resto = sal - 3000
 #resultado = (resto * 0.18) + (1000 * 0.08)
 #print(f"O imposto a pagar é R$ {resultado:0.2f}")
#else:
 #resto = sal - 4500
 #resultado = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 #print(f"O imposto a pagar é R$ {resultado:0.2f}")

#Exercircio 06

#print("="*42)
#print("     CALCULE O TEMPO DE EVENTO")
#print("="*42)
#print()
#dia1 = int(input("Informe o dia de início do evento: "))
#h1,m1,s1 = map(int,input("Informe a hora de início do evento (no formato hh:mm:ss):").split(":"))

#dia2 = int(input("Informe o dia de término do evento: "))
#h2,m2,s2 = map(int,input("Informe a hora de término do evento (no formato hh:mm:ss):").split(":"))

#s = s2 - s1
#m = m2 - m1
#h = h2 - h1
#d = dia2 - dia1

#if(s<0):
#    s+=60
#    m-=1

#if(m<0):
#    m+=60
#    h-=1

#if(h<0):
#    h+=24
#    d-=1

#print("O evento durará:")
#print(f"{d} dia(s)")
#print(f"{h} hora(s)")
#print(f"{m} minuto(s)")
#print(f"{s} segundo(s)")

#Exercircio 07

#print("="*30)
#print("     CONSULTE DDD")
#print("="*30)
#print()

#a = int(input("Informe o DDD: "))

#if a==61:
#    print("Brasilia")
#elif a==71:
#    print("Salvador")
#elif a==11:
#    print("Sao Paulo")
#elif a==21:
#    print("Rio de Janeiro")
#elif a==32:
#    print("Juiz de Fora")
#elif a==19:
#    print("Campinas")
#elif a==27:
#    print("Vitoria")
#elif a==31:
#    print("Belo Horizonte")
#else:
#    print("DDD nao cadastrado")

#Exercircio 08

#print("="*30)
#print("        DESCUBRA O MÊS")
#print("="*30)
#print()

#a = int(input("Informe o número do mês desejado: "))

#if(a==1):
#    print("January")
#elif(a==2):
#    print("February")
#elif(a==3):
#    print("March")
#elif(a==4):
#    print("April")
#elif(a==5):
#    print("May")
#elif(a==6):
#    print("June")
#elif(a==7):
#    print("July")
#elif(a==8):
#    print("August")
#elif(a==9):
#    print("September")
#elif(a==10):
#    print("October")
#elif(a==11):
#    print("November")
#elif(a==12):
#    print("December")
    
    
#Exercircio 09
    
#print("="*30)
#print("        CALCULE AS RAIZES DA EQUAÇÃO")
#print("="*30)
#print()

#A,B,C = map(float,input("Informe os valores de A, B e C da equação (Sendo A^2x + Bx + C no formato A B C): ").split())

#D = (B**2)-(4*A*C)
#if(D <0 or A==0):
#    print("Impossivel calcular")
#else:
#    D= D**(1/2)
#    R1 = (-B+D)/(2*A)
#    R2 = (-B-D)/(2*A)
#    print(f'R1 = {R1:0.5f}\nR2 = {R2:0.5f}')

#Exercircio 10
    
#print("="*40)
#print("     DESCUBRA QUEM É O VICE-CAMPEÃO")
#print("="*40)
#print()

#p1,p2,p3 = map(int,input("Informe a pontuação dos competidores A, B e C (separados por espaço): ").split())

#if (p1 > p2 and p1 < p3) or (p1 > p3 and p1 < p2):
#    print (p1)
#elif (p2 > p1 and p2 < p3) or (p2 > p3 and p2 < p1):
#    print (p2)
#else:
#    print (p3)

#Exercircio 11

# print("="*40)
# print("     CAMPEONATO DOS CAMPEÕES")
# print("="*40)
# print()

# c_vit,c_emp,c_saldo = map(int,input("Informe a pontuação do (separados por espaço): ").split())
# f_vit,f_emp,f_saldo = map(int,input("Informe a pontuação dos competidores A, B e C (separados por espaço): ").split())

# pontosC = c_vit * 3 + c_emp
# pontosF = f_vit * 3 + f_emp

# if (pontosC == pontosF):
#     if (f_saldo > c_saldo): 
#         print("F")
#     elif (f_saldo < c_saldo): 
#         print("C")
#     elif (f_saldo == c_saldo):
#         print("=")
# else:
#     if (pontosC > pontosF): 
#         print("C")
#     elif (pontosC < pontosF): 
#         print("F")

#Exercircio 12

# print("="*30)
# print("     Trader do Nlog Nintendo ")
# print("="*30)
# print()

# d, i, x, f = map(int, input("Informe na sequência e separado por espaços o dia de registro, preço inicial, variação diária do preço da ação, em quantos dias será o resgate:  ").split())

# # calcular o número de dias pares e ímpares que passarão até F dias a partir do dia inicial D
# print(f"São {f - d} dias totais")
# dias_pares = (f - d) // 2
# print(f"São {dias_pares} dias pares")
# dias_impares = (f - d) - dias_pares
# print(f"São {dias_impares} dias impares")

# # calcular o preço final das ações com base no número de dias pares e ímpares que passarão
# preco_final = i + dias_pares * x - dias_impares * x

# print(preco_final)

#Exercircio 13

# print("="*30)
# print("     Teste de Dado Clássico ")
# print("="*30)
# print()

# # lê o número de casos de teste
# n = int(input("Informe o numero de testes: "))

# # itera sobre os casos de teste
# for i in range(n):
#     # lê os valores do dado
#     valores = [int(x) for x in input("Informe os valores das faces do Dado: ").split()]
    
#     # verifica se o dado é clássico
#     if (valores[0] + valores[5] == 7) and (valores[1] + valores[3] == 7) and (valores[2] + valores[4] == 7):
#         print("SIM")
#     else:
#         print("NAO")


#Exercircio 14

# print("="*30)
# print("     Calcule o tempo de jogo ")
# print("="*30)
# print()

# # ler os tempos de início e fim
# tempo_inicial, tempo_final = map(int, input("Informe a hora de início e de fim do jogo: ").split())

# # calcular a duração do jogo
# if tempo_inicial < tempo_final:
#     duracao = tempo_final - tempo_inicial
# else:
#     duracao = 24 - tempo_inicial + tempo_final

# print("O JOGO DUROU", duracao, "HORA(S)")

#Exercircio 15

# print("="*51)
# print("  Calcule o tempo de jogo com precisão em minutos ")
# print("="*51)
# print()

# # ler as horas iniciais e finais do jogo
# hi, mi, hf, mf = map(int, input("Informe a hora de início e de fim do jogo: ").split())

# # converter para minutos
# inicio = hi * 60 + mi
# fim = hf * 60 + mf

# # cálcular a duração
# duracao = fim - inicio

# # ajustar a duração para casos em que o jogo durou mais de 24 horas
# if duracao <= 0:
#     duracao += 24 * 60

# # converter a duração para horas e minutos
# horas = duracao // 60
# minutos = duracao % 60

# print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

#Exercircio 16

# print("="*40)
# print("  Calcule as dimensões das caixas ")
# print("="*40)
# print()

# import math

# # lê os valores de entrada
# diametro = int(input("Informe o diâmetro da bola de boliche: "))
# altura, largura, profundidade = map(int, input("Informe as dimensões da caixa AxLxP: ").split())


# # verificar se a bola cabe dentro da caixa
# if (diametro <= altura):
#     if (diametro <= largura):
#         if (diametro <= profundidade):
#          print('S')
# else:
#     print('N')

#Exercircio 17

# print("="*40)
# print("  Calcule seu ajuste de salário ")
# print("="*40)
# print()


# salary = float(input("Informe o seu salário: "))

# if salary <= 400.00:
#     readjustment_rate = 0.15
# elif salary <= 800.00:
#     readjustment_rate = 0.12
# elif salary <= 1200.00:
#     readjustment_rate = 0.10
# elif salary <= 2000.00:
#     readjustment_rate = 0.07
# else:
#     readjustment_rate = 0.04

# readjustment = salary * readjustment_rate
# new_salary = salary + readjustment
# percentual = readjustment_rate * 100

# print("Novo salario: {:.2f}".format(new_salary))
# print("Reajuste ganho: {:.2f}".format(readjustment))
# print("Em percentual: {:.0f} %".format(percentual))
