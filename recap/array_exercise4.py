def soma(lista):
    j = 0
    for i in lista: 
        j += i
    return j

def soma2(lista):
    x = 0 
    soma =0
    while x< len(lista):
        soma +=lista[x]
        x+=1
    return soma

array = [10,2,40,50,-2,3,100,21,33,29,123,234,32,88,90,23]
print(soma(array))

print(soma2(array))