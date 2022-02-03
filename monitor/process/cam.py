from curses.ascii import SI
from re import T
import cv2
from threading import Thread
import logging
from ..data_base import DataBase 
from PySide6.QtCore import Signal,QThread
from typing import Type

class CamPing(QThread):
    
    """
    tenta conectar em um link rstp para verificar que a câmera esta online
    """
    aviso  = Signal(str)
    result = Signal(str)
    def __init__(self,parent) -> None:
        super().__init__(parent=parent)
        self.log = logging.getLogger(__name__)
        self.rstp = ""
        self.name_cam = ""
    
    def run(self) -> None:
        self.aviso.emit("#######################")
        self.aviso.emit(f"testando {self.name_cam}")      
        self.__connect()

    def set_cam(self,name_cam):
        self.name_cam = name_cam
        data = DataBase(name_cam)
 
        self.rstp = data.get_rtsp_link()


    def __connect(self):
        try:
            cap = cv2.VideoCapture(self.rstp)
            if cap.isOpened():
                self.log.debug(f'câmera {self.name_cam} ok')
                self.aviso.emit(f'{self.name_cam} ok')
            else:
                self.result.emit(f"Não estou conseguindo acessar a câmera {self.name_cam}")
                self.aviso.emit(f"erro na câmera {self.name_cam}")
                self.log.info(f'erro connexão {self.name_cam} {self.rstp}')
        except Exception as error:
            print("err ",error)
            self.log.error(error)

        

if __name__ =="__main__":
    cam = CamPing()
    cam.ping("cam 01")