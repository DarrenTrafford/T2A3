from jikanpy import Jikan
import requests
import json

jikan = Jikan()

class Recommendation():

    def __init__(self, series_str):
        self.series = series_str
        self.malid = self.getmalid()
        self.recommendations = self.get()

    def getmalid(self):
        question = input(f"What {self.series} do you like?\n")
        response = jikan.search(self.series, question)
        return response['results'][0]['mal_id']

    def get(self):
        variable = requests.get(f"https://api.jikan.moe/v3/{self.series}/{self.malid}/recommendations").text
        return json.loads(variable)

    def top5(self):
        return self.recommendations['recommendations'][:5]

    def clean(self):
        tobesaved = []
        for variable2 in self.top5():
            tobesaved.append({variable2['title']: variable2['url']})
        return({"name": tobesaved})

    def print(self, data):
        for i in data:
            print(i[0],i[1])
            print("")

    @classmethod
    def greeting(cls):
        return "Greetings"