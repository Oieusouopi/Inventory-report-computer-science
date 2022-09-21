from inventory_report.importer.importer import Importer
import json

class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
            with open(path) as file:
                report_list = json.load(file)
                return report_list