

settings: dict = [{
    "id":"tiles",
    "name":"Mapa de fons",
    "groups":[
        {
            "name":"Visibilitat",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"tile",
                            "name":"Selecciona mapa de fons",
                            "description":"",
                            "type":"state",
                            "default":"CartoDB Positron",
                            "choices":[
                                {
                                    "id":"CartoDB Positron",
                                    "name":"CartoDB Positron",
                                    "description":""
                                },
                                {
                                    "id":"OpenStreetMap",
                                    "name":"OpenStreetMap",
                                    "description":""
                                }
                            ]
                        }
                    ]
                }    
            ]
        }
    ]
}]