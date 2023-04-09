import threading
import time
import singleton
from roblox import RobloxAPI
from gui import main as gui_main
roblox_api = RobloxAPI()

def verify_key():
    return roblox_api.login()

def set_cookie(cookie):
    return roblox_api.set_cookie(cookie)

def join_game(place_id):
    return roblox_api.join_game(place_id)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Bot(metaclass=Singleton):
    def __init__(self):
        self.cookie_jar = None
        self.stop_event = threading.Event()

    def start(self, username, password):
        self.stop_event.clear()
        self.cookie_jar = Roblox.login(username, password)
        t = threading.Thread(target=self.run)
        t.start()

    def stop(self):
        self.stop_event.set()

    def run(self):
        roblox = Roblox(self.cookie_jar)
        while not self.stop_event.is_set():
            # TODO: add botting logic here
            time.sleep(1)


if __name__ == '__main__':
    gui_main()
