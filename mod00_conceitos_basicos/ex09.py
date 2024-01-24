horas_de_exercicio = int(input('Digite a quantidade de horas de exercicio: '))
minutos = horas_de_exercicio / 60
media_calorias_minuto = 5

calorias_perdidas = media_calorias_minuto * minutos

print(
    f'Com base nas informações fornecidas, você perdeu {calorias_perdidas:.2f}')
