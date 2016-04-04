class Config(dict):
    def __init__(self, from_object=None, **data):
        super(Config).__init__(**data)

        if from_object:
            self.from_object(from_object)

    """Hug and Rest config class"""
    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
