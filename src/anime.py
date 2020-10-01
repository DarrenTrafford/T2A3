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


## Begin finding MAL ID for recommendation
    def askquestion(self):
        question = input(f"What {self.series} do you like?\n")
        return question

## MAL ID grabbed from installed API
    def getmalid(self):
        response = jikan.search(self.series, self.name)
        return response['results'][0]['mal_id']

## API Call using MAL ID returns Anime information
    def get(self):
        variable = requests.get(f"https://api.jikan.moe/v3/{self.series}/{self.malid}/recommendations").text
        return json.loads(variable)

## Logic to give me top 5 recommendations based on input above
    def top5(self):
        return self.recommendations['recommendations'][:5]

## Slicing data to get only the Title and URL
    def clean(self):
        tobesaved = {}
        tobesaved_list = []
        for variable2 in self.top5():
            tobesaved_list.append({variable2['title']: variable2['url']})
        tobesaved[self.name] = tobesaved_list
        return(tobesaved)



    @classmethod
    def greeting(cls):
        return "Greetings"