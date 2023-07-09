from image_handler import *
from display_objects import *
from screen import *
from config import *
from colors import *

# images and text initialized here
logo = DisplayObject(image=resize_image(get_image('iphoneyos.png'), (100, 100)))
background = DisplayObject(image=resize_image(get_image('default_background.png'), (get_int('display_width'), get_int('display_height'))))

# screens initialized here
startup_screen = Screen(origin='main', name='startup')
startup_screen.add_object(logo, (get_int('display_width') // 2 - 50, get_int('display_height') // 2 - 50), ScreenImportance.FOREGROUND)

home_screen = Screen(origin='main', name='home')
home_screen.set_background_color(BLACK)