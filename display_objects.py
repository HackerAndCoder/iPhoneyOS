import colors, pygame.font, image_handler, pygame

pygame.font.init()

class DisplayObject:
    def __init__(self):
        self.to_display = None

class DisplayText(DisplayObject):
    def __init__(self, text='', size = 10, font=None, color = colors.BLACK):
        super().__init__()
        self.font = font
        self.text = text
        self.text_size = size
        self.color = color
        self._font = pygame.font.SysFont(self.font, self.text_size)
        self.to_display = self._font.render(self.text, False, self.color)

class DisplayImage(DisplayObject):
    def __init__(self, image = image_handler.get_image('no_icon.png'), scale = 1):
        super().__init__()
        self.image = image
        self.to_display = None
        self.scale = scale
        self._update()
    
    def _update(self):
        self.to_display = pygame.transform.scale(self.image, (self.scale, self.scale))
    
    def set_image(self, image):
        try:
            self.image = image
        except:
            print('Error changin display image')
        self._update()
    
    def set_scale(self, scale):
        self.scale = scale
        self._update()
