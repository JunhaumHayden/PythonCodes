# replace

s= "Aula de Introdução a Programação Orientada a Objetos"
print("saída 0: ",s)
print('saída 1: ',s[5:10])
print('saída 1a: ',s[0:3])
print('inverso: ',s[::-1])

#não altera a string, apenas retorna 
print("saída 2: upper com retorno no print: ", s.upper())
print("saída 3: print s: ", s)

# s2 irá armazenar o conteúdo de s.upper()
# poderia ser s2 = s.upper() (s permaneceria original e s2 alterado)
s = s.upper()
print("s2: ",s)
#print("s2: ",s)

# se desejo alterar a string original usar o replace
print("\nreplace (no print): ",s.replace("Introdução a Programação Orientada a Objetos", "alterando"))
print("saída 4 (s com uso de replace):",s)

nova=s.replace("Introdução a Programação Orientada a Objetos", "alterando")
# ou  s = s.replace  - ele recebe o novo valor 
print("saída 5 (nova string recebendo o novo conteúdo): ",nova)


t1 ="Bom"
t2 = "Dia"
t3 = "!"
print(t1)
print(t2)
print(t3)

completo= '+'.join([t1,t2,t3])
print("join: ",completo)


print(s.lower().find("intro"))