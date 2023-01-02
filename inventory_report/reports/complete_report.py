from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(inventory):
        simple_report = SimpleReport.generate(inventory)
        total = {}
        for item in inventory:
            if item["nome_da_empresa"] not in total:
                total[item["nome_da_empresa"]] = 1
            else:
                total[item["nome_da_empresa"]] += 1

        comapany_counter = ""
        for key, value in total.items():
            comapany_counter += f"- {key}: {value}\n"
        return (
            f"{simple_report}\n"
            + "Produtos estocados por empresa:\n"
            + comapany_counter
        )


# mock = [
#     {
#         "id": 1,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "Mesa",
#         "nome_da_empresa": "Forces of Galo",
#         "data_de_fabricacao": "2020-04-06",
#         "data_de_validade": "2024-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2019-03-04",
#         "data_de_validade": "2022-12-30",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
# ]

# print(CompleteReport.generate(mock))
