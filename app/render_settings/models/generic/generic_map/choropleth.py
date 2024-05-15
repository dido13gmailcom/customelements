
choroplet:dict = {
    "id":"choropleth",
    "name":"Anàlisi i colors",
    "groups":[
        {
            "name":"Mètode d'agrupació",
            "categories":[
                
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"show_legend",
                            "name":"Mostra/Amaga llegenda",
                            "description":"",
                            "type":"state",
                            "default":"true",
                            "choices":[
                                {"id":"true","name":"Mostra","description":"Mostra la llegenda"},
                                {"id":"false","name":"Amaga","description":"Amaga llegenda"}
                            ]
                        },
                        {
                            "id":"show_title",
                            "name":"Mostra/Amaga títol de la llegenda",
                            "description":"",
                            "type":"state",
                            "default":"true",
                            "choices":[
                                {"id":"true","name":"Mostra","description":"Mostra títol"},
                                {"id":"false","name":"Amaga","description":"Amaga títol"}
                            ]
                        }
                    ]
                },
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"breaks",
                            "name":"Quantitat de breaks (llegenda)",
                            "description":"3 a 10",
                            "type":"integer",
                            "default":"5",
                            "parameters":{
                                "min":"3",
                                "max":"10",
                                "step":"1"
                            }
                        }
                    ]
                },
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"method",
                            "name":"Tipus d'agrupació",
                            "description":"",
                            "type":"state",
                            "default":"l",
                            "choices":[
                                {"id":"j","name":"Jenks Natural Breaks","description":"Llegenda basada en agrupació de Jenks"},
                                {"id":"l","name":"Lineal","description":"Llegenda lineal"},
                                {"id":"q","name":"Quantils","description":"Llegenda segons quantils"}
                            ]
                        }
                    ]
                },
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"colors",
                            "name":"Rampa de colors",
                            "description":"",
                            "type":"state",
                            "default":"Blues",
                            "choices":[
                                {"id":"viridis","name":"Viridis","description":""},
                                {"id":"plasma","name":"Plasma","description":""},
                                {"id":"inferno","name":"Inferno","description":""},
                                {"id":"Blues","name":"Escala de blaus ","description":""},
                                {"id":"Greens","name":"Escala de verds ","description":""},
                                {"id":"Oranges","name":"Escala de taronges ","description":""},
                                {"id":"Purples","name":"Escala de liles ","description":""},
                                {"id":"Reds","name":"Escala de vermells ","description":""},
                                {"id":"YlGnBu","name":"Groc-Verd-Blau","description":""},
                                {"id":"YlOrRd","name":"Groc-Taronja-Vermell","description":""},
                                {"id":"PuBuGn","name":"Lila-Blau-Verd","description":""},
                                {"id":"Spectral","name":"Spectral","description":""},
                                {"id":"Set1","name":"Set 1","description":""},
                                {"id":"Set2","name":"Set 2","description":""},
                                {"id":"Set3","name":"Set 3","description":""}
                                
                            ]
                        }
                    ]
                },
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"opacity",
                            "name":"Transparència (0-100)",
                            "description":"0 a 100",
                            "type":"integer",
                            "default":"100",
                            "parameters":{
                                "min":"0",
                                "max":"100",
                                "step":"1"
                            }
                        }
                    ]
                }     
            ]
        }
    ]
}