from render_settings.models.generic.generic_chartjs.get_font_module import get_font_module

x_axis: dict = {
    "id":"x_axis",
    "name":"Eix categòric (x)",
    "groups":[
        {
            "name":"Visibilitat",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"x-show",
                            "name":"Mostra/Amaga",
                            "description":"",
                            "type":"state",
                            "default":"true",
                            "choices":[
                                {
                                    "id":"true",
                                    "name":"Mostra",
                                    "description":""
                                },
                                {
                                    "id":"false",
                                    "name":"Amaga",
                                    "description":""
                                }
                            ]
                        },
                        {
                            "id":"x-font-size",
                            "name":"Mida del text",
                            "description":"Mida del text de l'eix X",
                            "type":"integer",
                            "default":"10"
                        },
                        {
                            "id":"x-font-weight",
                            "name":"Tipus de font",
                            "description":"Pes de la font de l'eix X",
                            "type":"state",
                            "default":"lighter",
                            "choices":[
                                {
                                    "id":"lighter",
                                    "name":"Lleuger",
                                    "description":""
                                },
                                {
                                    "id":"normal",
                                    "name":"Normal",
                                    "description":""
                                },
                                {
                                    "id":"bold",
                                    "name":"Negreta",
                                    "description":""
                                }
                            ]
                        },
                        {
                        "id":"x-font-color",
                        "name":"Color de la lletra de l'eix X",
                        "description":"Font color",
                        "type":"color",
                        "default":"#191919"
                        }
                    ]
                }    
            ]
        },

        {
            "name":"Títol Eix",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"x-title",
                            "name":"Títol",
                            "description":"",
                            "type":"string",
                            "default":""
                        },
                        {
                            "id":"x-title-font-size",
                            "name":"Mida del text",
                            "description":"Mida del text de l'eix X",
                            "type":"integer",
                            "default":"10"
                        },
                        {
                            "id":"x-title-font-weight",
                            "name":"Tipus de font",
                            "description":"Pes de la font de l'eix X",
                            "type":"state",
                            "default":"bold",
                            "choices":[
                                {
                                    "id":"lighter",
                                    "name":"Lleuger",
                                    "description":""
                                },
                                {
                                    "id":"normal",
                                    "name":"Normal",
                                    "description":""
                                },
                                {
                                    "id":"bold",
                                    "name":"Negreta",
                                    "description":""
                                }
                            ]
                        },
                        {
                        "id":"x-title-font-color",
                        "name":"Color de la lletra de l'eix X",
                        "description":"Color del text",
                        "type":"color",
                        "default":"#000000"
                        }
                    ]
                }
                
            ]
        },

        {
            "name":"Força categories (separat per |)",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"x-category-force",
                            "name":"Llista de categories",
                            "description":"Força l'aparició de les categories especificades tot i que no presentin valors en les dades",
                            "type":"string",
                            "default":""
                        }
                    ]
                }    
            ]
        },

        {
            "name":"Valors límit de l'eix X",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"x-lim-inf",
                            "name":"Valor inferior",
                            "description":"Números: decimal amb .",
                            "type":"string",
                            "default":""
                        },
                        {
                            "id":"x-lim-sup",
                            "name":"Valor superior",
                            "description":"Números: decimal amb .",
                            "type":"string",
                            "default":""
                        }
                    ]
                }    
            ]
        }
    ]
}