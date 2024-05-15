# Exemple i plantilla bàsica alhora d'inicialitzar una classe de visualització


class Vizualization_basic_Template:
    def __init__(self, Feed = None) -> None:
        self.Feed = Feed
        
    def get_data(self):
        return {}
    
    def get_options(self):
        return {}