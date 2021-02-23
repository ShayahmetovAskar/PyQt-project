from PyQt5.QtWidgets import QWidget
from UI.LeftMenuButtonsUI import Ui_Form


# Элемент, содержащий кнопки левой панели
class MenuButtons(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
