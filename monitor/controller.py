from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QMessageBox
from PySide6.QtCore import Slot
import os
from glob import glob
from .view import Ui_MainWindow
from .setup import __version__
from .data_base import DataBase
from .telegram import Bot
class MyLabel(QLabel):
    def __init__(self,parent=None) -> None:
        super().__init__(parent)
    def set_label(self,text):
        self.setText(text)

class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_cam.currentIndexChanged.connect(self.on_comboBox_cam_setCurrentIndex)
        self.setWindowTitle(f"Monitor {__version__}")
        self.restore_data()
        
    
    def add_cam_view(self,name_cam):
        self.label = MyLabel()
        self.label.set_label(name_cam)
         
        self.ui.verticalLayout.addWidget(self.label)
        self.ui.comboBox_cam.addItem(name_cam)
        
    @Slot()
    def on_pushButton_add_clicked(self):
        name_cam = self.ui.comboBox_cam.currentText()
        rstp_link = self.ui.lineEdit_rstp.text()
        data = DataBase(name_cam)
        data.set_rstp_link(rstp_link)

        print(name_cam)
        self.add_cam_view(name_cam)
    
    @Slot()
    def on_pushButton_del_clicked(self):
        index_selected = self.ui.comboBox_cam.currentIndex()
        name_cam = self.ui.comboBox_cam.currentText()
        path_file_config = os.path.join("config",f"{name_cam}.json")
        if os.path.isfile(path_file_config):
            os.remove(path_file_config)
            self.ui.comboBox_cam.removeItem(index_selected)
    
    @Slot()
    def on_comboBox_cam_setCurrentIndex(self, index):
        name_cam = self.ui.comboBox_cam.currentText()
        data = DataBase(name_cam)
        self.ui.lineEdit_rstp.setText(str(data.get_rstp_link()))

        print("test inde combo ",name_cam)
    
    @Slot()
    def on_pushButton_add_user_telegram_clicked(self):
        print("clicked get id user")
        msg = QMessageBox()
        msg.setText(f'Obtendo ID do telegram')
        msg.setWindowTitle("Info")
        msg.setInformativeText("1: Entre no telegram procure pelo usuario @SmartfluxBot \n"
                                "2: envie a msg /start para o bot")
        msg.setStandardButtons(msg.Ok)
        msg.exec()
        bot =Bot()
        bot.find_cliente()                        
    
    def restore_data(self):
        if os.path.isdir("config"):
            list_config = glob(os.path.join("config","*.json"))
            print(list_config)
            if len(list_config)>0:
                for path_file in list_config:
                    name_file = os.path.basename(path_file).split(".")[0]
                    self.add_cam_view(name_file)


if __name__ == "__main__":
    app = QApplication()

    janela = Controller()
    janela.show()
    app.exec()
