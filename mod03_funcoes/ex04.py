def converter_para_moeda_estrangeira(valor_em_reais, taxa_conversao):
    valor_convertido = valor_em_reais / taxa_conversao
    return valor_convertido

# Tabela de conversão
tabela_conversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

# Solicita ao usuário a quantidade de dinheiro na carteira
dinheiro_em_reais = float(input("Informe quanto dinheiro você tem na carteira em reais: "))

# Calcula e exibe quanto poderia comprar em cada moeda estrangeira
for moeda, taxa in tabela_conversao.items():
    valor_convertido = converter_para_moeda_estrangeira(dinheiro_em_reais, taxa)
    print(f"Com R${dinheiro_em_reais:.2f}, você poderia comprar {valor_convertido:.2f} {moeda}.")