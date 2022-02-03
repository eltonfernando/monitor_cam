"""
usa apo do telegram para avisar bot

"""
from requests import get, Response, post
import json
import logging
import os


class ApiTelegram():
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        if not os.path.isfile("token_bot.txt"):
            raise ("não achei token_bot.txt")

        self.token_bot = open("token_bot.txt", encoding="utf-8").read().strip()
        self.chat_id = ""
        self.msg_bot = ""
        self.first_name = ""

    def update_id(self) -> None:
        print("update id")
        url_update = f'https://api.telegram.org/bot{self.token_bot}/getUpdates'
        try:
            result: Response = get(url_update)
            # if result["ok"] is False return result["error_code"]
            if result.status_code != 200:
                data_json = json.loads(result.content)
                self.log.error(data_json["description"])
            else:
                data_json = json.loads(result.content)

                # print(json.dumps(data_json, indent=4, sort_keys=True))

                self.chat_id = str(data_json["result"][-1]["message"]["chat"]["id"])
                self.first_name = data_json["result"][-1]["message"]["chat"]["first_name"]  # so para privado
                msg_bot = data_json["result"][-1]["message"]["text"]
                self.msg_bot = msg_bot.lower()
                print("tes name bdb", self.first_name)


        # print(result.content)
        except Exception as error:
            print(error)

    def get_msg(self) -> str:
        return self.msg_bot

    def get_first_name(self):
        return self.first_name

    def get_id(self):
        return self.chat_id

    def set_id(self, chat_id):
        self.chat_id = chat_id

    def send_msg(self, msg):
        # msg="olá"

        url = f'https://api.telegram.org/bot{self.token_bot}/sendMessage?chat_id={self.chat_id}&text={msg}'
        try:
            result: Response = post(url)
            if result.status_code != 200:
                data_json = json.loads(result.content)
                self.log.error(data_json["description"])
            else:  # bot recebeu msg
                self.log.debug(f"aviso bot {msg}")
        except Exception as error:
            print(error)


if __name__ == "__main__":
    print("run")
    ob = ApiTelegram()
    ob.update_id()
    ob.send_msg("oi")
