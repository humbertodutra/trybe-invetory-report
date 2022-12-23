from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(rep: list):
        simple = SimpleReport.generate(rep)
        products_per_company = {}

        for product in rep:
            if product["nome_da_empresa"] in products_per_company:
                products_per_company[product["nome_da_empresa"]] += 1
            else:
                products_per_company[product["nome_da_empresa"]] = 1
        retorno = simple + "\nProdutos estocados por empresa::"
        for product in products_per_company:
            retorno += f"\n- {product}: {products_per_company[product]}"

        return retorno


smallMock = [
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 1,
        "nome_do_produto": "Cadeira ",
        "nome_da_empresa": "Forces of Galo",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2025-02-10",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
]

print(CompleteReport.generate(smallMock))
