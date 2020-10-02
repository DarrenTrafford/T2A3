import json

from os.path import isfile

# Logic to save and load lists without overwriting the previous save


class Data:

    file_path = "../data.json"

    @classmethod
    def check_data_exists(cls):
        if isfile(cls.file_path):
            return True
        return False

    @classmethod
    def load(cls):
        try:
            with open(cls.file_path, "r") as file:
                ret_data = file.readline()
                return json.loads(ret_data)
        except json.JSONDecodeError as e:
            print(e)
            return[]
        except Exception:
            print(
                "You don't currently have a list! "
                "Creating a new file for you!\n")
            return[]

    @classmethod
    def save(cls, data):
        if not cls.check_data_exists():
            with open(cls.file_path, 'w') as file:
                file.write(json.dumps(data))
        else:
            with open(cls.file_path, 'w') as file:
                file.write(json.dumps(data))


class AnimeData(Data):

    file_path = "../anime.json"


class MangaData(Data):

    file_path = "../manga.json"
