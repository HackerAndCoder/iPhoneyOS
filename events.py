import pygame

class EventType:
    FINGER_DOWN = 0
    FINGER_UP = 1
    FINGER_MOVE = 2
    NULL = 3
    QUIT = 4
    TICK = 5

class Event:
    def __init__(self, type = None, args = {}):
        self.type = type
        self.args = args

def get_event_type(event):
    if event.type == pygame.MOUSEBUTTONDOWN: return EventType.FINGER_DOWN
    if event.type == pygame.MOUSEBUTTONUP: return EventType.FINGER_UP
    if event.type == pygame.MOUSEMOTION: return EventType.FINGER_MOVE
    if event.type == pygame.QUIT: return EventType.QUIT