from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data: list):
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

        return retorno
