from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        oldest_factorydate = datetime.strptime(
            data[0]["data_de_fabricacao"], "%Y-%m-%d"
        )
        expiring_date = datetime.strptime(
            data[0]["data_de_validade"], "%Y-%m-%d"
        )

        empresa_que_mais_aparece = []

        for product in data:
            if (
                datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d")
                < oldest_factorydate
            ):
                oldest_factorydate = datetime.strptime(
                    product["data_de_fabricacao"], "%Y-%m-%d"
                )

            if (
                expiring_date < datetime.now()
                or expiring_date
                > datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            ):
                expiring_date = datetime.strptime(
                    product["data_de_validade"], "%Y-%m-%d"
                )

            empresa_que_mais_aparece.append(product["nome_da_empresa"])

        contador_empresa = max(
            set(empresa_que_mais_aparece), key=empresa_que_mais_aparece.count
        )
        retorno = (
            f"Data de fabricação mais antiga: {oldest_factorydate:%Y-%m-%d}\n"
            f"Data de validade mais próxima: {expiring_date:%Y-%m-%d}\n"
            f"Empresa com mais produtos: {contador_empresa}"
        )
        print(retorno)
        return retorno


smallMock = [
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-01-02",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-05-03",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 1,
        "nome_do_produto": "Cadeira ",
        "nome_da_empresa": "Forces of Galo",
        "data_de_fabricacao": "2022-05-03",
        "data_de_validade": "2025-02-10",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
]

SimpleReport.generate(smallMock)
