lista = input().split(" ")

#lista_Inteiros = list(map(int, lista))
menor = int(lista[0])
maior = int(lista[0])
for i in range(len(lista)):
    if int(lista[i]) > maior:
        maior = int(lista[i])
    elif int(lista[i]) < menor:
        menor = int(lista[i])

print(menor)        
print(maior)

#print(lista)