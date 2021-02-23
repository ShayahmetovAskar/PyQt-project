from PyQt5.QtWidgets import QWidget
from UI.TopBarDictionary2UI import Ui_Form


# Элемент панели с кнопками "назад", "открыть" и "сохранить"
class TopBarDictionary2(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
