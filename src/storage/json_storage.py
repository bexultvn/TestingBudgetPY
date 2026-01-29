import json
import os
import copy


class JsonStorage:
    def __init__(self, path):
        self.path = path

    def load(self):
        if not os.path.exists(self.path):
            return {}

        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return copy.deepcopy(data)

    def save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
