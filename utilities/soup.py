from bs4 import BeautifulSoup as bs4
import re

def C2(text):
    soup = bs4(text,"lxml")
    #print(soup.prettify())


def C2_index(text:str,root:str):
    soup = bs4(text,"lxml")
    # print(soup.prettify())
    
    result = {}
    class_in_json = {}
    """ find class name """
    title = soup.find("a")
    class_in_json["name"] = "微積分甲 (一)"
    class_in_json["link"] = title.get("href")
    """ find class number """
    class_in_json["number"] = "564003 [T34F56]"
    """ find text book """
    lists = soup.find("ul").find_all("li")
    book = re.match("教科書：(.*)",lists[0].text)
    class_in_json["text_book"] = book.groups()[0]
    """ find class """
    links = lists[1].find_all("a")
    #print(links[0].get("href"))
    # class schedule    
    class_in_json["schedule"] = root + links[0].get("href")
    # class school_schedule
    class_in_json["school_schedule"] = links[1].get("href")
    # class announces
    teaching_points = lists[1].find("ul").find_all("li")
    class_in_json["announce"] = teaching_points[0].find("a").get("href")
    result["class"] = class_in_json
    """ find scoring """
    scoring = teaching_points[1].find("ul").find_all("li")
    scoring_in_json = []
    for i in range(len(scoring)-1):
        text = str(scoring[i])
        print(text)
        title = re.match("<li>(.*)\(",text).groups()[0]
        weight = re.match(r"\(([0-9])%\)",text)
        print(weight)
        break
        scoring_in_json.append({
            "title": title,
            "weight": "isefjiskfje",
            "notes": ["fesjif","sfej"]
        })

    # find individual title, weight, notes
    """ find TA """
    # find name, email, office_hours
    """ find disscuss content """

    """ find references """
    #print(result)