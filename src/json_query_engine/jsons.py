json_value = {
    "people": [
        {
            "name": "John Doe",
            "age": 30,
            "address": {
                "city": "New York",
                "state": "NY"
            },
            "is_student": False,
            "hobbies": ["reading", "traveling"]
        },
        {
            "name": "Anna Smith",
            "age": 25,
            "address": {
                "city": "San Francisco",
                "state": "CA"
            },
            "is_student": True,
            "hobbies": ["painting", "gardening"]
        }
    ]
}

json_schema = {
    "type": "object",
    "properties": {
        "people": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"},
                    "address": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string"},
                            "state": {"type": "string"}
                        },
                        "required": ["city", "state"]
                    },
                    "is_student": {"type": "boolean"},
                    "hobbies": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["name", "age", "address", "is_student", "hobbies"]
            }
        }
    },
    "required": ["people"]
}
