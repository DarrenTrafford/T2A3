from os import system
from jikanpy import Jikan
from src.anime import Recommendation
from src.datahandling import AnimeData
from src.datahandling import MangaData
from menus import Menus

jikan = Jikan()

def newrec(data, option):
    current_data = data.load()
    anime = Recommendation(option)
    current_data.append(anime.clean())
    data.save(current_data)
    recommendation = current_data[-1]
    for key, value in recommendation.items():
        print(f"Your Current {option} Recommendations:\n")
        print(key, "\n")
        for atitle in value:
            for key1, value1 in atitle.items():
                print(f"{key1}: {value1}")


def viewlist(data, option):
    alldata = data.load()
    print(f"Your Current {option} Recommendations:\n")
    for recommendation in alldata:
        for key, value in recommendation.items():
            print("\n", key, "\n")
            for atitle in value:
                for key1, value1 in atitle.items():
                    print(f"{key1}: {value1}")

def animenu():
    print(Menus.ANIME_MSG)
    while True:
        menu_selection = int(input(">"))
        if menu_selection not in [1,2,9]:
            print("Please input valid selection 1,2 or 9")
            menu_selection = int(input(">"))
        elif menu_selection == 1:
            system('clear')
            newrec(AnimeData, "anime")
            print(Menus.ANIME_MSG)
        elif menu_selection == 2:
            system('clear')
            viewlist(AnimeData, "Anime \n")
            print(Menus.RETURN_MSG)
        elif menu_selection == 9:
            exit()

def manmenu():
    print(Menus.MANGA_MSG)
    while True:
        menu_selection = int(input(">"))
        if menu_selection not in [1,2,9]:
            print("Please input valid selection 1,2 or 9")
            menu_selection = int(input(">"))
        elif menu_selection == 1:
            system('clear')
            newrec(MangaData, "manga")
            print(Menus.MANGA_MSG)
        elif menu_selection == 2:
            system('clear')
            viewlist(MangaData, "Manga \n")
            print(Menus.RETURN_MSG)
        elif menu_selection == 9:
            exit()

def retmenu():
    print(Menus.RETURN_MSG)
    while True:
        menu_selection = int(input(">"))
        if menu_selection not in [1,9]:
            print("Please input valid selection 1 or 9")
            menu_selection = int(input(">"))
        elif menu_selection == 1:
            system('clear')
            mainmenu()
        elif menu_selection == 9:
            exit()

# Main menu loop:
def mainmenu():
    print(Menus.MENU_MSG)
    while True:
        menu_selection = int(input(">"))
        if menu_selection not in [1,2,3,4,9]:
            print("Please input valid selection 1-4 or 9:")
            menu_selection = int(input(">"))
        elif menu_selection == 1:
            system('clear')
            newrec(AnimeData, "anime")
            animenu()
        elif menu_selection == 2:
            system('clear')
            newrec(MangaData, "manga")
            manmenu()
        elif menu_selection == 3:
            system('clear')
            viewlist(AnimeData, "Anime \n")
        elif menu_selection == 4:
            system('clear')
            viewlist(MangaData, "Manga \n")
        elif menu_selection == 9:
            exit()
mainmenu()


