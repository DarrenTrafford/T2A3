import json
import requests

from os.path import isfile

class Data():

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
        except Exception as e:
            print(f"Error: {e}")
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
