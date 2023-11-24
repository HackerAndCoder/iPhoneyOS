import screen, colors, events, actions

class App:
    '''
    The App class has several rules you must follow.

    the app.local_name varible CANNOT CONTAIN SPACES
    
    The icon_image_name arg in the __init__ function is optional. Use it for declaring a different image than the default for the app.
    If it is not specified, the system will try to load the path {local_name}_icon.png as the icon
    '''
    def __init__(self, local_name = 'insertappnameherenospaces', icon_image_name = None):

        # setup code for the assets like icons and other images that the app uses
        import sys
        sys.path.append('../apps')
        import image_handler


        for char in tuple(local_name):
            if char.isspace():
                print(f'\'{local_name}\' contains a space, which is an illegal character for App.local_name. Exiting...')
                exit(1)
        
        self.local_name = local_name

        self.is_system_app = False

        # this code allows you to load a custom image for an icon but if you don't specify it will load local_name + "_icon". For example "settings_app" + "_icon" is "settings_app_icon" for the image name (no extension)
        if not icon_image_name:
            self.icon_name = local_name + "_icon"
            self.icon_name += '.png'
        else:
            self.icon_name = icon_image_name

        self.icon = image_handler.get_icon_image(self.icon_name)

    def get_app(self):
        return self

    def get_icon(self):
        return self.icon

    def launch(self):
        return screen.Screen(background_color=colors.LIGHT_GREY)

    def get_result(self, event, data):
        #print('paint app running')
        return (actions.Action.NONE, {})