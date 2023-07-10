import pygame, screen, colors

pygame.init()

class DeviceScreen:
    def __init__(self, size = (240, 320)):
        self.events = []
        self.size = size
        self.update = True
        self.display = pygame.display.set_mode(size)
        self.fps_clock = pygame.time.Clock()
        self._clear_screen()

        pygame.display.set_caption("iPhoney OS")

    def display_loop(self):
        while self.update:
            self.fps_clock.tick(30)
            self._update_display()

    def _update_display(self):
        self.display.fill(colors.WHITE)
        self.display.blit(self.screen.get_render(), (0, 0))
        pygame.display.flip()

        # handle events 
        for event in pygame.event.get():
            self.events.append(event)

    def get_events(self):
        events = self.events.copy()
        self.events.clear()
        return events
    
    def _clear_screen(self):
        self.screen = screen.Screen(origin='blank', name='blank', background_color=colors.AQUA)
    
    def set_screen(self, screen):
        self._clear_screen()
        self.screen = screen
        #print(f'set screen to {self.screen.name}') # debug
    
    def quit(self):
        pygame.quit()