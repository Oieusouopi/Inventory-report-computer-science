# from datetime import datetime


from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, list):
        manufacturing_date = [info["data_de_fabricacao"] for info in list]
        most_old_fabrication_product = min(manufacturing_date)
        # validation_date = [
        #     info["data_de_validade"]
        #     for info in list
        #     if date["data_de_validade"] >= datetime.today()
        # ]
        companies = [info["nome_da_empresa"] for info in list]
        companies_most_product = Counter(companies).most_common()[0][0]
        return (
            f"Data de fabricação mais antiga: {most_old_fabrication_product}"
            f"Data de validade mais próxima:"
            f"Empresa com mais produts: {companies_most_product}"
        )
