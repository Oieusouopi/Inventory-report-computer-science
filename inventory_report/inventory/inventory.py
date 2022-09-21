import csv
import json
from bs4 import BeautifulSoup
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path[-4:] == ".csv":
            with open(path) as file:
                report = csv.DictReader(file)
                report_list = [object_report for object_report in report]
                return cls.type_data(type, report_list)
        elif path[-4:] == "json":
            with open(path) as file:
                report_list = json.load(file)
                return cls.type_data(type, report_list)
        elif path[-4:] == ".xml":
            with open(path, "r") as file:
                report = file.read()
                report_list = BeautifulSoup(report, "xml")
                return cls.type_data(type, report_list)
        else:
            raise "Error arquivo invalido"

    @classmethod
    def type_data(cls, type, report_list):
        if type == "simples":
            return SimpleReport.generate(report_list)
        elif type == "completo":
            return CompleteReport.generate(report_list)
        else:
            raise "Algo deu errado"
