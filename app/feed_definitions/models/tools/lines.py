

definition:dict = {
        "feeds":[
            {
                "id": "x-axis",
                "name": "▰ Dimensions",
                "description": "Eix X de la gràfica. Solament accepta variables tipus dimensió (obligatori)",
                "axis":"0",
                "type":"dimension",
                "min": "1",
                "max":"1"
            },
            {
                "id": "y-axis",
                "name": "📏 Indicador",
                "description": "Eix Y de la gràfica. Solament accepta variables tipus indicador (obligatori)",
                "type": "measure",
                "min": "1",
                "max": "1"
            },
            {
                "id": "legend",
                "name": "Llegenda",
                "description": "Estableix els colors de la llegenda en base a una dimensió (opcional)",
                "axis":"1",
                "type":"dimension",
                "min": "0",
                "max":"1"
            }
            
        ]
    }