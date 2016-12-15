from lxml import html


class Parser:


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

    def extract_villager_summary(self, villagerId, htmlContent):
        id = villagerId
        tree = html.fromstring(htmlContent)
        name = tree.xpath("//div[@id='title']")[0].text_content()
        storylist = tree.xpath("//div[@id='t1']/div[@class='storyevent' and not(@id)]")
        sex = storylist[0].text_content()
        age = storylist[1].text_content().replace(" years old", "")
        alive_or_dead_or_job = storylist[2].text_content()
        died_year = ""
        address = ""
        job = ""
        if 'Died' in alive_or_dead_or_job :
            died_year = alive_or_dead_or_job.replace('Died in Year ','')
        elif 'Lives' in alive_or_dead_or_job:
            address = alive_or_dead_or_job.replace('Lives in ','')
        else: job = alive_or_dead_or_job
        alive_or_dead_or_job2 = storylist[3].text_content()
        if 'Died' in alive_or_dead_or_job2 :
            died_year = alive_or_dead_or_job2.replace('Died in Year ','')
        elif 'Lives' in alive_or_dead_or_job2:
            address = alive_or_dead_or_job2.replace('Lives in ','')
        return {"id": id, "name": name, "sex": sex, "age": age, "died_year": died_year, "address": address, "job": job}

    def extract_villager_story(self, villagerId, htmlContent):
        # "id": "", "storyday": "", "storyevent": ""
        id = villagerId
        tree = html.fromstring(htmlContent)
        events = tree.xpath("//div[@id='t2']/div[@class='timelineevent']")
        storyevents = []
        for items in events:
            for i in range(0,len(items)-1):
                storyday = items.xpath("./div[@class='storyevent']/div[@class='storyday']")[i].text_content()
                storyevent = items.xpath("./div[@class='storyevent']/text()[last()]")[i].strip()
                story = {"id": id, "storyday": storyday, "storyevent": storyevent}
                storyevents.append(story)
        return storyevents