from jikanpy import Jikan
import requests
import json

jikan = Jikan()

class Recommendation():

    def __init__(self, series_str):
        self.series = series_str
        self.name = self.askquestion()
        self.malid = self.getmalid()
        self.recommendations = self.get()

    def askquestion(self):
        question = input(f"What {self.series} do you like?\n")
        return question

    def getmalid(self):
        response = jikan.search(self.series, self.name)
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
        return(tobesaved)

    def print(self, data):
        for i in data:
            print(i[0],i[1])
            print("")

    @classmethod
    def greeting(cls):
        return "Greetings"