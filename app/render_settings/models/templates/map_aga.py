

settings: dict = [{
            "id":"version",
            "name":"Versió de la capa",
            "groups":[
                {
                    "name":"Versió",
                    "categories":[
                        {
                            "name":"",
                            "description":"",
                            "properties":[
                                {
                                    "id":"versio",
                                    "name":"Versió de la capa",
                                    "description":"Va a l'uníson amb les dimensions versionades de l'univers",
                                    "type":"state",
                                    "default":"v",
                                    "choices":[
                                            {
                                                "id":"v",
                                                "name":"Vigent",
                                                "description":"Agafa l'última capa disponible (dinàmic)"
                                            },
                                            {
                                                "id":"2023",
                                                "name":"Distribució 2023 (10 Regions)",
                                                "description":"Estableix la capa 2023 com a predeterminada (estàtic)"
                                            },
                                            {
                                                "id":"2018",
                                                "name":"Distribució 2018 (7 i 9 Regions)",
                                                "description":"Estableix la capa 2018 com a predeterminada (estàtic)"
                                            }
                                        ]
                                }
                            ]
                        }]
                }
                        
            ]
    }]
    