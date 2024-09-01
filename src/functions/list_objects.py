list_objects = {
    "type": "function",
    "function": {
        "name": "list_objects",
        "description": "List a collection of Items, Customer, Block, Etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "object": {
                    "description": "Desired Object to list, Customer, Block, etc?",
                    "type": "string",
                    "enum": [
                        "customer", "block"
                    ]
                }
            },
            "required": ["object"]
        }
    }
}
