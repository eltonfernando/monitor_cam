from PySide6.QtWidgets import QApplication
from monitor.controller import Controller
import logging
import os
if __name__ == "__main__":
    DEBUG = True
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s::'
                                   '%(asctime)s::'
                                   '%(filename)s::'
                                   '%(funcName)s::'
                                   'line %(lineno)d::'
                                   '%(message)s')

    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)s::'
                                   '%(asctime)s::'
                                   '%(filename)s::'
                                   '%(funcName)s::'
                                   'line %(lineno)d::'
                                   '%(message)s',
                            filename=os.path.join("log", "loger.log"))




    app = QApplication()

    janela = Controller()
    janela.show()
    app.exec()