class Singleton:
    """
    Basic singleton class.
    Inherit from it to ensure your class will have only one instance at a time.
    """
    _instances = {}

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)

        return cls._instances[cls]
