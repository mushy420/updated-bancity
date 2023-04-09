import requests
import time
import singleton


class RobloxAPI:
    def __init__(self):
        self.cookie_jar = None

    def login(self):
        while True:
            bancity_key = input("Please enter your Bancity key: ")
            r = requests.post("https://api.bancity.xyz/v1/verify_key", json={"key": bancity_key})
            if r.status_code == 200:
                print("Bancity key verification successful. Continuing...")
                return True
            else:
                print("Bancity key verification failed. Please try again.")
                continue

    def set_cookie(self, cookie):
        self.cookie_jar = cookie

    def join_game(self, place_id):
        if self.cookie_jar is None:
            print("Error: Cookie jar is not set.")
            return False
        else:
            r = requests.post(f"https://www.roblox.com/game/join.ashx?placeid={place_id}", cookies=self.cookie_jar)
            if r.status_code == 200:
                print("Join request sent.")
                while True:
                    r = requests.get(f"https://www.roblox.com/games/getgameinstancejson?placeId={place_id}", cookies=self.cookie_jar)
                    data = r.json()
                    if data['Message'] == "":
                        print(f"Joined game {data['Title']}.")
                        return True
                    else:
                        print(f"Joining game... {data['Message']}")
                        time.sleep(5)
            else:
                print("Join request failed.")
                return False


roblox_api = RobloxAPI()


def verify_key():
    return roblox_api.login()


def set_cookie(cookie):
    return roblox_api.set_cookie(cookie)


def join_game(place_id):
    return roblox_api.join_game(place_id)
