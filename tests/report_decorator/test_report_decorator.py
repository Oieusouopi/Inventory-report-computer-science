from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate([{
        "id": 1,
        "nome_do_produto": "Cafe",
        "nome_da_empresa": "Cafes Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "instrucao"
    }])
    assert "\033[32mData de fabricação mais antiga:\033[0m" in report
    assert "\033[36m2020-07-04\033[0m\n" in report
    assert "\033[32mData de validade mais próxima:\033[0m" in report
    assert "\033[36m2023-02-09\033[0m\n" in report
    assert "\033[32mEmpresa com mais produtos:\033[0m" in report
    assert "\033[31mCafes Nature\033[0m" in report
