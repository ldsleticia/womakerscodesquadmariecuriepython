def carrinho_compras():
    # Inicializa o carrinho como um dicionário vazio
    carrinho = {}

    # Adiciona produtos e quantidades ao carrinho
    carrinho["Produto1"] = 3
    carrinho["Produto2"] = 2
    carrinho["Produto3"] = 1

    # Calcula o total do carrinho de compras
    total_carrinho = sum(carrinho.values())

    # Exibe o conteúdo do carrinho e o total
    print("Conteúdo do carrinho:", carrinho)
    print("Total do carrinho de compras:", total_carrinho)

# Chama a função
carrinho_compras()

