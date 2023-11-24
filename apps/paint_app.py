import app_main_class, screen, colors, sys
sys.path.append('../apps')
import actions

class Paint(app_main_class.App):
    def __init__(self):
        super().__init__('paint')
        self._init()
    
    def _init(self):
        self.main_screen = screen.Screen(background_color=colors.WHITE)
    
    def launch(self):
        self._init()
        return super().launch()
    
    def get_result(self, event, data):
        return (actions.Action.UPDATE_SCREEN, {'screen': self.main_screen})

app = Paint()