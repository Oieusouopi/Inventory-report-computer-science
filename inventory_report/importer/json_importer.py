from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path[-4:] == "json":
            with open(path) as file:
                report_list = json.load(file)
                return report_list
        else:
            raise ValueError("Arquivo inválido")
