def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao(arr):
    novoarr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoarr.append(arr.pop(menor))
    return novoarr

print(ordenacao([7,6,3,2,10]))