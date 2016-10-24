import csv

class CsvCreator:

    def __init__(self, fileName, fieldNames):
        self.fileName = fileName
        self.fieldNames = fieldNames

    def output_dict_to_csv(self, dicts) :
        with open(self.fileName, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldNames)
            writer.writeheader()
            writer.writerows(dicts)

