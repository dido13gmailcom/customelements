from uuid import uuid4

def add_id(settings: dict) -> dict:
    
    id:str = str(uuid4())[:8]
    
    settings["regions"][0]["groups"][0]["categories"][0]["properties"][0]["default"] = id
    
    return settings
     
    