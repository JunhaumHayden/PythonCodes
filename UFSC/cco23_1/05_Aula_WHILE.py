#    #Estruturas de Repetição (for)
#    #Exercircio 01


#print("="*30)
#print("      Chá de Revelação")
#print("="*30)

#s = str(input("Informe o seu sexo (M => Masculino e F => Feminino): ")).upper()

#while s != "M" and s != "F":
#       print("Valor incorreto, digite novamente")
#       s = str(input("Informe o seu sexo (M => Masculino e F => Feminino):")).upper()
#else:
#               print(f"O sexo escolhido foi {s}")


#    #Exercircio 03

# print("="*30)
# print("      Previdencia")
# print("="*30)

# #Iniciando uma vaiavel para testar a condição do laço de repetição
# apontador = "S"
# while(apontador == "S"):
#     #Entrada para verificação
#     salario = (float(input("Informe o salario: ")))

#     #Calculo do desconto de 11%
#     desconto = (float(salario * 0.11))

#     #Verificação da condição de desconto
#     if desconto > 320: # para o caso for maior do que o teto de 320
#         desconto = 320 #A variável "desconto recebe o valor do teto"
#         print(f"O valor do desconto é: R${desconto:,.2f} que corresponde a {(desconto *100)/salario:,.2f} %") 
        
#     else:
#         print(f"O valor do desconto é: {desconto:,.2f} ")
#      #Entrada para verificação de continuidade do programa   
#     apontador = str(input("Deseja calcular o desconto para outro funcionário? (S / N): ")).upper()
# else:
#     print("Obrigado por utilizar nossos sistemas!")
# #############################################################################    
#     #Exercircio 04
# #beecrowd | 1075
# #Remaining 2

# print("="*30)
# print("      Remaining 2")
# print("="*30)
# #Entrada para verificação
# n = int(input("Digite um número inteiro menor que 10000: "))
# #Incrementando o contador com a função FOR
# for i in range(1, 10001):
#     if i % n == 2: #Sempre que o resto da divisão for igual a 2
#         print(i)   #Imprime o numero o contador


# #############################################################################    
#     #Exercircio 05
# #beecrowd | 1078
# #Multiplication Table

# print("="*40)
# print("      Multiplication Table")
# print("="*40)
# #Entrada para verificação
# n = int(input("Digite um número inteiro entre 2 e 999: "))
#
# # Teste da condição de execução do programa
# if n > 1 and n < 1000:
#     for i in range(1, 11): #Incremento de um contador de 1 a 10 utilizando a função FOR e range
#         print(f"{i} x {n} = {i*n}") #printa o resultado a cada passagem
# else:
#     print("O número digitado não está dentro do intervalo permitido!")

# #############################################################################    
#     #Exercircio 06
# #beecrowd | 1146
# #Growing Sequences

# print("="*40)
# print("      Growing Sequences")
# print("="*40)

# #Laço de repetição utilizando while true, pois a parada do programa será dentro do laço
# while True:
#     x = int(input("Informe um numero (Condição de para é zero - 0 -): ")) #Entrada para verificação
#     if x == 0: #Condição de parada do programa
#         break
#     #Utilizando a função FOR para percorrer os numeros de 1 a x através da função range
#     for i in range(1, x+1): 
#         if i == x: #Condição de parada da lista (Sem espaço)
#             print(i)
#         else: #Condição para imprimir a lista com espaços
#             print(i, end=" ")


# #############################################################################    
#     #Exercircio 07
# #beecrowd | 1134
# #Type of Fuel

# print("="*30)
# print("      Type of Fuel")
# print("="*30)

# #Inicia as variáveis com valores igual a zero
# alcool = gasolina = diesel = 0

# #utilizando um laço de repetição While para incrementar de acordo com o produto selecionado
# while True:
#     #Entrada para verificação
#     codigo = int(input("Informe o produto (1. Alcohol 2. Gasoline 3. Diesel 4. Finaliza o programa): "))
    
#     if codigo == 1:
#         alcool += 1
#     elif codigo == 2:
#         gasolina += 1
#     elif codigo == 3:
#         diesel += 1
#     elif codigo == 4:
#         break
#     # Caso numero escolhido não esteja na lista
#     if codigo not in (1, 2, 3, 4): 
#         continue
# #Imprime os resultado após a finalização do laço de repetição
# print("MUITO OBRIGADO")
# print(f"Alcool: {alcool}")
# print(f"Gasolina: {gasolina}")
# print(f"Diesel: {diesel}")

# #############################################################################    
#     #Exercircio 08
# #beecrowd | 1101
# #Sequence of Numbers and Sum

# print("="*30)
# print("      Sequence of Numbers and Sum")
# print("="*30)
# #utilizando um laço de repetição com While True para ler indefinidamente
# while True:
#     #Entrada para verificação
#     m, n = map(int, input("Informe dois numeros (separados por espaço): ").split())
#     if m <= 0 or n <= 0: #Condição de parada do programa quando a entrada for menor ou igual a zero
#         break
#     if n < m: #Condição de verificação de maior valor
#         m, n = n, m #Caso n seja menor que m, os valores são trocados de posição.
#     soma = 0 #Instanciação da variavel que irá receber o valor da soma
#     for i in range(m, n+1): #utilizando a função FOR para percorrer os valores entre m e n através da função range
#         print(i, end=' ') #Imprime os valores a cada passagem, utilizando espaços
#         soma += i #incrementa a soma com o valor da variavel i
#     print('Sum=%d' % soma)
