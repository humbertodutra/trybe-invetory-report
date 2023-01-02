import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict


class Inventory:
    def import_data(path, report_type):
        if path.endswith(".csv"):
            return Inventory.to_csv(path, report_type)
        elif path.endswith(".json"):
            return Inventory.to_json(path, report_type)
        elif path.endswith(".xml"):
            return Inventory.import_xml(path, report_type)
        else:
            raise ValueError("Arquivo inválido")

    def to_csv(path, report_type):
        with open(path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            if report_type == "simples":
                return SimpleReport.generate(list(reader))
            elif report_type == "completo":
                return CompleteReport.generate(list(reader))
            else:
                raise ValueError("Tipo de relatório inválido")

    def to_json(path, report_type):
        with open(path, encoding="utf-8") as json_file:
            reader = json.load(json_file)
            if report_type == "simples":
                return SimpleReport.generate(reader)
            elif report_type == "completo":
                return CompleteReport.generate(reader)
            else:
                raise ValueError("Tipo de relatório inválido")

    def import_xml(path, report_type):
        with open(path) as file:
            doc = xmltodict.parse(file.read())["dataset"]["record"]
            if report_type == "simples":
                return SimpleReport.generate(doc)
            elif report_type == "completo":
                return CompleteReport.generate(doc)
            else:
                raise ValueError("Tipo inválido")
