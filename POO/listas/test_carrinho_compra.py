# test_carrinho_compra.py

import pytest
from carrinho_compra import adicionar_item, calcular_total

def test_adicionar_item():
    carrinho = []
    adicionar_item(carrinho, "Banana", 2.5)
    assert carrinho == [("Banana", 2.5)]

def test_calcular_total():
    carrinho = [("Banana", 2.5), ("Maçã", 3.0)]
    total = calcular_total(carrinho)
    assert total == 5.5