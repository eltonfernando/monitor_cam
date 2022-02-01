"""
usa apo do telegram para avisar bot

"""
from requests import get,Response,post
import json
import logging

class ApiTelegram():
    def __init__(self) -> None:
        self.log = logging.getLogger(__name__)
        self.token_bot="2133038248:AAF7a-Azb5xm_RDg03_uqs0SpoXHvoP50t8"
        self.chat_id = "991766209"
        self.msg_bot =  ""
    
    def update_id(self)->None:
        url_update = f'https://api.telegram.org/bot{self.token_bot}/getUpdates'
        try:
            result : Response = get(url_update)
            # if result["ok"] is False return result["error_code"]
            if result.status_code !=200:
                data_json = json.loads(result.content)
                self.log.error(data_json["description"])
            else:
                data_json = json.loads(result.content)
                
                #print(json.dumps(data_json, indent=4, sort_keys=True))

                self.chat_id=data_json["result"][-1]["message"]["chat"]["id"]
                msg_bot=data_json["result"][-1]["message"]["text"]
                self.msg_bot=msg_bot.lower()
                 
                            
           # print(result.content)
        except Exception as error:
            print(error)
    
    def get_msg(self)-> str:
        return self.msg_bot

    
    def send_msg(self,msg):
        #msg="olá"

        url = f'https://api.telegram.org/bot{self.token_bot}/sendMessage?chat_id={self.chat_id}&text={msg}'
        try:
            result: Response = post(url)
            if result.status_code != 200:
                data_json = json.loads(result.content)
                self.log.error(data_json["description"])
            else: # bot recebeu msg
                self.log.debug(f"aviso bot {msg}")
        except Exception as error:
            print(error)
      

if __name__ =="__main__":
    print("run")
    ob = ApiTelegram()
    ob.update_id()
    ob.send_msg()