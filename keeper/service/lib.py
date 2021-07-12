class Singleton:
    _instances = {}

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)

        return cls._instances[cls]
