from UI.LearnMode2UI import Ui_Form
from random import sample, shuffle
from Fragments.LearnModeBase import LearnModeBase
from PyQt5 import QtCore, QtGui, QtWidgets


class LearnMode2(QtWidgets.QWidget, Ui_Form, LearnModeBase):
    def __init__(self, go_back):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)
        LearnModeBase.__init__(self)
        self.setupUi(self)

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.current_letter_index = 0  # Номер текущей буквы в слове
        self.mistake = False  # Индикатор ошибки
        self.go_back = go_back

        # Подключение анимаций к элементам
        self.opacity_animations = []
        for widget in [self.label, self.label_2] + self.buttons:
            opacity_effect = QtWidgets.QGraphicsOpacityEffect()
            opacity_effect.setOpacity(1)
            widget.setGraphicsEffect(opacity_effect)
            opacity_animation = QtCore.QPropertyAnimation(opacity_effect, b'opacity', self)
            opacity_animation.setDuration(LearnModeBase.ANIMATION_DURATION)
            self.opacity_animations.append(opacity_animation)

    def start(self, title, count):
        super().start(title, count)

        if self.dictionary_length < 3:  # Если слов не достаточно, перейти к выбору сложности
            self.go_back()
            self.not_enough_words()
            return

        self.current_letter_index = 0
        self.words_order = self.generate_sequence(count, self.dictionary_length)  # Случайный порядок слов
        self.mistake = True  # Индикатор ошибки
        self.next_word()  # Показать первое слово

    def next_word(self):
        # Если индикатор ошибки False к счету прибавляется 1, иначе 0
        self.score += 1 if not self.mistake else 0
        self.mistake = False
        # Выход, если номер слова равен количеству повторений
        if self.current_index == self.repeats:
            self.go_back()
            self.show_result()
            return
        self.current_letter_index = 0
        # Вывод на экран перевода слова
        self.label.setText(self.translations[self.words_order[self.current_index]])
        self.next_letter()

    def next_letter(self):
        current_word = self.words[self.words_order[self.current_index]]  # Текущее слово
        self.display_text(current_word, self.current_letter_index)  # Вывод предыдущей буквы
        letter = current_word[self.current_letter_index]  # Текущая буква
        letter = letter.upper() if letter.isalpha() else letter
        # Случайная генерация четырех букв
        letters = [letter] + sample([i for i in self.alphabet if i != letter], 4)
        shuffle(self.buttons)
        # Установка букв в кнопки
        for i in range(len(self.buttons)):
            self.buttons[i].setText(letters[i])
        # Правильная буква в первой кнопке из списка
        # При нажатии на неё вызывается функция correct_button_clicked
        self.buttons[0].clicked.connect(self.correct_button_clicked)
        # При нажатии на другие кнопки вызывается incorrect_button_clicked
        for button in self.buttons[1:]:
            button.clicked.connect(self.incorrect_button_clicked)
        self.current_letter_index += 1

    # В label_2 устанавливается текст с определенным количеством открытых букв
    # Например, для text=hello-world, opened=5 выведется 'hello-_____'
    def display_text(self, text: str, opened: int):
        self.label_2.setText(text[:opened] + ('_' * (len(text) - opened)))

    # Событие при нажатии на правильную кнопку
    def correct_button_clicked(self):
        # От кнопок отвязываются функции
        for button in self.buttons:
            try:
                button.clicked.disconnect()
            except TypeError:
                pass
        current_word = self.words[self.words_order[self.current_index]]
        if self.current_letter_index == len(current_word):  # Если слово введено полностью
            # В label_2 слово вписывается полностью
            self.label_2.setText(current_word)
            self.current_index += 1
            # В нужном порядке проигрываются анимации
            self.fade_out_animation()
            QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION, self.next_word)
            QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION * 2, self.fade_in_animation)
        else:
            self.next_letter()

    # Событие при нажатии на неправильную кнопку
    def incorrect_button_clicked(self):
        self.mistake = True

    # Анимация появления элементов
    def fade_in_animation(self):
        self.fade_in_out_animation(0)

    # Анимация затухания элементов
    def fade_out_animation(self):
        self.fade_in_out_animation(1)

    def fade_in_out_animation(self, mode):
        for opacity_animation in self.opacity_animations:
            opacity_animation.setStartValue(int(mode))
            opacity_animation.setEndValue(int(not mode))
            opacity_animation.start()

    # К правильной кнопке привязывается соответствующая кнопка
    # Если правильная буква - 'Q', кнопка 'Q' на клавиатуре будет имитировать нажатие правильной кнопки
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == QtGui.QKeySequence(self.buttons[0].text())[0]:
            self.buttons[0].animateClick()
        else:
            self.mistake = True
