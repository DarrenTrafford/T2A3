import json

class Data():

    file_path = "data.json"

    @classmethod
    def save(cls, path, data):
        with open(path, "w") as file_handler:
            json_string = json.dumps(data)
            file_handler.write(json_string)

    @classmethod
    def load(cls, path):
        try:
            with open(path, "r") as file_handler:
                json_string = file_handler.read()
                return json.loads(json_string)
        except:
            return []

    @classmethod
    def update(cls, path, data):
        olddata = cls.load("data.json")
        print(olddata)
        olddata["pickle"] = data
        jsonstring = json.dumps(olddata)
        cls.save(path, jsonstring)
