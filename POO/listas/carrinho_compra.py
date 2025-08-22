# carrinho_compra.py

def adicionar_item(carrinho, item, preco):
    carrinho.append((item, preco))
    return carrinho

def calcular_total(carrinho):
    return sum(preco for _, preco in carrinho)