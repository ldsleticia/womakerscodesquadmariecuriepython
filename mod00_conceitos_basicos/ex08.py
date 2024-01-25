'''
Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre 
o total do seu salário no referido mês.
'''

preco_hora_trab = float(input("\nDigite o valor por sua hora de trabalho: R$ "))
qtd_horas_trabs = int(input("\nDigite a quantidade de horas trabalhadas esse mês: "))
salario = preco_hora_trab*qtd_horas_trabs

print(f'\nSeu salário esse mês é R$ {salario:.2f}!\n')
