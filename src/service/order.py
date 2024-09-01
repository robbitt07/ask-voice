from db import Database

from service.customer import find_customer

from typing import Dict


def submit_order(db: Database,
                 customer: str,
                 item: str,
                 item_quantity: str,
                 **kwargs) -> Dict:
    customer_ref = find_customer(db=db, name=customer)
    return db.write(
        table_name="order", data={
            "customer": customer, "customer_ref": customer_ref, "item": item,
            "item_quantity": item_quantity
        }
    )


def find_order(db: Database, order_number: str, **kwargs) -> Dict:
    return db.get("order", key=order_number)
