import system_main_class, screen, config

class OS(system_main_class.SystemApp):
    def __init__(self):
        super().__init__(config.get_string('os_core_local_name'))
    
    def get_result(self, event, data={}):
        return super().get_result(event, data)
    
    def launch(self):
        return super().launch()

app = OS()