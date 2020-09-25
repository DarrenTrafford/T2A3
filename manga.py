from jikanpy import Jikan
import requests
import json

jikan = Jikan()

class Manga():

    def __init__(self):
        self.malid = self.getmalid()
        self.recommendations = self.get()

    def getmalid(self):
        question = input("What Manga do you like?\n")
        response = jikan.search('manga', question)
        return response['results'][0]['mal_id']

    def get(self):
        variable = requests.get(f"https://api.jikan.moe/v3/manga/{self.malid}/recommendations").text
        return json.loads(variable)

    def top5(self):
        return self.recommendations['recommendations'][::5]

    def print(self):
        for variable2 in self.top5():
            print(variable2['title'] + "\n" + variable2['url'] + "\n")

variable = Manga()
variable.print()