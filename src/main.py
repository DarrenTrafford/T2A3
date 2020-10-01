from jikanpy import Jikan
from src.anime import Recommendation
from src.datahandling import AnimeData
from src.datahandling import MangaData

Recommendation.greeting()
print(Recommendation.greeting())

jikan = Jikan()

def test():
    current_data = MangaData.load()
    anime = Recommendation("manga")
    current_data.append(anime.clean())
    MangaData.save(current_data)
    for recommendation in current_data:
        for key,value in recommendation.items():
            print(key, "\n")
            for atitle in value:
                for key1,value1 in atitle.items():
                    print(f"{key1}: {value1}")

test()


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
#
#
#
#
#     break
