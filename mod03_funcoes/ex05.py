def contar_vogais():
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogal = 0

    frase = input('Escreva uma frase e eu contarei as vogais ').lower()

    for letra in vogais:
        vogal += frase.count(letra)
    print(f'Sua frase tem {vogal} vogais')


contar_vogais()
