submit_order = {
    "type": "function",
    "function": {
        "name": "submit_order",
        "description": "Submit an Order for a Customer",
        "parameters": {
            "type": "object",
            "properties": {
                "customer": {
                    "description": "Customer who is placing the Order",
                    "type": "string"
                },
                "item": {
                    "description": "The item to be ordered",
                    "type": "string",
                    "enum": [
                        "HAT", "SOCK", "TSHIRT", "LONG-SLEEVE"
                    ]
                },
                "item_quantity": {
                    "description": "How many of the items to be ordered",
                    "type": "number"
                }
            },
            "required": [
                "customer",
                "item",
                "item_quantity"
            ]
        }
    }
}


find_order = {
    "type": "function",
    "function": {
        "name": "find_order",
        "description": "Get the status and information for a order number.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_number": {
                    "description": "Associated order number that is being referenced.",
                    "type": "string"
                },
            },
            "required": [
                "order_number"
            ]
        }
    }
}
