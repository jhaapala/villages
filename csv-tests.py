import unittest
from csvcreator import CsvCreator
from parser import Parser

class TestCsv(unittest.TestCase):

    def test_output_dict_to_csv(self):
        csvCreator = CsvCreator("test1231321.csv", ["a","b"])
        rows = []
        rows.append({"a" : 1, "b": "bcolumn1"})
        rows.append({"a": 2, "b": "bcolumn2"})
        csvCreator.output_dict_to_csv(rows)

    def test_output_dict_to_csv_2(self):
        parser = Parser()
        with open('samples/villagerDead.html', 'r') as myfile:
            data = myfile.read()
        result = parser.extract_villager_story("vId", data)
        csvCreator = CsvCreator("testrun.csv", ['storyevent', 'id', 'storyday'])
        csvCreator.output_dict_to_csv(result)

if __name__ == '__main__':
    unittest.main()