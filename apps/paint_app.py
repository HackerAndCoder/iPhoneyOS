import app_main_class, screen

class Paint(app_main_class.App):
    def __init__(self):
        super().__init__('paint')
        self.main_screen = screen.Screen()
    
    def launch(self):
        return super().launch()

app = Paint()