# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Network test")
        MainWindow.resize(334, 188)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: white;")
        MainWindow.setWindowTitle('Network test')
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"color: #32a5fa;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.title.setFrameShadow(QFrame.Plain)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setStyleSheet(u"font-size: 14px;")
        self.input_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.input_label.setIndent(-1)

        self.input_label2 = QLabel(self.centralwidget)
        self.input_label2.setObjectName(u"input_label2")
        self.input_label2.setStyleSheet(u"font-size: 14px;")
        self.input_label2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.input_label2.setIndent(-1)

        self.verticalLayout.addWidget(self.input_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setStyleSheet(u"width: 150px;\n"
"height: 25px;\n"
"background-color: white;\n"
"border: 1px solid rgb(190, 187, 187);\n"
"border-radius: 7px;\n"
"padding-left: 5px;")
        self.lineEdit.setMaxLength(256)
        self.lineEdit.setFrame(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	background-color: white;\n"
"	border: 1px solid rgb(190, 187, 187);\n"
"	height: 25px;\n"
"	border-radius: 7px;\n"
"}\n"
"QComboBox::drop-down {\n"
"\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"background-color:  white;\n"
"color: #4f4f4f;\n"
"\n"
"selection-background-color: #4f4f4f;\n"
"selection-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox.setInsertPolicy(QComboBox.InsertAtTop)
        self.comboBox.setIconSize(QSize(0, 0))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.input_label2)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgba(198, 198, 198, 233);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.63, y2:0.545455, stop:0 rgba(0, 217, 255, 255), stop:1 rgba(50, 165, 250, 255));\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAutoFillBackground(False)
        self.status_label.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"font-size: 13px; ")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status_label, 0, Qt.AlignTop)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_test = QPushButton(self.centralwidget)
        self.start_test.setObjectName(u"start_test")
        self.start_test.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_test.sizePolicy().hasHeightForWidth())
        self.start_test.setSizePolicy(sizePolicy1)
        self.start_test.setStyleSheet(u"#start_test {\n"
"background-color: #32a5fa;\n"
"color: white;\n"
"height: 30px;\n"
"width: 150px;\n"
"border-radius: 10%; }")
        self.start_test.setAutoRepeatDelay(300)

        self.horizontalLayout.addWidget(self.start_test)

        self.full_test = QPushButton(self.centralwidget)
        self.full_test.setObjectName(u"full_test")
        self.full_test.setStyleSheet(u"background-color: #32a5fa;\n"
"color: white;\n"
"height: 30px;\n"
"width: 150px;\n"
"border-radius: 10%; ")

        self.horizontalLayout.addWidget(self.full_test)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Nettest", u"Nettest", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0441\u0435\u0442\u0438", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u0438\u043b\u0438 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0435\u0440\u0432\u0438\u0441 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.input_label2.setText(QCoreApplication.translate("MainWindow", u"Пожалуйста, дождитесь окончания\nПолное тестирование может занять до 15 минут", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"world of tanks", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"world of warships", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"world of warplanes", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"valorant", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"warface", None))

        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Scan network", None))
        self.start_test.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0442\u0435\u0441\u0442", None))
        self.full_test.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0442\u0435\u0441\u0442", None))
    # retranslateUi

