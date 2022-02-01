import json
import logging
import os
class FileConfig():
    def __init__(self,path_file_config : str) -> None:
        
        self.log = logging.getLogger(__name__)
        
        self.dir_base = os.path.join("monitor","telegram","config")
        if not os.path.isdir(self.dir_base):
            raise (self.dir_base)
        if not path_file_config.endswith('.json'):
            path_file_config = path_file_config+".json"

        self.path_file_config = os.path.join(self.dir_base, path_file_config)
        self.current_data = {}
        self.read_data()
    
    def set_id_user(self,id_user):
        self.current_data["id"]= id_user
        self.write_data()

    def get_id_user(self):
        if "id" in self.current_data:
            return self.current_data["id"]
        else:
            return ""
    
    def read_data(self):
        try:
            with open(self.path_file_config, encoding="utf-8") as file:
                self.current_data = json.load(file)
        except Exception as erro:
            self.log.info(erro)

    def write_data(self):
        try:
            with open(self.path_file_config,"w", encoding="utf-8") as outfile:
                json.dump(self.current_data, outfile,indent=2)
        except Exception as error:
            self.log.error(error)
