from actions import Action

class SystemApp:
    def __init__(self, local_name = 'namenospaces'):
        self.local_name = local_name
        self.is_system_app = True
    
    def get_result(self, event, data = {}):
        return (Action.NONE, {})
    
    def launch(self):
        return None