class SingletonCreateMixin:

    instances = {}

    @classmethod
    def create(cls):
        if cls in cls.instances:
            return cls.instances[cls]
        instance = cls()
        cls.instances[cls] = instance
        return instance
