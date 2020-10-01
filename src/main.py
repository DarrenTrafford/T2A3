from jikanpy import Jikan
from src.anime import Recommendation
from src.datahandling import AnimeData
from src.datahandling import MangaData
from menus import Menus

Recommendation.greeting()
print(Recommendation.greeting())

jikan = Jikan()

def newrec(data, option):
    current_data = data.load()
    anime = Recommendation(option)
    current_data.append(anime.clean())
    data.save(current_data)
    for recommendation in current_data:
        for key,value in recommendation.items():
            print(f"Your Current {option} Recommendations:\n")
            print(key, "\n")
            for atitle in value:
                for key1,value1 in atitle.items():
                    print(f"{key1}: {value1}")


def viewlist(data, option):
    alldata = data.load()
    print(f"Your Current {option} Recommendations:\n")
    for recommendation in alldata:
        for key, value in recommendation.items():
            print(key, "\n")
            for atitle in value:
                for key1, value1 in atitle.items():
                    print(f"{key1}: {value1}")


def animenu():
    menu_selection = int(input(">"))
    if menu_selection not in [1,2,9]:
        print("Please input valid selection 1,2 or 9")
        menu_selection = int(input(">"))
    elif menu_selection == 1:
        newrec(AnimeData, "anime")
        print(Menus.ANIME_MSG)
    elif menu_selection == 2:
        viewlist(AnimeData, "Anime \n")
        print(Menus.RETURN_MSG)


print(Menus.MENU_MSG)
# Main menu loop:
while True:
    menu_selection = int(input(">"))
    if menu_selection not in [1,2,3,4,9]:
        print("Please input valid selection 1-4 or 9:")
        menu_selection = int(input(">"))
    elif menu_selection == 1:
        newrec(AnimeData, "anime")
        print(Menus.ANIME_MSG)
        animenu()
    elif menu_selection == 2:
        newrec(MangaData, "manga")
        print(Menus.MANGA_MSG)
    elif menu_selection == 3:
        viewlist(AnimeData, "Anime \n")
        print(Menus.RETURN_MSG)
    elif menu_selection == 4:
        viewlist(MangaData, "Manga \n")
        print(Menus.RETURN_MSG)
    elif menu_selection == 9:
        break


