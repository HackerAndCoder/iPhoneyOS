from image_handler import *
from display_objects import *
from screen import *
from config import *

# images and text initialized here
logo = DisplayObject(image=resize_image(get_image('iphoneyos.png'), (100, 100)))


# screens initialized here
startup_screen = Screen(origin='main', name='startup')
startup_screen.add_object(logo, (int(get_value('display_width')) // 2 - 50, int(get_value('display_height')) // 2 - 50))