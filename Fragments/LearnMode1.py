from UI.LearnMode1UI import Ui_Form
from Fragments.LearnModeBase import LearnModeBase
from PyQt5 import QtCore, QtGui, QtWidgets
from random import shuffle, sample


class LearnMode1(QtWidgets.QWidget, Ui_Form, LearnModeBase):
    def __init__(self, go_back):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)
        LearnModeBase.__init__(self)
        self.setupUi(self)

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3]
        self.mistake = False
        self.go_back = go_back

        # Подключение анимаций к элементам
        self.opacity_animations = []
        for widget in [self.label, self.pushButton, self.pushButton_2, self.pushButton_3]:
            opacity_effect = QtWidgets.QGraphicsOpacityEffect()
            opacity_effect.setOpacity(1)
            widget.setGraphicsEffect(opacity_effect)
            opacity_animation = QtCore.QPropertyAnimation(opacity_effect, b'opacity', self)
            opacity_animation.setDuration(LearnModeBase.ANIMATION_DURATION)
            self.opacity_animations.append(opacity_animation)

    def start(self, title, repeats):
        super().start(title, repeats)

        if self.dictionary_length < 3:  # Если слов не достаточно, перейти к выбору сложности
            self.go_back()
            self.not_enough_words()
            return

        self.mistake = False  # Индикатор ошибки
        self.words_order = self.generate_sequence(repeats, self.dictionary_length)  # Случайный порядок слов

        self.next_word()  # Показать первое слово

    def next_word(self):
        # Выход, если номер слова равен количеству повторений
        if self.current_index == self.repeats:
            self.go_back()  # Возвращение к выбору сложности
            self.show_result()  # Вывод результата
            return

        current_index = self.words_order[self.current_index]  # Индекс текущего слова (случайный)
        # Генерация двух неправильных вариантов ответа
        incorrect_word_index_1, incorrect_word_index_2 = sample(
            [i for i in range(self.dictionary_length) if i != current_index], 2)

        # Вывод на экран перевода слова
        self.label.setText(self.translations[current_index])

        shuffle(self.buttons)  # Перемешивание списка с кнопками
        # В первую кнопку устанавливается правильный ответ, в остальные случайный неправильный
        self.buttons[0].setText(self.words[current_index])
        self.buttons[1].setText(self.words[incorrect_word_index_1])
        self.buttons[2].setText(self.words[incorrect_word_index_2])

        # При нажатии на правильную кнопку вызывается correct_button_clicked, а на неправильную incorrect_button_clicked
        self.buttons[0].clicked.connect(self.correct_button_clicked)
        self.buttons[1].clicked.connect(self.incorrect_button_clicked)
        self.buttons[2].clicked.connect(self.incorrect_button_clicked)

        self.current_index += 1

    # Событие при нажатии на правильную кнопку
    def correct_button_clicked(self):
        # От кнопок отсоединяются старые функции
        for button in self.buttons:
            try:
                button.clicked.disconnect()
            except TypeError:
                pass
        # Если индикатор ошибки False к счету прибавляется 1, иначе 0
        self.score += 1 if not self.mistake else 0
        self.mistake = False
        # "Растворение" элементов
        self.fade_out_animation()
        # Через время, равное длительности анимации вызывается функция next_word
        QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION, self.next_word)
        # Появление элементов через время, равное двум длительностям анимации
        QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION * 2, self.fade_in_animation)

    # Событие при нажатии на неправильную кнопку
    def incorrect_button_clicked(self):
        self.mistake = True

    # Появление элементов
    def fade_in_animation(self):
        self.fade_in_out_animation(0)

    # Растворение элементов
    def fade_out_animation(self):
        self.fade_in_out_animation(1)

    def fade_in_out_animation(self, mode):
        for opacity_animation in self.opacity_animations:
            opacity_animation.setStartValue(int(mode))
            opacity_animation.setEndValue(int(not mode))
            opacity_animation.start()

    # Клавиши 1, 2, 3 привязываются к соответствующим кнопкам
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        key_code = a0.key()
        if key_code == QtCore.Qt.Key_1:
            self.pushButton_2.animateClick()
        elif key_code == QtCore.Qt.Key_2:
            self.pushButton.animateClick()
        elif key_code == QtCore.Qt.Key_3:
            self.pushButton_3.animateClick()
