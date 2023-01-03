from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "HulkShirt" "Atletico" "01/12/2022",
        "31/12/2023",
        "100" "Armazenar em local seco",
    )

    assert ("HulkShirt" in product._repr_()).is_true()
    assert ("Atletico" in product._repr_()).is_true()
    assert ("2020-01-01" in product._repr_()).is_true()
    assert ("2024-01-01" in product._repr_()).is_true()
    assert ("100" in product._repr_()).is_true()
    assert ("Armazenar em local seco" in product._repr_()).is_true()
