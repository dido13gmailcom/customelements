from render_settings.models.generic.generic_chartjs.get_font_module import get_font_module

y_axis: dict = {
    "id":"y_axis",
    "name":"Eix valors (Y)",
    "groups":[
        {
            "name":"Visibilitat",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"y-show",
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
                            "id":"y-font-size",
                            "name":"Mida del text",
                            "description":"Mida del text de l'eix Y",
                            "type":"integer",
                            "default":"10"
                        },
                        {
                            "id":"y-font-weight",
                            "name":"Tipus de font",
                            "description":"Pes de la font de l'eix Y",
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
                        "id":"y-font-color",
                        "name":"Color de la lletra de l'eix Y",
                        "description":"Color del text",
                        "type":"color",
                        "default":"#191919"
                        }
                    ]
                }    
            ]
        },

        {
            "name":"Títol",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"y-title",
                            "name":"Títol",
                            "description":"",
                            "type":"string",
                            "default":""
                        },
                        {
                            "id":"y-title-font-size",
                            "name":"Mida del text",
                            "description":"Mida del text de l'eix Y",
                            "type":"integer",
                            "default":"10"
                        },
                        {
                            "id":"y-title-font-weight",
                            "name":"Tipus de font",
                            "description":"Pes de la font de l'eix Y",
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
                        "id":"y-title-font-color",
                        "name":"Color de la lletra de l'eix Y",
                        "description":"Color del text",
                        "type":"color",
                        "default":"#000000"
                        }
                    ]
                }    
            ]
        },

        {
            "name":"Valors límit de l'eix Y",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"y-lim-inf",
                            "name":"Valor inferior (decimal amb .)",
                            "description":"Números: decimal amb .",
                            "type":"string",
                            "default":""
                        },
                        {
                            "id":"y-lim-sup",
                            "name":"Valor superior (decimal amb .)",
                            "description":"Números: decimal amb .",
                            "type":"string",
                            "default":""
                        }
                    ]
                }    
            ]
        },

        {
            "name":"Intercanvia eixos",
            "categories":[
                {
                    "name":"",
                    "description":"",
                    "properties":[
                        {
                            "id":"y-reverse",
                            "name":"Intercanvia Y per X",
                            "description":"Intercanvia la posició de l'eix Y, que passa a posició horitzontal",
                            "type":"boolean",
                            "default":"false"
                        }
                    ]
                }    
            ]
        }
    ]
}