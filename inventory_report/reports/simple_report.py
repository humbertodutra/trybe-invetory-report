from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(inventory: list):

        min_factory_date = min(
            [product["data_de_fabricacao"] for product in inventory]
        )

        expired_products = min(
            [
                product["data_de_validade"]
                for product in inventory
                if datetime.now().strftime("%Y-%m-%d")
                < product["data_de_validade"]
            ]
        )

        companey, number = Counter(
            [product["nome_da_empresa"] for product in inventory]
        ).most_common()[0]

        return (
            f"Data de fabricação mais antiga: {min_factory_date}\n"
            f"Data de validade mais próxima: {expired_products}\n"
            f"Empresa com mais produtos: {companey}"
        )
