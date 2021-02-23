import sys

from UI.mainUI import Ui_MainWindow
from TopBars.TopBarDictionary1 import TopBarDictionary1
from TopBars.TopBarDictionary2 import TopBarDictionary2
from TopBars.TopBarLearn import TopBarLearn

from Elements.TitleBar import TitleBar
from Fragments.FragmentLearn import FragmentLearn
from Fragments.FragmentDict import DictFragment
from Elements.menuButtons import MenuButtons
from src.styles import Styles
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.expanded = False
        self.menuTexts = [' ' * 15 + i for i in ['Учить', 'Словарь']]

        self.setupUi(self)
        self.horizontalLayout.addWidget(
            TitleBar(self, ''))  # Добавление строки заголовка в окно приложения
        self.setStyleSheet(Styles.style_scroll_bar)

        self.setWindowFlags(Qt.FramelessWindowHint)  # Окно без рамок и стандартной строки заголовка
        self.pushButtonToggle.clicked.connect(self.toggle_menu)

        # Инициализация элементов верхней панели
        self.top_fragment1 = TopBarLearn()
        self.top_fragment2 = TopBarDictionary1()
        self.top_fragment3 = TopBarDictionary2()

        # Добавление элементов в верхнюю панель
        self.stackedWidgetTopBar.addWidget(self.top_fragment1)
        self.stackedWidgetTopBar.addWidget(self.top_fragment2)
        self.stackedWidgetTopBar.addWidget(self.top_fragment3)
        self.stackedWidgetTopBar.addWidget(QWidget())  # Пустой элемент

        self.stackedWidgetTopBar.setCurrentIndex(1)

        # Инициализация основных элеметнов
        self.fragment1 = FragmentLearn(self.stackedWidgetTopBar, self.top_fragment1)
        self.fragment2 = DictFragment(self.stackedWidgetTopBar, self.top_fragment2,
                                      self.top_fragment3)

        # Добавление элементов в основное окно
        self.stackedWidget.addWidget(self.fragment1)
        self.stackedWidget.addWidget(self.fragment2)
        self.stackedWidget.setCurrentIndex(1)

        # Инициализция и добавление в макет кнопок левой панели
        self.menu = MenuButtons()
        self.verticalLayout_sideBar.addWidget(self.menu)

        # Анимаци левой панели
        self.animation = QPropertyAnimation(self.frame_side, b'minimumWidth')
        self.animation.setDuration(250)

        # Настройка кнопок левой панели
        self.menu.pushButton.clicked.connect(self.menu_button_clicked)
        self.menu.pushButton_2.clicked.connect(self.menu_button_clicked)

    # Анимация левой панели
    def toggle_menu(self):
        if self.expanded:
            self.collapse_menu()
        else:
            self.expand_menu()

    # Разворачивание левой панели
    def expand_menu(self):
        if self.expanded:
            return
        self.animation.setStartValue(70)
        self.animation.setEndValue(150)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()
        self.menu.pushButton.setText(self.menuTexts[0])
        self.menu.pushButton_2.setText(self.menuTexts[1])
        self.expanded = True

    # Сворачивание левой панели
    def collapse_menu(self):
        if not self.expanded:
            return
        self.animation.setStartValue(150)
        self.animation.setEndValue(70)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()
        self.menu.pushButton.setText('')
        self.menu.pushButton_2.setText('')
        self.expanded = False

    # Обработка нажатий кнопок левой панели
    def menu_button_clicked(self):
        self.collapse_menu()
        btn = self.sender()
        if btn == self.menu.pushButton:
            page = self.fragment1.top_bar_page
            self.stackedWidgetTopBar.setCurrentIndex(page)
            self.stackedWidget.setCurrentIndex(0)
            self.fragment1.refresh()
        elif btn == self.menu.pushButton_2:
            page = self.fragment2.top_panel_page
            self.stackedWidgetTopBar.setCurrentIndex(page)
            self.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
