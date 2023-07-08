import colors, pygame.font

pygame.font.init()

class DisplayObject:
    def __init__(self, image = None):
        self.image = image
        self.to_display = image

class DisplayText:
    def __init__(self, text='', size = 10, font=None, color = colors.BLACK):
        self.font = font
        self.text = text
        self.text_size = size
        self.color = color
        self._font = pygame.font.SysFont(self.font, self.text_size)
        self.to_display = self._font.render(self.text, False, self.color)