from PyQt5.QtWidgets import QWidget, QStackedWidget
from UI.FragmentLearnUI import Ui_Form
from Fragments.SelectLearnMode import SelectLearnMode
from Fragments.LearnMode1 import LearnMode1
from Fragments.LearnMode2 import LearnMode2
from Fragments.LearnMode3 import LearnMode3


class FragmentLearn(QWidget, Ui_Form):
    def __init__(self, stacked_widget_top_bar: QStackedWidget, info_widget):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget_top_bar = stacked_widget_top_bar  # Верхняя панель
        self.top_bar_page = 3  # Страница верхней панели

        # Элемент верхней панели
        self.info_widget = info_widget
        # Кнопка верхней панели
        self.info_widget.pushButton.clicked.connect(self.go_back)

        # Инициализация страниц
        self.select_mode = SelectLearnMode(self.start_mode1, self.start_mode2, self.start_mode3,
                                           self.go_back)
        self.learn_easy = LearnMode1(self.go_back)
        self.learn_medium = LearnMode2(self.go_back)
        self.learn_hard = LearnMode3(self.go_back)

        # Добавление страниц в виджет
        self.stackedWidget.addWidget(self.select_mode)
        self.stackedWidget.addWidget(self.learn_easy)
        self.stackedWidget.addWidget(self.learn_medium)
        self.stackedWidget.addWidget(self.learn_hard)

        # Начальная страница - страница с выбором сложности
        self.stackedWidget.setCurrentIndex(0)

    # Начать изучение слов в первом режиме
    def start_mode1(self, title: str, count: int):
        self.top_bar_page = 0
        self.stacked_widget_top_bar.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.learn_easy.start(title, count)

    # Начать изучение слов во втором режиме
    def start_mode2(self, title: str, count: int):
        self.top_bar_page = 0
        self.stacked_widget_top_bar.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        self.learn_medium.start(title, count)

    # Начать изучение слов в третьем режиме
    def start_mode3(self, title: str, count: int):
        self.top_bar_page = 0
        self.stacked_widget_top_bar.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(3)
        self.learn_hard.start(title, count)

    # Вернуться к выбору сложности
    def go_back(self):
        self.stacked_widget_top_bar.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(0)
        self.top_bar_page = 3

    # Обновить данные о словарях
    def refresh(self):
        self.select_mode.refresh()
