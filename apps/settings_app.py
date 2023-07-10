import app_main_class, screen

class Settings(app_main_class.App):
    def __init__(self):
        super().__init__('settings')
        self.main_screen = screen.Screen()

    
    def launch(self):
        return super().launch()

app = Settings()