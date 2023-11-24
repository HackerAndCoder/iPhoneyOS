import system_main_class, screen, config, events, actions, math, colors, image_handler, display_objects

class OS(system_main_class.SystemApp):
    def __init__(self):
        super().__init__(config.get_string('os_core_local_name'))
        self.finger_down_init_pos = None
        self.startup = None

    def get_result(self, event, data={}):
        if self.startup:
            return (actions.Action.UPDATE_SCREEN, {'screen': self.base_screen})
        
        self.startup = False

        if event == events.EventType.FINGER_DOWN:
            self.finger_down_init_pos = data['pos']
        
        elif event == events.EventType.FINGER_UP:
            touch_x = data['pos'][0]
            touch_y = data['pos'][1]
            x = math.floor(config.get_int('display_width') // touch_x)
            y = math.floor(config.get_int('display_width') // touch_y) # if your wondering why its using display width instead of heaight the app grid is 3 x 3 and there is a bit of space on the bottom

        
        return super().get_result(event, data)
    
    def launch(self):
        self.startup = True
        self.background_image = image_handler.get_image(config.get_string('user_set_background'))
        self.base_screen = screen.Screen()
        self.base_screen.add_object(display_objects.DisplayImage(self.background_image))

app = OS()