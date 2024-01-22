while True:
    numero = int(input('Digite um numero entre 0 e 10 fora: '))
    if numero < 0 or numero > 10:
        continue
    else:
        print(f'O número digitado foi {numero}')
        break
