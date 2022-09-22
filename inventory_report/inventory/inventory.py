from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path[-4:] == ".csv":
            report_list = CsvImporter.import_data(path)
            return cls.type_data(type, report_list)
        elif path[-4:] == "json":
            report_list = JsonImporter.import_data(path)
            return cls.type_data(type, report_list)
        elif path[-4:] == ".xml":
            report_list = XmlImporter.import_data(path)
            return cls.type_data(type, report_list)
        else:
            raise "Arquivo inválido"

    @classmethod
    def type_data(cls, type, report_list):
        if type == "simples":
            return SimpleReport.generate(report_list)
        elif type == "completo":
            return CompleteReport.generate(report_list)
        else:
            raise "Algo deu errado"
