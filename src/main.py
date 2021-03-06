from os import system, name
from jikanpy import Jikan
from anime import Recommendation
from datahandling import AnimeData
from datahandling import MangaData
from menus import Menus

jikan = Jikan()


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# Logic to create new recommendation


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


# Logic to view existing lists


def viewlist(data, option):
    alldata = data.load()
    print(f"Your Current {option} Recommendations:")
    for recommendation in alldata:
        for key, value in recommendation.items():
            print("\n", key, "\n")
            for atitle in value:
                for key1, value1 in atitle.items():
                    print(f"{key1}: {value1}")


# Anime Menu


def animenu():
    print(Menus.ANIME_MSG)
    while True:
        menu_selection = int(input(">"))
        if menu_selection not in [1, 2, 9]:
            print("Please input valid selection 1,2 or 9")
        elif menu_selection == 1:
            clear_screen()
            newrec(AnimeData, "anime")
            print(Menus.ANIME_MSG)
        elif menu_selection == 2:
            clear_screen()
            viewlist(AnimeData, "Anime \n")
            print(Menus.RETURN_MSG)
            while True:
                submenu_selection = int(input(">"))
                if submenu_selection not in [1, 9]:
                    print("Please input valid selection 1 or 9")
                elif submenu_selection == 1:
                    clear_screen()
                    return
                elif submenu_selection == 9:
                    exit()
        elif menu_selection == 9:
            clear_screen()
            return ()


# Manga Menu


def manmenu():
    print(Menus.MANGA_MSG)
    while True:
        menu_selection = int(input(">"))
        if menu_selection not in [1, 2, 9]:
            print("Please input valid selection 1,2 or 9")
        elif menu_selection == 1:
            clear_screen()
            newrec(MangaData, "manga")
            print(Menus.MANGA_MSG)
        elif menu_selection == 2:
            clear_screen()
            viewlist(MangaData, "Manga \n")
            print(Menus.RETURN_MSG)
            while True:
                submenu_selection = int(input(">"))
                if submenu_selection not in [1, 9]:
                    print("Please input valid selection 1 or 9")
                elif submenu_selection == 1:
                    return
                elif submenu_selection == 9:
                    exit()
        elif menu_selection == 9:
            clear_screen()
            return ()


# Main menu loop:


def mainmenu():
    while True:
        print(Menus.MENU_MSG)
        menu_selection = int(input(">"))
        if menu_selection not in [1, 2, 3, 4, 9]:
            print("Please input valid selection 1-4 or 9:")
        elif menu_selection == 1:
            newrec(AnimeData, "anime")
            clear_screen()
            animenu()
        elif menu_selection == 2:
            newrec(MangaData, "manga")
            clear_screen()
            manmenu()
        elif menu_selection == 3:
            clear_screen()
            viewlist(AnimeData, "Anime \n")
            print(Menus.RETURN_MSG)
            while True:
                submenu_selection = int(input(">"))
                if submenu_selection not in [1, 9]:
                    print("Please input valid selection 1 or 9")
                elif submenu_selection == 1:
                    clear_screen()
                    break
                elif submenu_selection == 9:
                    exit()
        elif menu_selection == 4:
            clear_screen()
            viewlist(MangaData, "Manga \n")
            print(Menus.RETURN_MSG)
            while True:
                submenu_selection = int(input(">"))
                if submenu_selection not in [1, 9]:
                    print("Please input valid selection 1 or 9")
                elif submenu_selection == 1:
                    clear_screen()
                    break
                elif submenu_selection == 9:
                    exit()
        elif menu_selection == 9:
            exit()


mainmenu()
