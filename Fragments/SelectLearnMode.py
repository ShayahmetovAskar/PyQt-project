from PyQt5.QtWidgets import QWidget
from UI.SelectLearnModeUI import Ui_Form
from db_helper import Helper


class SelectLearnMode(QWidget, Ui_Form):
    def __init__(self, start_function1, start_function2, start_function3, go_back):
        super().__init__()
        self.setupUi(self)
        # Функции запусков
        self.start_function1 = start_function1
        self.start_function2 = start_function2
        self.start_function3 = start_function3
        self.go_back = go_back

        self.db_helper = Helper()

        self.current_theme = None
        self.repeats = None

        # Функции для обновления данных
        self.comboBox_easy.popupAboutToBeShown.connect(self.set_combo_box_data)
        self.comboBox_medium.popupAboutToBeShown.connect(self.set_combo_box_data)
        self.comboBox_hard.popupAboutToBeShown.connect(self.set_combo_box_data)

        # Обновление данных
        self.refresh()

        # Подключение функций старта к кнопкам
        self.pushButton_easy.clicked.connect(self.button_start_clicked)
        self.pushButton_medium.clicked.connect(self.button_start_clicked)
        self.pushButton_hard.clicked.connect(self.button_start_clicked)

    def set_combo_box_data(self):
        self.sender().clear()
        themes = self.db_helper.get_titles()
        self.sender().addItems(themes)

    # Обработка нажатий кнопок
    def button_start_clicked(self):
        sender = self.sender()
        # Если база данных пуста, будет обработано исключение
        try:
            if sender == self.pushButton_easy:
                self.start_function1(self.comboBox_easy.currentText(), self.spinBox_easy.value())
            elif sender == self.pushButton_medium:
                self.start_function2(self.comboBox_medium.currentText(), self.spinBox_medium.value())
            elif sender == self.pushButton_hard:
                self.start_function3(self.comboBox_hard.currentText(), self.spinBox_hard.value())
        except Exception as e:
            self.go_back()
            print(e)

    def refresh(self):
        self.comboBox_easy.popupAboutToBeShown.emit()
        self.comboBox_medium.popupAboutToBeShown.emit()
        self.comboBox_hard.popupAboutToBeShown.emit()
