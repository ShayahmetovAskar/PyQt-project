from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QFont


# Строка заголовка окна, содержащая текстовое поле заголовка и кнопки управления приложением
class TitleBar(QWidget):
    def __init__(self, parent, text=''):
        super().__init__()
        self.parent = parent

        # Настройка макета элемента
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.start_move_pos = None

        # Размеры кнопок управления
        btn_size_x = 40
        btn_size_y = 40

        # Текстовое поле заголовка
        self.title = QLabel(text)
        self.title.setFixedHeight(btn_size_y)  # Высота равна высоте кнопок управления
        self.title.setAlignment(Qt.AlignLeft)
        self.title.setContentsMargins(20, 0, 0, 0)
        self.title.setFont(QFont('', 20, QFont.Normal))
        self.title.setStyleSheet("""color: white; """)  # Цвет текста - белый

        # Настройки кнопки 'закрыть' |X|
        self.btn_close = QPushButton()
        self.btn_close.clicked.connect(self.close_clicked)
        self.btn_close.setFixedSize(btn_size_x, btn_size_y)
        self.btn_close.setStyleSheet("""
                                        QPushButton {
                                            background-position: center;
                                            background-repeat: no-repeat;
                                            border: none;
                                        }
                                        QPushButton:hover {
                                            background-color: rgb(232, 17, 35);
                                        }
                                        QPushButton:pressed {	
                                            background-color: rgb(221, 93, 103);
                                        }
                                        """)
        self.btn_close.setIcon(QIcon('src/icons/icon_close.png'))

        # Настройки кнопки 'свернуть' |-|
        self.btn_minimize = QPushButton()
        self.btn_minimize.clicked.connect(self.minimize_clicked)
        self.btn_minimize.setFixedSize(btn_size_x, btn_size_y)
        self.btn_minimize.setStyleSheet("""
                                        QPushButton {
                                            background-position: center;
                                            background-repeat: no-repeat;
                                            border: none;
                                        }
                                        QPushButton:hover {
                                            background-color: rgb(40, 43, 46);
                                        }
                                        QPushButton:pressed {	
                                            background-color: rgb(43, 46, 50);
                                        }
                                        """)
        self.btn_minimize.setIcon(QIcon('src/icons/icon_minimize.png'))

        # Добавление элементов в макет
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_minimize)
        self.layout.addWidget(self.btn_close)

        self.setLayout(self.layout)
        self.start = QPoint(0, 0)
        self.isPressed = False

    # При нажатии на строку заголовка сохраняется начальная позиция окна
    def mousePressEvent(self, event):
        self.isPressed = True
        self.start_move_pos = event.globalPos()

    # При перемещении строки заголовка перемещается окно приложения
    def mouseMoveEvent(self, event):
        if self.isPressed:
            move_point = event.globalPos() - self.start_move_pos
            widget_pos = self.parent.pos()
            self.start_move_pos = event.globalPos()
            self.parent.move(widget_pos.x() + move_point.x(), widget_pos.y() + move_point.y())

    def mouseReleaseEvent(self, event):
        self.isPressed = False

    # Действие при нажатии кнопки 'закрыть' |X|
    def close_clicked(self):
        self.parent.close()

    # Действие при нажатии кнопки 'свернуть' |-|
    def minimize_clicked(self):
        self.parent.showMinimized()
