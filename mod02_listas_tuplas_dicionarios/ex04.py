agenda = {
    'amanda': "11999999999",
    'ana': "11999999998"
}

nome_para_procurar = input('Digite o nome que você deseja buscar: ').lower()

usuario = agenda.get(nome_para_procurar)
nomes = ','.join(str(nome) for nome in agenda.keys())

if usuario is None:
    print('Nome não encontrado')
    print(f'Na agenda há os seguintes contatos: {nomes}')
else:
    print(f'{nome_para_procurar}: ({usuario[0:2]}) {usuario[2:7]}-{usuario[7:11]}')
