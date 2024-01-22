numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'O primeiro número é o maior')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'O segundo número é o maior')
else:
    print('O terceiro número é o maior')
