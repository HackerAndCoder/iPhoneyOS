import system_app_class, actions

class OS(system_app_class.SystemApp):
    def __init__(self, local_name='os'):
        super().__init__(local_name)
    
    def get_result(self, action, data={}):
        return super().get_result(action, data)
    