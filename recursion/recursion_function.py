def regressiva(i):
    print(i)

    if i <= 1:
        return
    else:
        regressiva(i-1)

print (regressiva(8))


def soma_lista(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + soma_lista(arr[1:])

print(soma_lista([2,4,5,6,3]))