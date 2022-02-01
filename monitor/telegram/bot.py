from .api import ApiTelegram
from .client import FileConfig
import threading

class Bot():
    def __init__(self) -> None:
        self.chat_id = ""
        self.name_cliente = ""
    
    def add_new_cliente(self):
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
    def load_data_cliente(self, name_file):
        data = FileConfig(name_file)
        self.chat_id = data.get_id_user()
        self.name_cliente = name_file

    
    def del_cliente_file(self,name_cliente):
        data = FileConfig(name_cliente)
        data.del_file()
    
    def teste_msg(self,name_file):
        if self.chat_id == "":
            self.load_data_cliente(name_file)

        api_bot = ApiTelegram()
        api_bot.set_id(self.chat_id)
        msg = f"Oi {self.name_cliente}! essa é uma message de teste"
        api_bot.send_msg(msg)