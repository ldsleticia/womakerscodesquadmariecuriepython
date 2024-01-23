def converter_moeda():
    moeda = float(input('Quantos reais você possui? '))
    converte_para_dolar_americano = moeda / 4.91
    converte_para_dolar_australiano = moeda / 3.18
    converte_para_dolar_canadense = moeda / 3.64
    converte_para_peso = moeda / 0.02
    converte_para_franco_suico = moeda / 0.42
    converte_para_euro = moeda / 5.36
    converte_para_libra_esterlina = moeda / 6.21

    print(f'Voce pode comprar {converte_para_dolar_americano:.2f} dólares americanos')
    print(f'Voce pode comprar {converte_para_dolar_australiano:.2f} dólares australianos')
    print(f'Voce pode comprar {converte_para_dolar_canadense:.2f} dólares canadenses')
    print(f'Voce pode comprar {converte_para_peso:.2f} pesos argentinos')
    print(f'Voce pode comprar {converte_para_franco_suico:.2f} francos suíços')
    print(f'Voce pode comprar {converte_para_euro:.2f} euros')
    print(f'Voce pode comprar {converte_para_libra_esterlina:.2f} libras esterlinas')


converter_moeda()
