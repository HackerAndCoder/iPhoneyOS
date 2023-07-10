from actions import *
from app_main_class import App

class SystemApp(App):
    def __init__(self, local_name = 'namenospaces'):
        super().__init__(local_name)
        self.local_name = local_name
    
    def get_result(self, action, data = {}):
        return (Action.NONE, {})
    
    def launch(self):
        return super().launch()