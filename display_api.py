import pygame, screen, colors

pygame.init()

class DeviceScreen:
    def __init__(self, size = (240, 320)):
        self.events = []
        self.screen = None
        self.size = size
        self.update = True
        self.display = pygame.display.set_mode(size)
        self.fps_clock = pygame.time.Clock()

    def display_loop(self):
        while self.update:
            self.fps_clock.tick(30)
            self._update_display()

    def _update_display(self):
        self.display.fill(colors.WHITE)
        if self.screen:
            self.display.blit(self.screen.get_render(), (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():
            self.events.append(event)

    def get_events(self):
        events = self.events.copy()
        self.events.clear()
        return events
    
    def set_screen(self, screen : screen.Screen):
        self.screen = screen
    
    def quit(self):
        pygame.quit()