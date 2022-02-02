from .api import ApiTelegram
from .client import FileConfig
import threading
import os
class Bot():
    def __init__(self) -> None:
   
        self.chat_id = ""
        self.name_cliente = ""
    
    def add_new_cliente(self,comboBox):
        self.task = threading.Thread(target=self.__resistre_cliente,args=(comboBox,))
        self.task.start()
        #self.task.join()


    def __resistre_cliente(self,comboBox):
        api_bot = ApiTelegram()
        api_bot.update_id()

        name_cliente = api_bot.get_first_name()
        chat_id = api_bot.get_id()
        msg = api_bot.get_msg()
        if name_cliente == "":
            print("api name", name_cliente)
        else:
            if msg.endswith("start"):
                data = FileConfig(name_cliente)
                data.set_id_user(chat_id)
                comboBox.addItem(name_cliente)
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
   
    def alert_user(self,msg):
        dir_base = os.path.join("monitor","telegram","config")
        list_name_file = os.listdir(dir_base)
        if len(list_name_file)>0:
            for name_file in list_name_file:
                if name_file.endswith(".json"):
                    self.load_data_cliente(name_file)
                    name_cliente = name_file.replace(".json","")
                    api_bot = ApiTelegram()
                    api_bot.set_id(self.chat_id)
                    api_bot.send_msg(f'Oi {name_cliente}! {msg}')

