import system_main_class, screen

class OS(system_main_class.SystemApp):
    def __init__(self):
        super().__init__('os')
    
    def launch(self):
        return super().launch()

app = OS()