import logging

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Slot, QTimer
import os
from glob import glob
from .view import Ui_MainWindow
from .setup import __version__
from .data_base import DataBase
from .telegram import Bot
from .process import CamPing


class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.log= logging.getLogger(__name__)

        self.setWindowTitle(f"Monitor {__version__}")
        self.restore_data()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.ui.comboBox_cam.activated.connect(self.update_select_combo_cam)

        self.cam = CamPing(self)
        self.cam.aviso.connect(self.log_text)
        self.cam.result.connect(self.aviso_bot)

    def update_select_combo_cam(self,index):
        text = self.ui.comboBox_cam.currentText()
        data = DataBase(text)
        rtsp = data.get_rtsp_link()
        self.ui.lineEdit_rstp.setText(rtsp)

    def timer_event(self):

        if not self.cam.isRunning():
            self.cam.start()
        else:
            self.log.info("thread running")

    @Slot(str)
    def log_text(self, text: str):
        color = "blue"
        cursor = self.ui.textBrowser_log.textCursor()
        if text.startswith("erro"):
            color = "red"
            cursor.insertHtml('''<h4><br><span style="color: {};">{} </span ></br> </h4>'''.format(color,text))
        else:
            cursor.insertHtml('''<p><br <span style="color: {};">{} </span> </br> </p>'''.format(color, text))
            #self.ui.textBrowser_log.append(text)

    def update_combo_cliente(self):
        dir_base = os.path.join("monitor", "telegram", "config")
        list_path_cliente = glob(os.path.join(dir_base, "*.json"))
        if len(list_path_cliente) > 0:
            for path_file_client in list_path_cliente:
                name_file = os.path.basename(path_file_client).split(".")[0]
                self.ui.comboBox_name_cliente.addItem(name_file)

    def restore_data(self):
        self.update_combo_cliente()
        if os.path.isdir("config"):
            list_config = glob(os.path.join("config", "*.json"))
            if len(list_config) > 0:
                for path_file in list_config:
                    name_file = os.path.basename(path_file).split(".")[0]
                    self.ui.textBrowser_log.append(name_file)
                    self.ui.comboBox_cam.addItem(name_file)

                name_cam = self.ui.comboBox_cam.currentText()
                data= DataBase(name_cam)
                rtsp = data.get_rtsp_link()
                self.ui.lineEdit_rstp.setText(rtsp)

    @Slot(str)
    def aviso_bot(self, text):
        bot = Bot()
        bot.alert_user(text)

    @Slot()
    def on_pushButton_add_clicked(self):
        name_cam = self.ui.comboBox_cam.currentText()
        rstp_link = self.ui.lineEdit_rstp.text()
        data = DataBase(name_cam)
        data.set_rtsp_link(rstp_link)

        if self.ui.comboBox_cam.findText(name_cam)==-1:
            self.ui.textBrowser_log.append(f"{name_cam} adicionado")
            self.ui.comboBox_cam.addItem(name_cam)


    @Slot()
    def on_pushButton_del_clicked(self):
        index_selected = self.ui.comboBox_cam.currentIndex()
        name_cam = self.ui.comboBox_cam.currentText()
        path_file_config = os.path.join("config", f"{name_cam}.json")
        if os.path.isfile(path_file_config):
            os.remove(path_file_config)
            self.ui.comboBox_cam.removeItem(index_selected)

    @Slot()
    def on_pushButton_add_user_telegram_clicked(self):
        print("clicked get id user")
        msg = QMessageBox()
        msg.setText(f'Obtendo ID do telegram')
        msg.setWindowTitle("Info")
        msg.setInformativeText("1: Entre no telegram procure pelo usuário @SmartfluxBot (ou seu bot) \n"
                               "2: envie a msg /start para o bot")
        msg.setStandardButtons(msg.Ok)
        msg.exec()
        bot = Bot()
        bot.add_new_cliente(self.ui.comboBox_name_cliente)
        self.update_combo_cliente()

    @Slot()
    def on_pushButton_teste_msg_client_clicked(self):
        name_cliente = self.ui.comboBox_name_cliente.currentText()
        bot = Bot()
        bot.teste_msg(name_cliente)

        msg = QMessageBox()
        msg.setText(f'Envio de mensagem')
        msg.setWindowTitle("Aviso")
        msg.setInformativeText("Se você recebeu uma mensagem de teste no seu telegram é porque esta tudo ok")
        msg.setStandardButtons(msg.Ok)
        msg.exec()

    @Slot()
    def on_pushButton_del_user_telegram_clicked(self):
        name_file_cliente = self.ui.comboBox_name_cliente.currentText()
        self.ui.comboBox_name_cliente.removeItem(self.ui.comboBox_name_cliente.currentIndex())
        bot = Bot()
        bot.del_cliente_file(name_file_cliente)

    @Slot()
    def on_pushButton_start_monitor_clicked(self):
        self.ui.textBrowser_log.append("start monitor")
        if not self.timer.isActive():
            self.timer.start(5000)  # 10 segundos
            self.ui.comboBox_cam.setEditable(False)
            self.ui.pushButton_add.setEnabled(False)
            self.ui.pushButton_del.setEnabled(False)
            self.ui.pushButton_add_user_telegram.setEnabled(False)
            self.ui.pushButton_del_user_telegram.setEnabled(False)
            self.ui.pushButton_teste_msg_client.setEnabled(False)
            self.ui.pushButton_start_monitor.setEnabled(False)

    @Slot()
    def on_pushButton_stop_monitor_clicked(self):
        self.ui.comboBox_cam.setEditable(True)
        self.ui.pushButton_add.setEnabled(True)
        self.ui.pushButton_del.setEnabled(True)
        self.ui.pushButton_add_user_telegram.setEnabled(True)
        self.ui.pushButton_del_user_telegram.setEnabled(True)
        self.ui.pushButton_teste_msg_client.setEnabled(True)
        self.ui.pushButton_start_monitor.setEnabled(True)
        if self.timer.isActive():
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication()

    janela = Controller()
    janela.show()
    app.exec()
