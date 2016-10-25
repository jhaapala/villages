import unittest
from parser import Parser


class TestParser(unittest.TestCase):

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

    def test_parse_villager_summary_dead(self) :
        parser = Parser()
        with open('samples/villagerDead.html', 'r') as hall:
            data = hall.read()
        result = parser.extract_villager_summary(data)
        self.assertEqual(result["id"], "vId")
        self.assertEqual(result['name'], "Agda Holst")
        self.assertEqual(result['sex'], "Female")
        self.assertEqual(result['age'], "115")
        self.assertEqual(result['died_year'], "117")
        self.assertEqual(result['address'], "")

    def test_parse_villager_summary_alive(self) :
        parser = Parser()
        with open('samples/villagerAlive.html', 'r') as hall:
            data = hall.read()
        result = parser.extract_villager_summary("vId", data)
        self.assertEqual(result["id"], "vId")
        self.assertEqual(result['name'], "Lena Sorensen")
        self.assertEqual(result['sex'], "Female")
        self.assertEqual(result['age'], "0")
        self.assertEqual(result['died_year'], "")
        self.assertEqual(result['address'], "Hofn 165")

    def test_extract_villager_story(self):
        parser = Parser()
        with open('samples/villagerDead.html', 'r') as myfile:
            data = myfile.read()
        result = parser.extract_villager_story("vId", data)
        self.assertEqual(len(result), 51)
        self.assertEqual(result[0]["id"], "vId")
        self.assertEqual(result[0]["storyday"], "04/002")
        self.assertEqual(result[0]["storyevent"], "Born in Hofn 30")

        self.assertEqual(result[1]["id"], "vId")
        self.assertEqual(result[1]["storyday"], "24/005")
        self.assertEqual(result[1]["storyevent"], "Friends with dmp2hccsfg")

        self.assertEqual(result[6]["id"], "vId")
        self.assertEqual(result[6]["storyday"], "04/011")
        self.assertEqual(result[6]["storyevent"], "No longer friends with dmp2hccsfg")

        self.assertEqual(result[7]["id"], "vId")
        self.assertEqual(result[7]["storyday"], "18/011")
        self.assertEqual(result[7]["storyevent"], "Friends with dmp2hccsfg")

if __name__ == '__main__':
    unittest.main()