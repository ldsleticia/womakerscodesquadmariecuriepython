numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite mais um número: '))

lista = [numero_1, numero_2, numero_3]

if numero_1 < numero_2 < numero_3:
    print(numero_1, numero_2, numero_3)
elif numero_2 < numero_1 < numero_3:
    print(numero_2, numero_1, numero_3)
elif numero_3 < numero_2 < numero_1:
    print(numero_3, numero_2, numero_1)
elif numero_2 < numero_3 < numero_1:
    print(numero_2, numero_3, numero_1)
elif numero_3 < numero_1 < numero_2:
    print(numero_3, numero_1, numero_2)
elif numero_1 < numero_3 < numero_2:
    print(numero_1, numero_3, numero_2)

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            troca = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = troca
print(lista)
