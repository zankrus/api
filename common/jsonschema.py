SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "bookingid": 35,
            "booking": {
                "firstname": "David",
                "lastname": "Bond",
                "totalprice": 9783,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "1997-12-15",
                    "checkout": "2012-05-08"
                },
                "additionalneeds": "space"
            }
        }
    ],
    "required": [
        "bookingid",
        "booking"
    ],
    "properties": {
        "bookingid": {
            "$id": "#/properties/bookingid",
            "type": "integer",
            "title": "The bookingid schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                35
            ]
        },
        "booking": {
            "$id": "#/properties/booking",
            "type": "object",
            "title": "The booking schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "firstname": "David",
                    "lastname": "Bond",
                    "totalprice": 9783,
                    "depositpaid": True,
                    "bookingdates": {
                        "checkin": "1997-12-15",
                        "checkout": "2012-05-08"
                    },
                    "additionalneeds": "space"
                }
            ],
            "required": [
                "firstname",
                "lastname",
                "totalprice",
                "depositpaid",
                "bookingdates",
                "additionalneeds"
            ],
            "properties": {
                "firstname": {
                    "$id": "#/properties/booking/properties/firstname",
                    "type": "string",
                    "title": "The firstname schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "David"
                    ]
                },
                "lastname": {
                    "$id": "#/properties/booking/properties/lastname",
                    "type": "string",
                    "title": "The lastname schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "Bond"
                    ]
                },
                "totalprice": {
                    "$id": "#/properties/booking/properties/totalprice",
                    "type": "integer",
                    "title": "The totalprice schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        9783
                    ]
                },
                "depositpaid": {
                    "$id": "#/properties/booking/properties/depositpaid",
                    "type": "boolean",
                    "title": "The depositpaid schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": False,
                    "examples": [
                        True
                    ]
                },
                "bookingdates": {
                    "$id": "#/properties/booking/properties/bookingdates",
                    "type": "object",
                    "title": "The bookingdates schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": {},
                    "examples": [
                        {
                            "checkin": "1997-12-15",
                            "checkout": "2012-05-08"
                        }
                    ],
                    "required": [
                        "checkin",
                        "checkout"
                    ],
                    "properties": {
                        "checkin": {
                            "$id": "#/properties/booking/properties/bookingdates/properties/checkin",
                            "type": "string",
                            "title": "The checkin schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "1997-12-15"
                            ]
                        },
                        "checkout": {
                            "$id": "#/properties/booking/properties/bookingdates/properties/checkout",
                            "type": "string",
                            "title": "The checkout schema",
                            "description": "An explanation about the purpose of this instance.",
                            "default": "",
                            "examples": [
                                "2012-05-08"
                            ]
                        }
                    },
                    "additionalProperties": True
                },
                "additionalneeds": {
                    "$id": "#/properties/booking/properties/additionalneeds",
                    "type": "string",
                    "title": "The additionalneeds schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "space"
                    ]
                }
            },
            "additionalProperties": True
        }
    },
    "additionalProperties": True
}