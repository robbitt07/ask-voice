import json
import os
from typing import Dict, Optional
from uuid import uuid4


class Database(object):

    def __init__(self) -> None:
        self._db = {}
        self.load()

    @property
    def data_path(self):
        return os.path.join("data", "_db.json")

    def load(self):
        if not os.path.exists(self.data_path):
            self._db = {}
            return

        with open(self.data_path, "r") as f:
            self._db = json.load(f)

    def save(self):
        with open(self.data_path, "w") as f:
            json.dump(self._db, f)

    def get(self, table_name: str, key: str) -> Optional[Dict]:
        return self._db.get(table_name, {}).get(key)

    def set(self, table_name: str, key: str, data: dict) -> Dict:
        table = self._db.get(table_name, {})
        table.update({key: data})
        self._db.update({table_name: table})
        self.save()
        return data

    def write(self, table_name: str, data: dict) -> Dict:
        key = str(uuid4())
        table = self._db.get(table_name, {})
        table.update({key: data})
        self._db.update({table_name: table})
        self.save()
        return {"key": key, "data": data}

    def list(self, table_name: str) -> Dict:
        return self._db.get(table_name, {})

    def search(self, table_name: str, attr: str, value: str) -> Dict:
        table = self._db.get(table_name, {})
        return {
            key: data
            for key, data in table.items()
            if value in str(data.get(attr))
        }

    def find_best(self, table_name: str, attr: str, value: str) -> Dict:
        return next(iter(
            self.search(table_name=table_name, attr=attr, value=value).items()
        ))
