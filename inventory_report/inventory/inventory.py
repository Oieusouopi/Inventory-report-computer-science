import csv
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path[-4:] == ".csv":
            with open(path) as file:
                report = csv.DictReader(file)
                report_list = [object_report for object_report in report]
                if type == "simples":
                    return SimpleReport.generate(report_list)
                elif type == "completo":
                    return CompleteReport.generate(report_list)
                else:
                    raise "Algo deu errado"
        else:
            raise "Error arquivo invalido"
