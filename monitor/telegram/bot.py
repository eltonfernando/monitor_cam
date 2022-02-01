from .api import ApiTelegram
from .client import FileConfig
import threading
class Bot():
    def __init__(self) -> None:
        pass
    
    def find_cliente(self):
        self.task = threading.Thread(target=self.__resistre_cliente,args=())
        self.task.start()

    def __resistre_cliente(self):
        api_bot = ApiTelegram()
        api_bot.update_id()

        name_cliente = api_bot.get_frist_name()
        chat_id = api_bot.get_id()
        msg = api_bot.get_msg()
        if name_cliente is "":
            print("api telegram nao retornou corretamente")
        else:
            if msg.endswith("start"):
                data = FileConfig(name_cliente)
                data.set_id_user(chat_id)
            else:
                print("não é start ", msg)
