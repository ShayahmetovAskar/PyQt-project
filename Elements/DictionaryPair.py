from PyQt5.QtWidgets import QWidget
from UI.DictionaryWordPairUI import Ui_Form
from src.styles import Styles


# Элемент словаря с тремя текстовыми полями - для счетчика, слова и перевода слова.
class DictionaryPair(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(Styles.style_dictionary_pair)
        self.label.setStyleSheet('font-size: 8px;')
