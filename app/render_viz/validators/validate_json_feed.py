

def validate_json_feed(json_feed:dict) -> list:
    """
    Retorna una llista dels possibles errors que
    pugui tenir el Request Body enviat pel BO pel que
    fa les dades tipus Feed

    Args:
        json_feed (dict): 

    Returns:
        errors (list):  llista amb els errors detectats. 
                        Si len(result) = 0, no hi ha errors 
                        aparentment...
    """

    errors: list = []

    if len(json_feed) == 0:
        errors.append("No hi ha dades")

    if not isinstance(json_feed,dict):
        errors.append("L'objecte d'entrada no està ben formatat")

    return errors