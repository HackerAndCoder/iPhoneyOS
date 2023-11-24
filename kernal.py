import display_api, app_handler, pygame, assets, time, config, image_handler, math, screen
from display_objects import *
from events import *
from actions import Action

# temp
import random

device_screen = display_api.DeviceScreen()
registered_apps = False
os_core = None
home_screen = None
external_apps = []

def setup():
    global main_screen, device_screen, external_apps, registered_apps, sys_apps, os_core, current_running_app, home_screen
    external_apps = app_handler.register_apps()
    sys_apps = app_handler.register_sys_apps()

    for i_key in sys_apps.keys():
        i = sys_apps[i_key]
        if i.local_name == config.get_string('os_core_local_name'):
            os_core = i
            current_running_app = os_core
            break
    if not os_core:
        Exception('Couldn\'t find operating system core. Exitting...')
    # do all the registering and setup here
    registered_apps = True

    main_handler()

def update_display():
    global os_core
    device_screen._update_display()

def get_current_app():
    return current_running_app

def set_current_running_app(app):
    global current_running_app
    current_running_app = app

def run_action(action, data):
    if action == Action.LAUNCH_APP:
        if data['name'] in external_apps.keys():
            external_apps[data['name']].launch()
            set_current_running_app(external_apps[data['name']])
    elif action == Action.EXIT_APP:
        set_current_running_app(os_core)
        get_current_app().launch()
    
    elif action == Action.UPDATE_SCREEN:
        device_screen.set_screen(data['screen'])

def handle_events():
    global os_core, current_running_app
    events = device_screen.get_events()

    event_type = EventType.TICK
    data = {}

    if events:
        for event in events:
            event_type = get_event_type(event)
            data = {}
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event_type == EventType.FINGER_DOWN:
                data = {"pos": event.pos}
            elif event_type == EventType.FINGER_UP:
                data = {"pos": event.pos}
            elif event_type == EventType.FINGER_MOVE:
                data = {"pos": event.pos, "rel": event.rel}
    
    return current_running_app.get_result(event_type, data)

def main_handler():
    global device_screen

    update_display()
    device_screen.set_screen(assets.startup_screen)
    update_display()
    time.sleep(config.get_int('logo_display_time'))
    os_core.launch()
    while True:
        update_display()
        raw_action = handle_events()
        if raw_action:
            action, data = raw_action[0], raw_action[1]
            try:
                run_action(action, data)
            except:
                print('Error in running action!')

if __name__ == '__main__':
    setup()