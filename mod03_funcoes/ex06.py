""" Vamos construir um jogo de forca. 
O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. 
A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado 
de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será 
revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um 
número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de 
tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse exercício"""

import random

palavras = ['mulheres','python','potencia','tech','gatinho']
tentativa = 6
letras_jogador = []
acertos = 0
erros = 0

palavra_aleatoria = random.choice(palavras)
print('Vamos brincar de FORCA? Tente adivinhar a palavra secreta \n')

while True:
  for letra in palavra_aleatoria:
    if letra in letras_jogador:
      print(letra, end=' ')
    else:
      print('_', end=' ')
  
  chance = input('\nEscolha uma letra: ')
  print('\n')
  letras_jogador.append(chance.lower())

  if chance.lower() not in palavra_aleatoria:
    tentativa -= 1
    erros += 1
    print('\nNão existe a letra `{}` na palavra secreta. Você errou {}x\n'.format(chance, erros))
  else:
    acertos += 1
  
  if tentativa == 0:
    print('Você excedeu o número de tentativas. Infelizmente, VOCÊ PERDEU T^T\n')
    break 

  if acertos == len(set(palavra_aleatoria)):
    print(f'\nA palavra secreta era: {palavra_aleatoria}.')
    print('\nPARABÉNS VOCÊ GANHOU! (⁠ﾉ⁠◕⁠ヮ⁠◕⁠)⁠ﾉ⁠*⁠.⁠✧\n')
    break