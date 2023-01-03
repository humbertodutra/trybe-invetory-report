from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Hulk_shirt",
        "Atletico",
        "01/12/2020",
        "31/12/2023",
        "100",
        "Armazenar em local seco",
    )

    assert ("Hulk_shirt" in product.__repr__()) is True
    assert ("Atletico" in product.__repr__()) is True
    assert ("01/12/2020" in product.__repr__()) is True
    assert ("31/12/2023" in product.__repr__()) is True
    assert ("Armazenar em local seco" in product.__repr__()) is True
