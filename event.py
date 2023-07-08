class EventType:
    FINGER_DOWN = 0
    FINGER_UP = 1
    FINGER_MOVE = 2 # unused 

class Event:
    def __init__(self, type = None, args = {}):
        self.type = type
        self.args = args