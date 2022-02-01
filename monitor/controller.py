from PySide6.QtWidgets import QApplication, QMainWindow
from view.from_ui import Ui_MainWindow

from setup import __version__
class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Monitor {__version__}")

if __name__ == "__main__":
    app = QApplication()

    janela = Controller()
    janela.show()
    app.exec()
