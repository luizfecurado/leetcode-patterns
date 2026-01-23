def bubble(lista):
    tamanho = len(lista)
    for i in lista:
        print(lista)
        for j in range(tamanho-1):
           if lista[j] > lista[j+1]:
               lista[j+1], lista[j] = lista[j], lista[j+1]

bubble([10,6,4,3,2,1])