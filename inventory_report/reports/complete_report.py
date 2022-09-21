from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)

        companies = [info["nome_da_empresa"] for info in list]
        quantity_companies = Counter(companies)
        arr_quantity_companies = [
            {i: quantity_companies[i]} for i in quantity_companies.keys()
        ]
        simple_report += "\nProdutos estocados por empresa:\n"
        for item in arr_quantity_companies:
            simple_report += f"- {[*item.keys()][0]}: {[*item.values()][0]}\n"
        return simple_report
