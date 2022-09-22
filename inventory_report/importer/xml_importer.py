from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path[-4:] == ".xml":
            with open(path, "r") as file:
                report = file.read()
                report_list = xmltodict.parse(report)["dataset"]["record"]
                return report_list
        else:
            raise ValueError("Arquivo inválido")
