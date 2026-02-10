def funcao(lista):
    if not lista:
        return 0
    else:
        return lista[0] + funcao(lista[1:])
    

print(funcao([1,2,3,4,5]))
        