from UI.LearnMode3UI import Ui_Form
from Fragments.LearnModeBase import LearnModeBase
from PyQt5 import QtCore, QtWidgets


class LearnMode3(QtWidgets.QWidget, Ui_Form, LearnModeBase):
    def __init__(self, go_back):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)
        LearnModeBase.__init__(self)
        self.setupUi(self)

        self.go_back = go_back

        # Анимация для label
        opacity_effect1 = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect1.setOpacity(1)
        self.label.setGraphicsEffect(opacity_effect1)
        self.label_opacity_animation = QtCore.QPropertyAnimation(opacity_effect1, b'opacity', self)
        self.label_opacity_animation.setDuration(LearnModeBase.ANIMATION_DURATION)

        # Анимация для label_2
        opacity_effect2 = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect2.setOpacity(1)
        self.label_2.setGraphicsEffect(opacity_effect2)
        self.label_opacity_animation2 = QtCore.QPropertyAnimation(opacity_effect2, b'opacity', self)
        self.label_opacity_animation2.setDuration(LearnModeBase.ANIMATION_DURATION)

        # При нажати enter в lineEdit имитируется нажатие кнопки pushButton
        self.lineEdit.returnPressed.connect(self.pushButton.animateClick)

    def start(self, title, repeats):
        super().start(title, repeats)

        if self.dictionary_length < 3:  # Если слов не достаточно, перейти к выбору сложности
            self.go_back()
            self.not_enough_words()
            return

        self.words_order = self.generate_sequence(repeats, self.dictionary_length)  # Случайный порядок слов
        self.label.setText('')
        self.label_2.setText('')
        self.pushButton.setText('Проверить')
        self.next_word()  # Показать первое слово

    def next_word(self):
        # Анимации
        self.fade_out_label1()
        self.fade_out_label2()

        # Выход, если номер слова равен количеству повторений
        if self.current_index == self.repeats:
            QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION * 3, self.go_back)
            QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION * 3, self.show_result)
            return
        current_index = self.words_order[self.current_index]
        self.lineEdit.setText('')
        self.disconnect_clicked_listener()  # Отключение функции от кнопки

        # Анимации
        QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION,
                                 lambda: self.label.setText(self.translations[current_index]))
        QtCore.QTimer.singleShot(LearnModeBase.ANIMATION_DURATION * 2, self.fade_in_label1)

        self.pushButton.clicked.connect(self.check_input)

    def check_input(self):
        inp = self.lineEdit.text()
        # Выход из функции если lineEdit пуст
        if len(inp.strip()) == 0:
            return

        # Проверка правильности введенного слова
        if inp.lower() == self.words[self.words_order[self.current_index]].lower():
            self.label_2.setText('Верно')
            self.score += 1
        else:
            self.label_2.setText(f'Правильно будет так: {self.words[self.words_order[self.current_index]]}')
        self.current_index += 1
        self.disconnect_clicked_listener()
        self.pushButton.clicked.connect(self.next_word)
        self.fade_in_label2()
        self.pushButton.setText('Далее')

    # Исчезновение label1
    def fade_out_label1(self):
        self.label_opacity_animation.setStartValue(1)
        self.label_opacity_animation.setEndValue(0)
        self.label_opacity_animation.start()

    # Появление label1
    def fade_in_label1(self):
        self.label_opacity_animation.setStartValue(0)
        self.label_opacity_animation.setEndValue(1)
        self.label_opacity_animation.start()

    # Исчезновение label2
    def fade_out_label2(self):
        self.label_opacity_animation2.setStartValue(1)
        self.label_opacity_animation2.setEndValue(0)
        self.label_opacity_animation2.start()

    # Появление label1
    def fade_in_label2(self):
        self.label_opacity_animation2.setStartValue(0)
        self.label_opacity_animation2.setEndValue(1)
        self.label_opacity_animation2.start()

    # Отключение функций от кнопки
    def disconnect_clicked_listener(self):
        try:
            self.pushButton.clicked.disconnect()
        except TypeError:
            pass
