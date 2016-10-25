import requests
from lxml import html
from parser import Parser
from csvcreator import CsvCreator
import time
from requests.exceptions import ConnectionError

parser = Parser()
payload = {'email': '', 'word': '' }
url = ""
sess = requests.session()
r = sess.post(url, data=payload)
tree = html.fromstring(r.content)
hallLinks = parser.extract_hall_links(r.content)
print( "We found " + str(len(hallLinks)) + " halls.")
villagerHrefs = []
start = time.time()
for hall in hallLinks:
    print( "Extracting births from " +  hall + " hall.")
    try :
        villagerHrefs.extend(parser.extract_hall_births(sess.get(hall).content))
        print("New total villager birth count: " + str(len(villagerHrefs)))
    except Exception :
        print("Somthing happened getting hall " + hall)
end = time.time()
print("Analyzed hall births in " + str((end - start)))

# start = time.time()
# stories = []
# for villager in villagerHrefs :
# # for x in range(0, 5) :
#     print("Getting story from " + villager)
#     vId = villager.replace('http://theislands.umn.edu/islander.php?id=', '')
#     summary = parser.extract_villager_story(vId, sess.get(villager).content)
#     print("Story for " + vId + " " + str(summary))
#     stories.extend(summary)
# end = time.time()
# print("Analyzed villager summaries in " + str((end - start)))
#
# storiesCsv = "full_stories.csv"
# print("Creating csv file " + storiesCsv)
# csvCreator = CsvCreator(storiesCsv, ['id', 'storyday', 'storyevent'])
# csvCreator.output_dict_to_csv(stories)

start = time.time()
summaries = []
for villager in villagerHrefs :
#for x in range(0, 1000) :
    print("Getting summary from " + villager)
    vId = villager.replace('http://theislands.umn.edu/islander.php?id=', '')
    for i in range(0,3) :
        try:
            summary = parser.extract_villager_summary(vId, sess.get(villager).content)
            break
        except ConnectionError:
            print("Sleepy time")
            time.sleep(10)
            if i==2 :
                print("check out")
    print("Summary for " + vId + " " + str(summary))

    summaries.append(summary)
end = time.time()
print("Analyzed villager summaries in " + str((end - start)))

summariesCsv = "summaries1.csv"
print("Creating csv file " + summariesCsv)
csvCreator = CsvCreator(summariesCsv, ['id', 'name', 'sex', 'age', 'died_year', 'address'])
csvCreator.output_dict_to_csv(summaries)