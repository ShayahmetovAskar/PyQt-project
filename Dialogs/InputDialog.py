from UI.InputDialogUI import Ui_Form
from PyQt5.QtWidgets import QDialog, QInputDialog
from PyQt5 import QtCore


# Диалоговое окно ввода информации с текстом, полем ввода и двумя кнопками подтвердить/отменить
class InputDialog(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def get_text(self):
        if self.exec_() == QInputDialog.Accepted:
            text = self.lineEdit.text()
            return text
        else:
            return None
