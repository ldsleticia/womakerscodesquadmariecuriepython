''' Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área. '''

nome = input('Qual é o seu nome? ')
cidade = input('Qual cidade você mora? ')
animal = input('Qual é o seu animal preferido? ')
livro = input('Qual é o nome do seu livro favorito? ')

print('Oii {}, Prazer em conhece-la! Ouvi dizer que {} é um lugar muito agradável. Acho {} um animal íncrivel hehe. Não conhecia o livro {}, obrigada pela dica <3'.format(nome,cidade,animal,livro))