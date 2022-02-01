from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Slot
from .view import Ui_MainWindow
from .setup import __version__


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
        self.setWindowTitle(f"Monitor {__version__}")
        
    
    def add_cam(self,name_cam):
        self.label = MyLabel()
        self.label.set_label(name_cam)
        self.ui.verticalLayout.addWidget(self.label)
        self.ui.comboBox_cam.addItem(name_cam)
        
    @Slot()
    def on_pushButton_add_clicked(self):
        name_cam = self.ui.comboBox_cam.currentText()
        print(name_cam)
        self.add_cam(name_cam)


if __name__ == "__main__":
    app = QApplication()

    janela = Controller()
    janela.show()
    app.exec()
