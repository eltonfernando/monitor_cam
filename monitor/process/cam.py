import cv2
from PySide6.QtCore import Signal, QThread
from typing import Type
from glob import glob
import os
import logging
from ..data_base import DataBase


class CamPing(QThread):
    """
    tenta conectar em um link rstp para verificar que a câmera esta online
    """
    aviso: Type[Signal] = Signal(str)
    result = Signal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.log = logging.getLogger(__name__)
        self.rtsp = ""
        self.name_cam = ""
        self.registre_cam_offline = []

    def run(self) -> None:
        self.aviso.emit("######### Tantando ##############")
        lis_path_file = glob(os.path.join("config", "*.json"))
        for path_file in lis_path_file:
            self.name_cam = os.path.basename(path_file).split(".")[0]
            data = DataBase(self.name_cam)
            self.rtsp = data.get_rtsp_link()
            self.aviso.emit(f"testando {self.name_cam}")
            self.__connect()
        self.aviso.emit("######### Fim teste ##############")

    def __connect(self):
        try:
            cap = cv2.VideoCapture(self.rtsp)
            status = False
            if cap.isOpened():
                status, frame = cap.read()

            if status:
                self.log.debug(f'câmera {self.name_cam} ok')
                self.aviso.emit(f'{self.name_cam} ok')
                if self.name_cam in self.registre_cam_offline:
                    self.registre_cam_offline.remove(self.name_cam)
                    self.result.emit(f" Câmera {self.name_cam} voltou")
            else:
                self.aviso.emit(f"erro na câmera {self.name_cam}")
                if not self.name_cam in self.registre_cam_offline:
                    self.result.emit(f"Não estou conseguindo acessar a câmera {self.name_cam}")
                    self.log.info(f'erro connexão {self.name_cam} {self.rtsp}')
                    self.registre_cam_offline.append(self.name_cam)


        except Exception as error:
            print("err ", error)
            self.log.error(error)


if __name__ == "__main__":
    cam = CamPing()
    cam.ping("cam 01")
