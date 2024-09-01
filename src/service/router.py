from typing import Dict, List

from db import Database

from service.customer import add_customer, find_customer, seach_customer
from service.list_objects import list_objects
from service.order import submit_order, find_order
from service.unknown import unknown

router = {
    "add_customer": add_customer,
    "find_customer": find_customer,
    "seach_customer": seach_customer,
    "submit_order": submit_order,
    "find_order": find_order,
    "list_objects": list_objects,
    "unknown": unknown
}


def route_action(db: Database, actions: List[Dict]) -> List[Dict]:
    action_results = []
    for action in actions:
        action_name = action["action_name"]
        if action_name not in router:
            continue

        func = router.get(action_name)
        action_results.append(
            {
                "action": action_name,
                "action_kwargs": action["action"],
                "results": func(db=db, **action["action"])
            }
        )

    return action_results
