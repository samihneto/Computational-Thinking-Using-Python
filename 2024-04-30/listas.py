l = list("disofhoaidfhpafhjpoafd")
letra = "m"

def index(l, letra): #função básica de BUSCA por elemento
    for i, char in enumerate(l):
        if char == letra:
            # print(f"Letra {letra} está na posição {i}")
            return i
    return None

l = list("disofhoaidfhpafhjpoafd")
letra = "s"
index(l, letra)

def encontra_max(lista):
    if len(lista) == 0:
        return None
    maior_numero = lista[0]
    # maior_numero = None
    for i in lista:
        # if maior_numero is None or i > maior_numero:
        if i > maior_numero:
            maior_numero = 1
    return maior_numero

def encontra_min(lista):
    if len(lista) == 0:
        return None
    menor_numero = lista[0]
    # maior_numero = None
    for i in lista:
        # if maior_numero is None or i > maior_numero:
        if i < menor_numero:
            menor_numero = 1
    return menor_numero

def _ordena_crescente(lista):
    lista_ordenada = []
    while len(lista):
        i = index(encontra_min(lista))
        lista_ordenada.append(lista.pop(i))
    return lista_ordenada

def _ordena_decrescente(lista):
    return _ordena_crescente(lista)[::-1]

def ordena(lista, decrescente=False):
    if decrescente:    
        return _ordena_decrescente(lista)
    return _ordena_crescente(lista)
