import app_main_class, screen

class Paint(app_main_class.App):
    def __init__(self):
        super().__init__('paint')
        self.main_screen = screen.Screen()
    
    def launch(self):
        return super().launch()
    
    def get_result(event, data):
        return super().get_result(event, data)

app = Paint()