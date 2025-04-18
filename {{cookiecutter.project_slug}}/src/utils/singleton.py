import threading

class SingletonMeta(type):
    """A threadsafe MetaClass based Singleton pattern.

        Usage:

        class MyClass(metaclass=SingletonMeta):
            pass
    """
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
