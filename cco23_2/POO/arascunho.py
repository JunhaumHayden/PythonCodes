print("="*30)
print("  Cadastrar de notas")
print("="*30)
#Tratamento de excecao
#n = int, input('1 - 01 Avaliação\n 2 - 02 Avaliação\n : ')
while True:
    try:
        a = int(input('digite: \n'))
        print(a)
        break
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
while True:
    #Tratamento de excecao
    try:
        c = int(input('Informe a categoria: \n 1 - Pequeno\n 2 - medio\n 3 - SUV / Caminhotene'))
        break
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
if c == 1:
    print(c)
if c == '2':
    print(c)
if c == '3':
    print(c)


# while True:
#     try:
#         N = int, input('1 - 01 Avaliação\n 2 - 02 Avaliação\n : ')
#         break
#     except ValueError:
#         print("Entrada inválida. Certifique-se de fornecer os valores corretos.")


# if N == '1':
#     print(N)
# if N == '2':
#     print(N)
# print("="*30)
# print( )
# print( )

# 10 / 0w

# try:
#     # Code that may raise an exception
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     # Code to handle the exception
#     print("Cannot divide by zero!")