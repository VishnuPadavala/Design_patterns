import threading
class student:
    _instance=None
    _lock=threading.Lock()
    def __init__(self):
        self.college="aditya"
        self.address="Surampalem"
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance=student()
        return cls._instance
    