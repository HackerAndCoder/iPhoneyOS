import display_api, app_handler, pygame, assets, time, config, image_handler, math, screen
from display_objects import *
# temp
import random

device_screen = display_api.DeviceScreen()
events = []
registered_apps = False

def setup():
    global main_screen, device_screen, external_apps, registered_apps, sys_apps 
    external_apps = app_handler.register_apps()
    sys_apps = app_handler.register_sys_apps()
    # do all the registering and setup here
    registered_apps = True
    main_handler()
    

def handle_render():
    global events, device_screen
    while True:
        update_display()

def update_display():
    device_screen._update_display()
    events = device_screen.get_events()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

def start_device_screen_loop():
    global device_screen
    device_screen.display_loop()

def gen_home_screen():
    screen_num = math.ceil(len(external_apps)/6)
    app_array = [[None]*6 for i in range(screen_num)]
    _home_screen = []
    for i in range(len(app_array)):
        _home_screen.append(screen.Screen())
        _home_screen[i].add_object(DisplayObject(image_handler.get_image('default_background.png')), (0, 0))

    screen_num = 0
    app_location_num = 0

    for app in external_apps:
        app_array[screen_num][app_location_num] = app

        app_display_x = (app_location_num % 3) * 80 + 20
        app_display_y = (app_location_num // 3)*80 + 20
        
        _home_screen[screen_num].add_object(DisplayObject(app.get_icon()), (app_display_x, app_display_y))

        app_location_num += 1
        if app_location_num > 6:
            screen_num += 1
            app_location_num = 0

    return _home_screen

def main_handler():
    global device_screen, events

    home_screen = gen_home_screen()

    update_display()
    device_screen.set_screen(assets.startup_screen)
    update_display()
    time.sleep(config.get_int('logo_display_time'))
    device_screen.set_screen(home_screen[0])
    while True:
        update_display()


if __name__ == '__main__':
    setup()