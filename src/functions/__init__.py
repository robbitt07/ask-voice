from .order import submit_order, find_order
from .customer import add_customer, find_customer, search_customer
from .list_objects import list_objects

tools = [
    add_customer, find_customer, search_customer, submit_order, find_order, 
    list_objects
]
