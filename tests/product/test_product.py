from inventory_report.inventory.product import Product


def test_cria_produto():
    novoProduto = Product(
        1,
        "Coca-Cola",
        "Coca-Cola Company",
        "2020-01-01",
        "2020-12-31",
        "123456789",
        "em local seco e fresco.",
    )
    assert novoProduto.id == 1
    assert novoProduto.nome_do_produto == "Coca-Cola"
    assert novoProduto.nome_da_empresa == "Coca-Cola Company"
    assert novoProduto.data_de_fabricacao == "2020-01-01"
    assert novoProduto.data_de_validade == "2020-12-31"
    assert novoProduto.numero_de_serie == "123456789"
    assert novoProduto.instrucoes_de_armazenamento == "em local seco e fresco."
