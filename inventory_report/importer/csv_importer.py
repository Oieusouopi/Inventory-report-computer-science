from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            report = csv.DictReader(file)
            report_list = [object_report for object_report in report]
            return report_list