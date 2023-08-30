def selection_sort(lista):
    for i in range(len(lista)):
        print(f'I: {i}')
        min_index = i
        for j in range(i+1, len(lista)):
            print(f'J: {j}')

            if lista[j] < lista[min_index]:
                min_index = j
        print(f'antes: {lista[i], lista[min_index]}')        
        lista[i], lista[min_index] = lista[min_index], lista[i]
        print(f'depois: {lista[i], lista[min_index]}')

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Chamando a função de ordenação
selection_sort(lista)

print("Lista ordenada:", lista)








