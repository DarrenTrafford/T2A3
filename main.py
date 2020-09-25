from jikanpy import Jikan
from prettyprinter import pprint
import requests
import json

jikan = Jikan()

question = input("What anime do you like?\n")

response = jikan.search('anime', question)

mal_id = response['results'][0]['mal_id']

variable = requests.get(f"https://api.jikan.moe/v3/anime/{mal_id}/recommendations").text

variable2 = json.loads(variable)

pprint(variable2['recommendations'][0]['title'])
pprint(variable2['recommendations'][0]['url'])
