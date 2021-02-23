from PyQt5.QtWidgets import QWidget
from UI.DictionaryThemeTitleUI import Ui_Form
from src.colors import Colors
from src.styles import Styles


# Элемент с текстовым полем для названия темы и кнопкой для перехода к соответствующей теме
class DictionaryTitle(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(f"""
                                QFrame {{
                                    background-color: {Colors.get_color(Colors.cardColor)};
                                    border-radius: 4px;

                                }}
                                QLabel {{
                                    border: none;
                                    font-size: 16px;
                                    color: {Colors.get_color(Colors.textColor)};
                                }}
                                """ + Styles.style_nice_button)
