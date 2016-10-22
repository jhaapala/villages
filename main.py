import requests
from lxml import html
import re


domain = ""
payload = {'email': '', 'word': '' }
url = ""
sess = requests.session()
r = sess.post(url, data=payload)
tree = html.fromstring(r.content)
links = tree.xpath("//area[@shape='circle']/@href")
hrefs = []
print "Here are our links: ", links
#villages
for village in links:
    href = domain + village
    print href
    hrefs.append(href)
personsHref = []
#houses
for x in range(0, 1) :
    villagePage = sess.get(hrefs[x])
    #v=[0-9]*&h=
    #c = re.compile("v=[0-9]*&h=")
    #m = c.match(villagePage.content)
    #print m
    #house.php?v=5&h=
    vId = villagePage.content.split("house.php?v=")[1].split("&h=")[0]
    houseids = html.fromstring(villagePage.content).xpath("//div[@class='houseid']/text()")
    #print houseids

# cancer = stressEvents + covariates
