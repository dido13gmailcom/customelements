

class NotReady:
    
    def __init__(self, Feed) -> None:
        self.feed = Feed
        
        
    def get_html(self):
        
        # Iniciem en estat not_ready
        template    = self.feed.html_templates.get_template("not_ready.html")
        required_items =    self._get_required_items()
        description = self._get_description()
        additional_info = self._get_additional_info()
        
        html        = template.render(data = self.feed.visualization,
                                      required_items = required_items,
                                      description = description,
                                      info = additional_info)
        
        return html
    
    def _get_description(self):

        target_viz = filter(lambda x: x['id'] == self.feed.id,self.feed.viz_types)
        target_viz = list(target_viz)[0]
        description = target_viz['description']

        return description
    
    def _get_required_items(self):

        ok = "<span style='color:#65B741;font-size:1.5rem;margin:0 1rem 0.4rem 0'>🗸</span>"
        ko = "<span style='color:#750E21;font-size:1.5rem;margin:0 1.3rem 0.4rem 0'>x</span>"
        op = "<span style='color:#5755FE;font-size:1.5rem;margin:0 1.3rem 0.4rem 0'>~</span>"

        defined_feeds = self.feed.feed_definitions['feeds']
        required_fields = []
        
        try:

            for field in defined_feeds:
                
                id_to_find = field["id"]

                min_expressions = int(field['min'])
                n_expressions = 0
                
                msg = ko
                if min_expressions == 0:
                    msg = op

                submitted_feeds = self.feed.json_feed['feeding']

                feed_submitted = [feed for feed in submitted_feeds if feed["id"] == id_to_find][0]

                if 'expressions' in feed_submitted.keys():
                    n_expressions = len(feed_submitted["expressions"]) 

                    if n_expressions >= min_expressions:
                        msg = ok
                    else:
                        msg = ko
                else:
                    n_expressions = 0

                req = {
                    'id':field['id'],
                    'desc':f"{field['description']} ({n_expressions}/{min_expressions})",
                    'check':msg
                }
                required_fields.append(req)     
                        
        except Exception as e:
            print(f"Feed._get_required_items(): {e}")
                
        return required_fields
    
    def _get_additional_info(self):
        
        available_viz = self.feed.viz_types 
        target_id = self.feed.id
        
        viz_info = [dict(x)["info"] for x in available_viz if dict(x)["id"] == target_id][0]
        
        return viz_info
    
