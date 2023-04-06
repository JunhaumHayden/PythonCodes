
exemplo = 'testando as funções de manipulação de string'
'''
#análise
print('count:',exemplo.count('e'))
print('find: ', exemplo.find('as1'))
print('find: ', exemplo.find('as'))
print('len: ', len(exemplo))
print('existe manipulação em exemplo? ', "manipulação" in exemplo) #operador
'''

#transformação
#string é imutável (utilizamos métodos para "mudá-la" sem alterar em seus elementos)

#replace (substitui em uma forma secundária)
print('replace: ',exemplo)
exemplo.replace("testando","executando")
print(exemplo)

print(exemplo.replace("testando","executando"))
print(exemplo)   #volta a imprimir a string original

novo_exemplo = exemplo.replace("testando","executando xxx")
print("\nnovo_exemplo: ",novo_exemplo)



lista = input('Digite 3 inf:').split()
print(lista)
lista_numérica = [int(x) for x in input('Digite 3 inf:').split()]
print(lista_numérica)
listac = input('Digite 3 inf (palavras):').split()
print(listac)
