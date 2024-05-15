import polars as pl

class Lines:
    def __init__(self, Feed = None) -> None:
        self.feed = Feed
        
    def get_data(self):
        
        feed_df = self._parse_dataframe()
        return {}
    
    def get_options(self):
        
        if len(self.feed.json_feed['settings']) == 0:
            pass
        else:
            pass
        
        return {}
    
    def _parse_dataframe(self):
        
        feeding = self.feed.json_feed['feeding']
    
        legend_id = feeding[2].get('expressions')
        if legend_id != None: legend_id = legend_id[0].get('dataId')
        
        y_axis_id = feeding[1].get('expressions')[0].get('dataId')
        x_axis_id = feeding[0].get('expressions')[0].get('dataId')
        
        
        legend_values   = []
        y_values        = []
        x_values        = []
        
        
        
        
        
        return False
        

    

    