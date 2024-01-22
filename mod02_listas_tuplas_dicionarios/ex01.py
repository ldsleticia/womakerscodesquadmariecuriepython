perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

sim = 0

for pergunta in perguntas:
    resposta = input(f'{pergunta} Responda apenas com Sim ou Não: ').lower()
    if resposta == 'sim':
        sim += 1

match sim:
    case 2:
        print('Suspeito')
    case 3 | 4:
        print('Cúmplice')
    case 5:
        print('Assassino')
    case _:
        print('Inocente')
