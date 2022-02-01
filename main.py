from PySide6.QtWidgets import QApplication
from monitor.controller import Controller

if __name__ == "__main__":
    app = QApplication()

    janela = Controller()
    janela.show()
    app.exec()