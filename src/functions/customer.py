add_customer = {
    "type": "function",
    "function": {
        "name": "add_customer",
        "description": "Add Customer to the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "Customer Name",
                    "type": "string"
                }
            },
            "required": [
                "name"
            ]
        }
    }
}


search_customer = {
    "type": "function",
    "function": {
        "name": "search_customer",
        "description": "Find multiple Customers in the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "Customer Name",
                    "type": "string"
                }
            },
            "required": [
                "name"
            ]
        }
    }
}

find_customer = {
    "type": "function",
    "function": {
        "name": "find_customer",
        "description": "Find a single Customer in the database.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "Customer Name",
                    "type": "string"
                }
            },
            "required": [
                "name"
            ]
        }
    }
}

