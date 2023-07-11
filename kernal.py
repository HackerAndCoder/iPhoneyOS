import display_api, app_handler, pygame, assets, time, config, image_handler, math, screen
from display_objects import *
from events import *

device_screen = display_api.DeviceScreen()
registered_apps = False
os_core = None

def setup():
    global main_screen, device_screen, external_apps, registered_apps, sys_apps, os_core
    external_apps = app_handler.register_apps()
    sys_apps = app_handler.register_sys_apps()

    for i_key in sys_apps.keys():
        i = sys_apps[i_key]
        if i.local_name == config.get_string('os_core_local_name'):
            os_core = i
            break
    if not os_core:
        Exception('Couldn\'t find operating system core. Exitting...')
    # do all the registering and setup here
    registered_apps = True
    main_handler()

def update_display():
    global os_core
    device_screen._update_display()

def run_action(action, data):
    pass

def handle_events():
    global os_core
    events = device_screen.get_events()
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
            else:
                event_type = EventType.TICK
            return os_core.get_result(event_type, data)

def gen_home_screen():
    screen_num = math.ceil(len(external_apps)/6)
    app_array = [[None]*6 for i in range(screen_num)]
    _home_screen = []
    for i in range(len(app_array)):
        _home_screen.append(screen.Screen())
        _home_screen[i].add_object(DisplayObject(image_handler.get_image('default_background.png')), (0, 0))

    screen_num = 0
    app_location_num = 0

    for app_key in external_apps.keys():
        app = external_apps[app_key]
        app_array[screen_num][app_location_num] = app

        app_display_x = (app_location_num % 3) * 80 + 20
        app_display_y = (app_location_num // 3) * 80 + 20
        
        _home_screen[screen_num].add_object(DisplayObject(app.get_icon()), (app_display_x, app_display_y))

        app_location_num += 1
        if app_location_num > 5:
            screen_num += 1
            app_location_num = 0

    return _home_screen

def main_handler():
    global device_screen

    home_screen = gen_home_screen()

    update_display()
    device_screen.set_screen(assets.startup_screen)
    update_display()
    time.sleep(config.get_int('logo_display_time'))
    device_screen.set_screen(home_screen[0])
    while True:
        update_display()
        raw_action = handle_events()
        if raw_action:
            action, data = raw_action[0], raw_action[1]
            run_action(action, data)

if __name__ == '__main__':
    setup()
