from lxml import html


class Parser:

    #domain = "http://theislands.umn.edu/"

    #[{"name": "", "url":""}]
    def extract_hall_births(self, htmlContent):
        tree = html.fromstring(htmlContent)
        links = tree.xpath("//div[@id='t2']/table/tr/td/a/@href")
        result = []
        for href in links:
            href = "http://theislands.umn.edu/" + href
            result.append(href)
        return result

    def extract_hall_links(self, htmlContent):
        tree = html.fromstring(htmlContent)
        links = tree.xpath("//area[@shape='circle']/@href")
        hrefs = []
        # villages
        for href in links:
            href = href.replace("village","hall")
            href = "http://theislands.umn.edu/" + href
            hrefs.append(href)
        return hrefs

    def extract_villager_summary(self, htmlContent):
        tree = html.fromstring(htmlContent)
        name = tree.xpath("//div[@id='title']")[0].text_content()
        storylist = tree.xpath("//div[@id='t1']/div[@class='storyevent' and not(@id)]")
        sex = storylist[0].text_content()
        age = storylist[1].text_content().replace(" years old", "")
        alive_or_dead = storylist[2].text_content()
        died_year = ""
        address = ""
        if 'Died' in alive_or_dead :
            died_year = alive_or_dead.replace('Died in Year ','')
        if 'Lives' in alive_or_dead:
            address = alive_or_dead.replace('Lives in ','')
        return {"name": name, "sex": sex, "age": age, "died_year": died_year, "address": address}


    def extract_villager_story(self, villagerId, htmlContent):
        # "id": "", "storyday": "", "storyevent": ""
        id = villagerId
        tree = html.fromstring(htmlContent)
        events = tree.xpath("//div[@id='t2']/div[@class='timelineevent']")
        storyevents = []
        for items in events:
            storyday = items.xpath("./div[@class='storyevent']/div[@class='storyday']")[0].text_content()
            storyevent = items.xpath("./div[@class='storyevent']/text()[last()]")[0].strip()
            storylink = ""
            try:
                storylink = items.xpath("./div[@class='storyevent']/a")[0].attrib["href"].replace("islander.php?id="," ")
            except Exception:
                pass
            storyevent = storyevent + storylink
            story = {"id": id, "storyday": storyday, "storyevent": storyevent}
            storyevents.append(story)
        return storyevents

