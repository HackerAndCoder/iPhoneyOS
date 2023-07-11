import app_main_class, screen

class SMS(app_main_class.App):
    def __init__(self):
        super().__init__('sms')
        self.main_screen = screen.Screen()
    
    def launch(self):
        return super().launch()
    
    def get_result(event, data):
        return super().get_result(event, data)

app = SMS()