

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
                                                "name":"10 Regions (2023)",
                                                "description":"Estableix la capa 2023 com a predeterminada (estàtic)"
                                            },
                                            {
                                                "id":"2018",
                                                "name":"9 Regions (2018)",
                                                "description":"Estableix la capa 2018 com a predeterminada (estàtic)"
                                            },
                                            {
                                                "id":"2017",
                                                "name":"7 Regions (2018)",
                                                "description":"Estableix la capa 2018 com a predeterminada (estàtic)"
                                            }
                                        ]
                                }
                            ]
                        }]
                }
                        
            ]
    }]
    