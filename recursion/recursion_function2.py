def maior_elemento(arr):
    if len(arr) == 1:
        return arr[0]
    maior = maior_elemento(arr[1:])
    if arr[0] > maior:
        return arr[0]
    return maior


lista = [1,2,3,4,5,6,7]

print(maior_elemento(lista))