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


# Menu Message
# MENU_MSG = """
# *****=====*****=====*****=====*****=====*****
# Welcome to Star Wars Directory
# Would you like to:
# 1. Get a New Anime Recommendation
# 2. Get a New Manga Recommendation
# 3. View Your Recommendations
# 4.
# 9. Exit
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
#     character = str(input("Name of an Anime you have watched recently?\n"))
#     temp_char = Star_Dict.get_api(character)
#     Star_Dict.write(temp_char)
#
#   elif menu_selection == 2:
#     character = str(input("Name of a Manga you have read recently?\n"))
#     temp = Star_Dict.search_dict(character)
#     if not temp:
#       print("No character found. Sorry.")
#     else:
#       print(f"Name: {character}")
#       print(f"Age: {temp[0]}")
#       print(f"Place of birth: {temp[1]}")
#     input("Enter to continue")
#   elif menu_selection == 3:
#     pass
#   elif menu_selection == 4:
#     chars = Star_Dict.read()
#     for item in chars.items():
#       print(f"Name: {item[0]}")
#       print(f"Age: {item[1][0]}")
#       print(f"Year Born: {item[1][1]}")
#       print("=====[]=====")
#     input("Enter to continue")
#   elif menu_selection == 9:
#     break
