import unittest
from parser import Parser

class TestStringMethods(unittest.TestCase):

    def test_parse_hall(self) :
        parser = Parser()
        with open('samples/map.html', 'r') as hall:
            data = hall.read()
        result = parser.extract_hall_links(data)
        self.assertEqual(len(result), 27)
        self.assertEqual(result[0], "http://theislands.umn.edu/hall.php?Hofn")

    def test_parse_hall_births(self) :
        parser = Parser()
        with open('samples/hall.html', 'r') as hall:
            data = hall.read()
        result = parser.extract_hall_births(data)
        self.assertEqual(len(result), 5359)
        self.assertEqual(result[0], "http://theislands.umn.edu/islander.php?id=u33fmnhctv")
        self.assertEqual(result[len(result) - 1], "http://theislands.umn.edu/islander.php?id=h29qhex99t")


    def test_parse_villager_summary(self) :
        parser = Parser()
        with open('samples/villagerDead.html', 'r') as hall:
            data = hall.read()
        result = parser.extract_villager_summary(data)
        self.assertEqual(result['name'], "Agda Holst")
        self.assertEqual(result['sex'], "Female")
        self.assertEqual(result['age'], "115")
        self.assertEqual(result['died_year'], "117")
        self.assertEqual(result['address'], "")



if __name__ == '__main__':
    unittest.main()