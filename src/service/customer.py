from db import Database

from typing import Dict, List


def add_customer(db: Database, name: str, **kwargs) -> Dict:
    return db.write("customer", {"name": name})


def find_customer(db: Database, name: str, **kwargs) -> Dict:
    return db.find_best("customer", attr="name", value=name)


def seach_customer(db: Database, name: str, **kwargs) -> Dict:
    return db.search("customer", attr="name", value=name)
