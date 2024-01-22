produtos = {
    "batata": 1,
    "arroz": 2
}

carrinho = {}
total = 0

while True:
    escolha = int(input('Digite 1 para escolher um produto ou 0 para sair: '))
    if escolha == 0:
        break

    print(produtos)
    produto = input('Digite o produto: ')
    quantidade = int(input('Digite a quantidade de unidades do produto: '))

    carrinho[produto] = quantidade

for key, value in carrinho.items():
    total += produtos.get(key) * value

print(carrinho)
print(total)
