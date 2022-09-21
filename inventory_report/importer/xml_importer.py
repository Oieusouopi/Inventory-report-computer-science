from inventory_report.importer.importer import Importer
from bs4 import BeautifulSoup

class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path, "r") as file:
                report = file.read()
                report_list = BeautifulSoup(report, "xml")
                return report_list
