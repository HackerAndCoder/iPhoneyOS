from actions import *

class SystemApp:
    def __init__(self, local_name = 'namenospaces'):
        self.local_name = local_name
    
    def get_result(self, action, data = {}):
        return (Action.NONE, {})