def max_array(lista):
    atual = lista[0]
    max_soma = lista[0]

    for i in range(1,len(lista)):
        if atual + lista[i] > lista[i]:
            atual = atual + lista[i]
        else:
            atual = lista[i]
        
        if atual > max_soma:
            max_soma = atual 
    return max_soma


lista = [5,-4,-2,6, 7,2,-8]

print(max_array(lista))