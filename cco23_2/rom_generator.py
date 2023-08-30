from random import randint

# Lista que armazena os valores para preenchimento da ROM auxiliar
store_values = []

print('')
print('Bem-vindo ao ROM Generator.')
rom = int(input('Informe o número da ROM para que as architectures aleatórias sejam geradas: '))
print('')
print(f'---------------ROM{rom}---------------')
print('')


# Uma iteração por linha
for i in range(16):

    # Dicionário do tipo posição:número + lista das strings + lista dos comentários
    numbers = {}
    strings_signal = []
    strings_comments = []

    for _ in range(rom + 3):

        # Obtemos uma posição aleatória que já não tenha sido escolhida
        while True:
            position = randint(0, 7)
            if position not in numbers.keys():
                break
        
        # Para essa posição, atribuímos um valor não repetido
        while True:
            value = randint(0, 14)
            if value not in numbers.values():
                break
        
        numbers[position] = value

    store_values.append(numbers.copy())

    # Hora de preencher a linha
    for j in range(8):
        string = ''

        string += '"'

        # Se essa posição for uma escolhida, preenchemos com o valor obtido.
        # Caso contrário, preenchemos com 1111.
        if j in numbers.keys():
            string += str(f'{int(bin(numbers[j])[2:]):04d}')
            strings_comments.append(str(hex(numbers[j])[2:]).upper())
        else:
            string += '1111'
            strings_comments.append('des')

        string += '"'

        strings_signal.append(string)

    print(' & '.join(strings_signal), end='')
    
    if i != 15:
        print(f' when address = "{int(bin(i)[2:]):04d}" else')
        print('--', end='')
        print('      '.join(strings_comments))
        print('')
    
    else:
        print(';')
        print('--', end='')
        print('      '.join(strings_comments))
        print('')


print(f'---------------ROM{rom}a---------------')
print('')

for k in range(16):
    string = ''
    string += '"'

    for l in range(14, -1, -1):
        if l in store_values[k].values():
            string += '1'
        else:
            string += '0'
    
    string += '"'
    
    if k != 15:
        string += f' when address = "{int(bin(k)[2:]):04d}" else'
    
    else:
        string += ';'
    
    print(string)

print('')
