from UI.ConfirmationDialogUI import Ui_Form
from PyQt5.QtWidgets import QDialog, QInputDialog
from PyQt5 import QtCore


# Диалоговое окно с текстом и кнопками подтвердить/отменить
class ConfirmationDialog(QDialog, Ui_Form):
    def __init__(self, text=''):
        super().__init__()
        self.setupUi(self)
        self.label.setText(text)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def get_results(self):
        return self.exec_() == QInputDialog.Accepted
