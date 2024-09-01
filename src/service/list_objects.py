from db import Database

from typing import Dict, List


def list_objects(db: Database, object: str, **kwargs) -> List[Dict]:
    if object in ("customer", "block"):
        return db.list(object)
    return []
