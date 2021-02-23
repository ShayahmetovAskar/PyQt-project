from db_helper import Helper
from random import shuffle

from Dialogs.InfoDialog import InfoDialog


class LearnModeBase:
    ANIMATION_DURATION = 200

    def __init__(self):
        self.helper = Helper()  # Помощник в работе с бд
        self.current_theme_title = ''  # Заголовок темы
        self.score = 0  # Количество правильных ответов
        self.repeats = 0  # Количество повторений
        self.current_index = 0  # Номер текущего слова
        self.dictionary_length = 0  # Количество слов в словаре
        self.words = []  # Список слов
        self.translations = []  # Список переводов
        self.words_order = []  # Случайный порядок слов

    @staticmethod
    # Генератор последовательности с минимальным количеством повторений
    def generate_sequence(repeats, length) -> list:
        sequence = []
        repeats *= length
        range_list = list(range(length))
        for i in range(repeats // length):
            shuffle(range_list)
            if len(sequence) and sequence[len(sequence) - 1] == range_list[0]:
                range_list[0], range_list[length - 1] = range_list[length - 1], range_list[0]
            sequence += range_list
        shuffle(range_list)
        if len(sequence) and sequence[len(sequence) - 1] == range_list[0]:
            range_list[0], range_list[length - 1] = range_list[length - 1], range_list[0]
        sequence += range_list[:repeats % length]
        return sequence

    def start(self, title, repeats):
        self.current_theme_title = title  # Заголовок темы
        self.repeats = repeats  # Количество повторений
        self.words, self.translations = self.helper.get_words_by_title(title)  # Списки слов и переводов
        self.dictionary_length = len(self.words)  # Количество слов в словаре
        self.current_index = 0  # Номер текущего слова
        self.score = 0  # Количество правильных ответов
        self.repeats *= self.dictionary_length

    # Вывод диалогового окна с результатом
    def show_result(self):
        dialog = InfoDialog(f'Ваш результат {self.score} из {self.repeats}')
        dialog.exec_()

    # Вывод диалогового с сообщением
    @staticmethod
    def not_enough_words():
        dialog = InfoDialog('Недостаточно слов в словаре')
        dialog.exec_()
