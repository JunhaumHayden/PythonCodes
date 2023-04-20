#Aula 09
# exemplo soma

def soma(a,b=1):
    print(f'a: {a}')
    print(f'b: {b}')
    
    soma= a+b
    print(soma)
    
   
#programa principal
soma(9,0)
soma(5,6)
soma(15)

#se deseja inverter a ordem dos parâmetros
soma(b=80,a=90)

# neste caso informar todos os parâmetros
#erro:
#soma(b=9, 10)

#erro (porque não estamos usando (por enquanto) empacotamento de parâmetros
#soma(4,5,6)

#funciona somente se eu indicar um valor para b na assinatura da função
# ex def soma(a,b=1)

soma(9,8)