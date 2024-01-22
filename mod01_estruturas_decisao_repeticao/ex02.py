turno = input('Digite o turno em que você estuda, sendo M para matutino, V para vespertino e N para noturno: ')
turno.lower()

if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa tarde!')
elif turno == 'n':
    print('Boa noite!')
else:
    print('Turno inválido')
