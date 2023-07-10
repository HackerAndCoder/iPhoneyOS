import display_api, app_handler, pygame, assets, time, config, display_objects, image_handler, math

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
    for i in range(0, screen_num, 6):
        print(i)
    print(app_array)
    print(sys_apps[0].local_name)

    return sys_apps[0].launch()

def main_handler():
    global device_screen, events

    home_screen = gen_home_screen()

    update_display()
    device_screen.set_screen(assets.startup_screen)
    update_display()
    time.sleep(config.get_int('logo_display_time'))
    device_screen.set_screen(home_screen)
    while True:
        update_display()


if __name__ == '__main__':
    setup()