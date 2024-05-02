
      # bubble sort

# Percorrer a lista toda
# a cada iteração, comparar os dados adjacentes,
# invertendo caso o elemento da esquerda seja menor que o da direita
# REPETIR até que não ocorra nenhuma inversão



lista = [3, 2, 54, 6, 2, 8, 345, 9]
for i in range(len(lista - 1)):
    pass
    if lista[i] > lista[i+1]:
            auxiliar = lista[i + 1]
            lista[i + 1] = lista[i]
            lista[i] = auxiliar
            # lista[i + 1], lista[i] = lista[i], lista[i+1]
print(lista)

def bubble_sort(lista: list[Any]):
    while True:
        sem_trocas = True
        for i in range(len(lista) - 1):
               if lista[i] > lista[i + 1]:
                      lista[i+1], lista[i] = lista[i], lista[i+1]
                      sem_trocas = True
        if sem_trocas:
            break
    return lista

print(bubble_sort([3, 2, 54, 6, 2, 8, 345, 9]))