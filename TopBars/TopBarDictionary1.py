from UI.TopBarDictionary1UI import Ui_Form
from PyQt5.QtWidgets import QWidget


# Элемент панели с кнопками "удалить" и "добавить"
class TopBarDictionary1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
