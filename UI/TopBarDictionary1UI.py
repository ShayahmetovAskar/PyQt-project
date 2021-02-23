from src.styles import Styles
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 44)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonDeleteTheme = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonDeleteTheme.setFont(font)
        self.pushButtonDeleteTheme.setStyleSheet(Styles.style_nice_button)
        self.pushButtonDeleteTheme.setIcon(QtGui.QIcon('src/icons/icon_delete.png'))
        self.pushButtonDeleteTheme.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButtonDeleteTheme)
        self.pushButtonAddTheme = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAddTheme.setFont(font)
        self.pushButtonAddTheme.setStyleSheet(Styles.style_nice_button)
        self.pushButtonAddTheme.setIcon(QtGui.QIcon('src/icons/icon_add.png'))
        self.pushButtonAddTheme.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButtonAddTheme)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonDeleteTheme.setText(_translate("Form", "Удалить"))
        self.pushButtonAddTheme.setText(_translate("Form", "Добавить"))
