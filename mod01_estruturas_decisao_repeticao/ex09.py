num_par = 0
num_impar = 0

while True:
    numero = int(input('Digite um número ou 0 para sair: '))

    if numero == 0:
        break
    elif numero < 0:
        continue
    elif numero % 2 == 0:
        num_par += 1
    elif numero % 2 != 0:
        num_impar += 1
print(f'Você digitou {num_par} numeros pares e {num_impar} numeros ímpares')
