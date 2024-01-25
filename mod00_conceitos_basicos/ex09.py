# Exercicio 9



def calcular_calorias_queimadas():
    horas_semana = float(input("Quantas horas por semana você se exercita? "))

    # Converte horas em minutos
    minutos_semana = horas_semana * 60

    # Considera uma média de 5 calorias por minuto de exercício
    calorias_por_minuto = 5

    # Calcula o total de calorias queimadas por semana
    calorias_semana = minutos_semana * calorias_por_minuto

    # Calcula o total de calorias queimadas por mês (considera 4 semanas no mês)
    calorias_mes = calorias_semana * 4

    # Imprime o total de calorias no mês
    print(f"Total de calorias queimadas no mês: {calorias_mes:.0f} calorias")


calcular_calorias_queimadas()
