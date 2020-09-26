from jikanpy import Jikan
from anime import Recommendation
from datahandling import Data
from prettyprinter import pprint
import json

Recommendation.greeting()
print(Recommendation.greeting())

jikan = Jikan()

Anime = Recommendation("anime")
Manga = Recommendation("manga")

Data.save("data.json", Anime.clean())
#Anime.print(Data.load("data.json"))
Anime2 = Recommendation("anime")
Data.update("data.json", Anime2.clean())
pprint(Data.load("data.json"))
# Menu Message
# MENU_MSG = """
# *****=====*****=====*****=====*****=====*****
#
# Would you like to:
# 1. Get a New Anime Recommendation
# 2. Get a New Manga Recommendation
# 3. View Your Anime Recommendations
# 4. View Your Manga Recommendations
# 9. Exit
#
# *****=====*****=====*****=====*****=====*****
# """


# Main menu loop:
# while True:
#   system('clear')
#   print(MENU_MSG)
#   menu_selection = int(input(">"))
#   if menu_selection not in  [1,2,3,4,9]:
#     print("Please input valid selection 1-9:")
#     menu_selection = int(input(">"))
#   elif menu_selection == 1:

#     break
