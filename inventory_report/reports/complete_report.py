from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, rep: list):
        simple = SimpleReport.generate(rep)
        products_per_company = {}

        for product in rep:
            if product["nome_da_empresa"] in products_per_company:
                products_per_company[product["nome_da_empresa"]] += 1
            else:
                products_per_company[product["nome_da_empresa"]] = 1

        retorno = simple + "\nProdutos estocados por empresa:\n"
        for product in products_per_company:
            retorno += f"- {product}: {products_per_company[product]}\n"

        return retorno
