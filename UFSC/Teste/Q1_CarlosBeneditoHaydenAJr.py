##Aluno: Carlos Benedito Hayden de Albuquerque Junior
##matricula: 23100455
##Questao 01


print("="*30)
print("    Questao 01")
print("="*30)

t = int(input("Informe o numero de testes a realizar: "))
for i in range(t,0,-1):
    c = int(input("Informe a quantidade de consoantes: "))
    d = int(input("Informe a quantidade de digitos: "))
    
    l = 1
    n = 1
    for i in range(c):
        #print(i)
        l = (l * 26)
        #print(l)
    for i in range(d):
        #print(i)
        n = (n * 10)
        #print(n)
    if ( c == 0 and d == 0):
        print(0)
    else:
        print(l*n)
print("="*30)
print("    Fim do programa")
print("="*30)    
