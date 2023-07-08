import app_main_class

class Settings(app_main_class.App):
    def __init__(self):
        super().__init__('settings')

app = Settings()