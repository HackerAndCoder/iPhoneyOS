import pygame, display_objects, config, colors

class ScreenImportance:
    BACKGROUND = 0
    FOREGROUND = 1

class Screen:
    def __init__(self, origin = 'default', name = 'default', size = None, objects = [], background_color = colors.WHITE):
        self.origin = origin
        self.name = name
        self.objects = objects
        self.background_color = background_color
        self._name = f'{self.origin}:{self.name}'
        if not size:
            self.size = (config.get_int('display_width'), config.get_int('display_height'))
        else:
            self.size = size
    
    def add_object(self, object : display_objects.DisplayObject, pos = (0, 0), importance = ScreenImportance.BACKGROUND):
        self.objects.append([object, pos, importance])
        return True
    
    def set_background_color(self, color):
        self.background_color = color
    
    def clear(self):
        self.objects = []
    
    def get_objects(self):
        return self.objects
    
    def get_render(self):
        render = pygame.Surface(self.size)
        render.fill(self.background_color)
        display_list = {"background": [], "foreground": []}
        for i in self.objects:
            if i[2] == ScreenImportance.BACKGROUND:
                display_list['background'].append(i)
            elif i[2] == ScreenImportance.FOREGROUND:
                display_list["foreground"].append(i)
        for i in display_list['background']:
            render.blit(i[0].to_display, i[1])
        for i in display_list['foreground']:
            render.blit(i[0].to_display, i[1])

        return render