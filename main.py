from jikanpy import Jikan
from anime import Recommendation
from prettyprinter import pprint
import requests
import json

jikan = Jikan()

Anime = Recommendation("anime")
Manga = Recommendation("manga")

print("Anime")
Anime.print()
print("Manga")
Manga.print()
