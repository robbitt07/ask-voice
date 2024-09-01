from db import Database

from typing import Dict


def unknown(db: Database, message: str, **kwargs) -> Dict:
    return {"message": message}
