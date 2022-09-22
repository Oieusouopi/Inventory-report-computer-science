from inventory_report.reports.colored_report import ColoredReport


def test_decorar_relatorio():
    colored_report = ColoredReport("simples")

    assert colored_report.generate(
            1,
            "Cafe",
            "Cafes Nature",
            "2020-07-04",
            "2023-02-09",
            "FR48",
            "instrucao",
    ) == (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m04-07-2020\033[0m\n"
        + "\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-02-09\033[0m\n"
        + "\033[32mEmpresa com mais produtos: \033[0m "
        + "\033[31mCafes Nature\033[0m"
    )
