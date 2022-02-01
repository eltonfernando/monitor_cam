import json
import logging
import os
class DataBase():
    def __init__(self,path_file_config : str) -> None:
        self.log = logging.getLogger(__name__)
        self.dir_base = "config"
        if not path_file_config.endswith('.json'):
            path_file_config = path_file_config+".json"

        self.path_file_config = os.path.join(self.dir_base, path_file_config)
        self.current_data = {}
        self.read_data()
    
    def set_rstp_link(self,rstp: str):
        self.current_data["rstp"]= rstp
        self.write_data()

    def get_rstp_link(self):
        if "rstp" in self.current_data:
            return self.current_data["rstp"]
        else:
            return 0

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