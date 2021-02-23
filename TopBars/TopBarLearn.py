from PyQt5.QtWidgets import QWidget
from UI.TopBarLearnUI import Ui_Form


# Элемент панели с кнопкой "назад"
class TopBarLearn(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
