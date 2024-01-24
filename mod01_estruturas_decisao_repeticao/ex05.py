lado_a = float(input('Digite o lado do triangulo: '))
lado_b = float(input('Digite o lado do triangulo: '))
lado_c = float(input('Digite o lado do triangulo: '))

if lado_a == lado_b and lado_b == lado_c:
    print('Triangulo equilatero')
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    print('Triangulo isosceles')
else:
    print('Triangulo escaleno')
