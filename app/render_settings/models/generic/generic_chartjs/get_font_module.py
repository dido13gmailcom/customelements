from copy import deepcopy




def get_font_module(add_prefix:str, font_size:int = 12):

    font_module = {
    "id":"font",
    "name":"Font",
    "description":"",
    "type":"font",
    "default":"",
    "properties":[
        {
        "id":"name",
        "name":"",
        "description":"",
        "type":"string",
        "default":"Helvetica"
        },
        {
        "id":"size",
        "name":"Font size",
        "description":"Font size",
        "type":"integer",
        "default":"10"
        },
        {
        "id":"bold",
        "name":"Negreta?",
        "description":"Font size",
        "type":"bool",
        "default":"false"
        },
        # {
        # "id":"bold",
        # "name":"Is bold?",
        # "description":"Is bold?",
        # "type":"boolean",
        # "default":"false"
        # },
        # {
        # "id":"italic",
        # "name":"Is italic?",
        # "description":"Is italic?",
        # "type":"boolean",
        # "default":"false"
        # },
        # {
        # "id":"underline",
        # "name":"Is underline?",
        # "description":"Is underline?",
        # "type":"boolean",
        # "default":"false"
        # },
        {
        "id":"color",
        "name":"Font color",
        "description":"Font color",
        "type":"color",
        "default":"#000000"
        }
    ]
    }

    font_module["id"] = add_prefix + font_module["id"]
    font_module["properties"][1]["default"] = f"{font_size}"

    return font_module