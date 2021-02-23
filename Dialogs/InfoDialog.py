from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from UI.InformationDialogUI import Ui_Form


# Иноформационное диалоговое окно с текстом и одной кнопкой
class InfoDialog(QDialog, Ui_Form):
    def __init__(self, text):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.label.setText(text)
        self.pushButton.clicked.connect(self.reject)
