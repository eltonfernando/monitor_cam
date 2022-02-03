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
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 688)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 490, 302))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.textBrowser_log = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_log.setObjectName(u"textBrowser_log")

        self.verticalLayout.addWidget(self.textBrowser_log)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 10, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.pushButton_del_user_telegram = QPushButton(self.centralwidget)
        self.pushButton_del_user_telegram.setObjectName(u"pushButton_del_user_telegram")

        self.gridLayout_4.addWidget(self.pushButton_del_user_telegram, 4, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.comboBox_name_cliente = QComboBox(self.centralwidget)
        self.comboBox_name_cliente.setObjectName(u"comboBox_name_cliente")
        self.comboBox_name_cliente.setEnabled(True)
        self.comboBox_name_cliente.setMinimumSize(QSize(160, 0))
        self.comboBox_name_cliente.setEditable(False)

        self.gridLayout_4.addWidget(self.comboBox_name_cliente, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)

        self.pushButton_add_user_telegram = QPushButton(self.centralwidget)
        self.pushButton_add_user_telegram.setObjectName(u"pushButton_add_user_telegram")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_add_user_telegram.sizePolicy().hasHeightForWidth())
        self.pushButton_add_user_telegram.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.pushButton_add_user_telegram, 1, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.pushButton_teste_msg_client = QPushButton(self.centralwidget)
        self.pushButton_teste_msg_client.setObjectName(u"pushButton_teste_msg_client")

        self.gridLayout_4.addWidget(self.pushButton_teste_msg_client, 4, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 13, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(135, 135, 135);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 11, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(135, 135, 135);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 14, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.pushButton_start_monitor = QPushButton(self.centralwidget)
        self.pushButton_start_monitor.setObjectName(u"pushButton_start_monitor")
        sizePolicy1.setHeightForWidth(self.pushButton_start_monitor.sizePolicy().hasHeightForWidth())
        self.pushButton_start_monitor.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.pushButton_start_monitor, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.pushButton_stop_monitor = QPushButton(self.centralwidget)
        self.pushButton_stop_monitor.setObjectName(u"pushButton_stop_monitor")

        self.gridLayout_5.addWidget(self.pushButton_stop_monitor, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 15, 0, 1, 1)

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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RTSP:", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add c\u00e2mera", None))
        self.pushButton_del.setText(QCoreApplication.translate("MainWindow", u"Delete c\u00e2mera", None))
        self.pushButton_del_user_telegram.setText(QCoreApplication.translate("MainWindow", u"Delete Ouvinte", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Del Cliente", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome Cliente", None))
        self.pushButton_add_user_telegram.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Add Cliente", None))
        self.pushButton_teste_msg_client.setText(QCoreApplication.translate("MainWindow", u"Teste aviso", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Criar alerta para o telegram", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Iniciar monitoramento", None))
        self.pushButton_start_monitor.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.pushButton_stop_monitor.setText(QCoreApplication.translate("MainWindow", u"Parar", None))
    # retranslateUi

