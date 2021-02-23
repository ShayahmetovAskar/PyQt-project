from PyQt5.QtWidgets import QWidget
from UI.DictionaryWordInputUI import Ui_Form


# Элемент для ввода слов в словарь, содержащий два поля для ввода текста и одну кнопку
class WordInput(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEditTranslation.returnPressed.connect(self.line_edit2_enter_pressed)

    # При нажатии кнопки enter на втором поле для ввода текста
    # имитируется нажатие кнопки и фокус переходит на первое поле
    def line_edit2_enter_pressed(self):
        self.pushButtonAddToDictionary.animateClick()
        self.lineEditWord.setFocus()
