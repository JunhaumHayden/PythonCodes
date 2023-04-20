##Aluno: Carlos Benedito Hayden de Albuquerque Junior
##matricula: 23100455
##Questao 04


print("="*30)
print("    Questao 04")
print("="*30)

def encontrarPrimos(n):
    #testar numero valido
    if n < 2:
      print("O número é inválido")
   #testar se numero é primo
    else:
        eh_primo = True
        #testar se o numero se há numero divisores nemores que o proprio numero
        #atraves do FOR que sairá do lcao antes de testar o proprio numero
        #Caso encontre algum divisor seta a variavel para falso e sai do laco
        for divisor in range(2, n):
            if n % divisor == 0:
                eh_primo = False
                break
        #Caso o numero seja primo retorna o numero
        if eh_primo:
            #print("O número é primo.")
            return (n)
        #caso o numero nao seja primo (validado pelo laco FOR) retorna nulo
        else:
            #print("O número não é primo.")
           
            return (None)
        
#Informar o numero de repetições e adiciona 1             
verif = int(input("Informe o n de tentativas: ") ) + 1
for i in range(verif, 1, -1):
    ene, eme = map(int, input("Informe os valores: ").split())
   #Caso o valor retornado seja nulo, subtrai 1 e testa novamente
    p1 = encontrarPrimos(ene)
    while p1 is None:
        ene -= 1
        p1 = encontrarPrimos(ene)
   #Caso o valor retornado seja nulo, subtrai 1 e testa novamente
    p2 = encontrarPrimos(eme)
    while p2 is None:
        eme -= 1
        p2 = encontrarPrimos(eme)

    produto = p1 * p2
    print(produto)

   
print("="*30)
print("    Fim do programa")
print("="*30)    
