from datetime import date


from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, list):
        manufacturing_date = [info["data_de_fabricacao"] for info in list]
        most_old_fabrication_product = min(manufacturing_date)

        recent_date_validate = min(
            [
                info["data_de_validade"]
                for info in list
                if date.fromisoformat(info["data_de_validade"]) >= date.today()
            ]
        )

        companies = [info["nome_da_empresa"] for info in list]
        companies_most_product = Counter(companies).most_common()[0][0]
        return (
            f"Data de fabricação mais antiga: {most_old_fabrication_product}\n"
            f"Data de validade mais próxima: {recent_date_validate}\n"
            f"Empresa com mais produtos: {companies_most_product}"
        )
