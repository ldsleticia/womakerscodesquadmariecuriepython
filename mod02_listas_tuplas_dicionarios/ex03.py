#Exercício 3 Módulo 3
def normalizar_nome_produto(nome):
    nome_normalizado = nome.lower()
    equivalencias = {
        "maca": "maçã",
        "maça": "maçã",
        "macã": "maçã",
        "pao" : "pão"
        "nao" : "não"
    }
    return equivalencias.get(nome_normalizado, nome_normalizado)


def adicionar_ao_carrinho(carrinho, produto, quantidade):
    if produto in carrinho:
        carrinho[produto] += quantidade
    else:
        carrinho[produto] = quantidade


def calcular_total(carrinho, precos):
    total = 0
    for produto, quantidade in carrinho.items():
        total += precos.get(produto, 0) * quantidade
    return total


# Preços fixos para cada produto
precos = {
    "maçã": 1.0,
    "banana": 0.5,
    "leite": 3.0,
    "pão": 2.0
}

# Carrinho de compras
carrinho = {}

while True:
    print("Produtos disponíveis e seus preços:", precos)
    produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
    produto = normalizar_nome_produto(produto)

    if produto in precos:
        quantidade = int(input(f"Digite a quantidade de {produto} que deseja adicionar: "))
        adicionar_ao_carrinho(carrinho, produto, quantidade)
    else:
        print("Produto não encontrado. Tente novamente.")

    continuar = input("Deseja adicionar mais um item? (sim/não) ").lower()
    if continuar != "sim":
        break

# Calculando o total do carrinho
total = calcular_total(carrinho, precos)
print("\nCarrinho:", carrinho)
print("Total do carrinho de compras: R$", total)
