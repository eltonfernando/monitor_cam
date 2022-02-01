# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'from_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 473)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_rstp = QLineEdit(self.centralwidget)
        self.lineEdit_rstp.setObjectName(u"lineEdit_rstp")

        self.gridLayout_3.addWidget(self.lineEdit_rstp, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout_3.addWidget(self.pushButton_add, 2, 1, 1, 1)

        self.comboBox_cam = QComboBox(self.centralwidget)
        self.comboBox_cam.setObjectName(u"comboBox_cam")
        self.comboBox_cam.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox_cam, 0, 1, 1, 1)

        self.pushButton_del = QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName(u"pushButton_del")

        self.gridLayout_3.addWidget(self.pushButton_del, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 490, 285))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 10, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 510, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RSTP:", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add c\u00e2mera", None))
        self.pushButton_del.setText(QCoreApplication.translate("MainWindow", u"Delete c\u00e2mera", None))
    # retranslateUi

