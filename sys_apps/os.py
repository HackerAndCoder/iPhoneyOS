import system_main_class, actions, screen, colors

class OS(system_main_class.SystemApp):
    def __init__(self):
        super().__init__('os')
        self.local_name = 'os'
    
    def get_result(self, action, data={}):
        return super().get_result(action, data)
    
    def launch(self):
        return super().launch()

app = OS()