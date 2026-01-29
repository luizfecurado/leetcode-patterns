from random import randint
contador = 0

for i in range(1,3):
    aleatorio = randint(1,50)
    usuario = int(input("Digite um número de 1 a 50: "))
    if usuario < 0 or usuario > 50:
        print("Número inválido")
    if usuario == aleatorio:
        print("Você acertou!")
        contador+=1
    if usuario > aleatorio:
        print("Você digitou um número maior")
    if usuario < aleatorio:
        print("Você digitou um número menor")
print (f"Você acertou {contador} vezes")


