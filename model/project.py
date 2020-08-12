
class Project:

    def __init__(self, name=None, status="development", enabled=True, view_state="public", description=None):
            self.name = name
            self.status = status
            self.enabled = enabled
            self.view_state = view_state
            self.description = description

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)