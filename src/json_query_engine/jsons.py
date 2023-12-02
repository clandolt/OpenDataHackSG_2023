json_schema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/OpenData",
    "definitions": {
        "OpenData": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "$ref": "#/definitions/ID"
                },
                "id": {
                    "type": "string",
                    "format": "uuid"
                },
                "name": {
                    "type": "string"
                },
                "category": {
                    "type": "string"
                },
                "accessibility": {
                    "$ref": "#/definitions/Accessibility"
                },
                "pathClassifications": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/PathClassification"
                    }
                }
            },
            "required": [
                "_id",
                "accessibility",
                "category",
                "id",
                "name",
                "pathClassifications"
            ],
            "title": "OpenData"
        },
        "ID": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "$oid": {
                    "type": "string"
                }
            },
            "required": [
                "$oid"
            ],
            "title": "ID"
        },
        "PathClassification": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer"
                },
                "presetKey": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "accessibility": {
                    "$ref": "#/definitions/Accessibility"
                },
                "key": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "isActive": {
                    "type": "boolean"
                }
            },
            "required": [
                "accessibility",
                "description",
                "id",
                "isActive",
                "key",
                "name",
                "presetKey"
            ],
            "title": "PathClassification"
        },
        "Accessibility": {
            "type": "string",
            "enum": [
                "Completely accessible",
                "Not easily accessible",
                "Partially accessible"
            ],
            "title": "Accessibility"
        }
    }
}
