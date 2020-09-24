from jikanpy import Jikan
from prettyprinter import pprint
import requests

jikan = Jikan()

question = input("What anime do you like?\n")

response = jikan.search('anime', question)

mal_id = response['results'][0]['mal_id']

pprint(requests.get(f"https://api.jikan.moe/v3/anime/{mal_id}/recommendations").text)