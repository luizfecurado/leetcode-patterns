def igual(arr,valor):
    if len(arr) == 0:
        return 0
    
    if arr[0] == valor:
        return 1 + igual(arr[1:], valor)
    else:
        return igual(arr[1:], valor)
    
print(igual([2,2,2,3,3,2,2,5], 2))


