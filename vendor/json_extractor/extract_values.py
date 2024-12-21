import json


class json_extractor:
    def __init__(self,json_file:str) -> None:
        with open(json_file, 'r') as file:
            self.data = json.load(file)

    def get_json(self):
        return self.data
    def get_value(self,key):
        return self.data[key]
    def get_keys(self):
        return self.data.keys()