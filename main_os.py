import display_api, app_handler, pygame, assets, time, config

device_screen = display_api.DeviceScreen()
events = []

def setup():
    global main_screen, device_screen
    external_apps = app_handler.register_apps()
    # do all the registering and setup here

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
    home_screen = assets.home_screen
    

def main_handler():
    global device_screen, events
    update_display()
    device_screen.set_screen(assets.startup_screen)
    update_display()
    time.sleep(config.get_int('logo_display_time'))
    device_screen.set_screen(assets.home_screen)
    while True:
        update_display()


if __name__ == '__main__':
    setup()