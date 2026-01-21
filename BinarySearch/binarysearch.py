def binary_search(arr, target):
    baixo = 0 
    alto = len(arr) - 1
    contador = 0

    while baixo <= alto:
        meio = (baixo + alto) //2
        chute = arr[meio]
        contador +=1

        if chute == target:
            return meio, contador
        if chute > target:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


lista =  [2,4,5,6,7,8,9,10,11,12,13]

print(binary_search(lista, 12))