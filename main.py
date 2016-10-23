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
for village in links:
    href = domain + village
    print href
    hrefs.append(href)
personsHref = []
for x in range(0, 1) :
    villagePage = sess.get(hrefs[x])
    vId = villagePage.content.split("house.php?v=")[1].split("&h=")[0]
    houseids = html.fromstring(villagePage.content).xpath("//div[@class='houseid']/text()")

