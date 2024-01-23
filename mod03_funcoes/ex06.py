def forca():
    palavra = 'janaina'
    tentativas = 0
    letras_usuario = []
    ganhou = False

    while True:
        if not ganhou:
            chute = input('Chute uma letra: ').lower()
            letras_usuario.append(chute)
            for letra in palavra:
                if letra == letras_usuario:
                    print(letra, end="")
                else:
                    print(' _ ', end='')
            print()

            tentativas += 1

        if not ganhou and tentativas > 5:
            print(f'Voce perdeu, a palavra era {palavra}')
            break


forca()
