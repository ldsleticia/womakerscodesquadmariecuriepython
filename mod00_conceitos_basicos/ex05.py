salario_bruto = float(
    input('Digite seu salário bruto para realizar o cálculo: '))
salario_liquido = 0

if salario_bruto <= 1903.98:
    print('Você não tem impostos a serem pagos')
elif salario_bruto <= 2826.65:
    impostos = (salario_bruto * (7.5 / 100))
    salario_liquido = salario_bruto - impostos
elif salario_bruto <= 3751.05:
    impostos = (salario_bruto * (15 / 100))
    salario_liquido = salario_bruto - impostos
elif salario_bruto <= 4664.68:
    impostos = (salario_bruto * (22.5 / 100))
    salario_liquido = salario_bruto - impostos
elif salario_bruto > 4664.68:
    impostos = (salario_bruto * (27.5 / 100))
    salario_liquido = salario_bruto - impostos

print(
    f'Seu salário líquido já deduzidos os impostos será de {salario_liquido:.2f}')
