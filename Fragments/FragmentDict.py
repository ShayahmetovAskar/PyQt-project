from os import listdir
from UI.FragmentDictionaryUI import Ui_Form
from Dialogs.InfoDialog import InfoDialog
from Dialogs.InputDialog import InputDialog
from Dialogs.ConfirmationDialog import ConfirmationDialog
from db_helper import Helper
from Elements.DictionaryTitle import DictionaryTitle
from Elements.DictionaryPair import DictionaryPair
from PyQt5 import QtCore, QtWidgets
import threading
import pyttsx3


# Словарь пользователя
class DictFragment(QtWidgets.QWidget, Ui_Form):
    def __init__(self, stacked_widget_top_bar: QtWidgets.QStackedWidget, top_bar_widget1,
                 top_bar_widget2):
        super().__init__()
        self.setupUi(self)
        self.engine = pyttsx3.init()
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        self.engine.setProperty('voice', voice_id)

        # Верхняя панель
        self.stacked_widget_top_bar = stacked_widget_top_bar

        # Элемент верхней панели в окне с названиями тем словарей
        self.top_bar_widget1 = top_bar_widget1
        # Кнопки этой панели
        self.top_bar_widget1.pushButtonAddTheme.clicked.connect(self.button_add_theme_clicked)
        self.top_bar_widget1.pushButtonDeleteTheme.clicked.connect(self.button_delete_theme_clicked)

        # Элемент верхней панели в окне со словами словаря
        self.top_bar_widget2 = top_bar_widget2
        # Кнопки этой панели
        self.top_bar_widget2.pushButtonGoBack.clicked.connect(self.button_back_clicked)
        self.top_bar_widget2.pushButtonImport.clicked.connect(self.import_file)
        self.top_bar_widget2.pushButtonExport.clicked.connect(self.export_file)

        # Элемент предназначенный для ввода слов в словарь
        self.wordInput.pushButtonAddToDictionary.clicked.connect(self.button_add_word_clicked)
        self.wordInputAnimation = QtCore.QPropertyAnimation(self.wordInput, b'maximumHeight')
        self.wordInputAnimation.setEasingCurve(QtCore.QEasingCurve.OutBack)

        # Список тем
        self.listWidget_titles.itemSelectionChanged.connect(self.item_selected)
        self.listWidget_titles.setUniformItemSizes(True)
        # Список слов
        self.listWidget_words.setSpacing(2)
        self.listWidget_words.setUniformItemSizes(True)

        self.selected_item_index = None  # Индекс выбранного элемента в списке тем
        self.top_panel_page = 1  # Страница верхней панели
        self.current_title = None  # Выбранная тема. Используется для отображения слов во втором окне
        self.button_to_label = dict()  # Соответствие кнопки к заголовку темы
        self.button_to_index = dict()  # Порядковый номер кнопки удаления слов
        self.button_speech_to_word = dict()  # Слово, соответствующее кнопке озвучивания
        self.db_helper = Helper()  # Помощник по бд

        self.theme_titles = []  # Список заголовков тем
        self.words = []  # Список слов определенной тем
        self.translations = []  # Список переводов слов определенной темы

        self.list_widget1_set_data()  # Заполнение списка тем

    # Добавление новой темы
    def button_add_theme_clicked(self):
        # Вызов диалогового окна ввода и получение результата
        dialog = InputDialog()
        value = dialog.get_text()
        if value is not None and len(value) != 0:  # Проверка входных данных
            # Если тема уже содержится в базе данных, то к названию добавляется цифра
            if value in self.theme_titles:
                c = 2
                while True:
                    if value + '_' + str(c) not in self.theme_titles:
                        value = value + '_' + str(c)
                        break
                    c += 1
            # Добавление в базу данных и обновление списка
            self.db_helper.add_title(value)
            self.list_widget1_set_data()

    # Заполнение списка тем
    def list_widget1_set_data(self):
        self.listWidget_titles.clear()
        self.button_to_label.clear()
        # Обновление списка тем
        self.theme_titles = self.db_helper.get_titles()
        # Заполнение списка элементами
        for i in range(len(self.theme_titles)):
            item = QtWidgets.QListWidgetItem()
            item.setData(0, i)
            wdt = DictionaryTitle()
            wdt.pushButton.setText(f'Перейти')
            wdt.pushButton.clicked.connect(self.button_goto_theme_clicked)
            wdt.label.setText(str(self.theme_titles[i]))
            self.button_to_label[wdt.pushButton] = str(self.theme_titles[i])
            item.setSizeHint(wdt.sizeHint())
            self.listWidget_titles.addItem(item)
            self.listWidget_titles.setItemWidget(item, wdt)

    # Удаление темы
    def button_delete_theme_clicked(self):
        # Проверка на наличие выбранного элемента
        if self.selected_item_index is not None:
            # Подтверждение удаления
            confirmation = ConfirmationDialog(
                "Действительно удалить?").get_results()  # Вызов диалогового окна
            if not confirmation:
                return
            # Удаление из базы данных и обновление списка
            self.db_helper.delete_title(self.theme_titles[self.selected_item_index])
            self.list_widget1_set_data()
            self.selected_item_index = None

    # Переход к выбранной теме
    def button_goto_theme_clicked(self):
        self.stackedWidget.setCurrentIndex(1)  # Переключение страницы основного окна
        self.stacked_widget_top_bar.setCurrentIndex(2)  # Переключение страницы верхней панели
        self.word_input_animation(True)  # Анимация поля ввода слов
        self.top_panel_page = 2
        self.current_title = (self.button_to_label[self.sender()])
        # Установка элементов в список
        self.list_widget2_set_data_words()

    # Переход со словаря к списку тем
    def button_back_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stacked_widget_top_bar.setCurrentIndex(1)
        self.word_input_animation(False)  # Обратная анимация поля ввода слов
        self.top_panel_page = 1
        self.current_title = None

    # Добавление слова в словарь
    def button_add_word_clicked(self):
        # Считывание данных с полей ввода
        word = self.wordInput.lineEditWord.text().strip()
        translation = self.wordInput.lineEditTranslation.text().strip()
        # Проверка введенных данных
        if len(word.strip()) != 0 and len(translation) != 0:
            # Проверка на содержание в базе данных
            if word not in self.words and translation not in self.translations:
                # Добавление в базу данных
                self.db_helper.add_word(self.current_title, word, translation)
                # Очистка полей ввода
                self.wordInput.lineEditWord.setText('')
                self.wordInput.lineEditTranslation.setText('')
                # Обновление списка и прокручивание его вниз
                self.list_widget2_set_data_words()
                self.listWidget_words.scrollToBottom()

    # Заполнение словаря
    def list_widget2_set_data_words(self):
        # Обновление списков
        self.words, self.translations = self.db_helper.get_words_by_title(self.current_title)
        self.listWidget_words.clear()
        for i in range(len(self.words)):
            item = QtWidgets.QListWidgetItem()
            item.setData(0, i + 1)
            wdt = DictionaryPair()
            wdt.label.setText(str(i + 1))
            wdt.label_2.setText(self.words[i])
            wdt.label_3.setText(self.translations[i])
            item.setSizeHint(wdt.sizeHint())
            self.button_to_index[wdt.pushButton] = i
            self.button_speech_to_word[wdt.pushButtonSpeech] = self.words[i]
            wdt.pushButton.clicked.connect(self.button_delete_word_clicked)
            wdt.pushButtonSpeech.clicked.connect(self.voice)
            self.listWidget_words.addItem(item)
            self.listWidget_words.setItemWidget(item, wdt)

    # Удаление слова из словаря
    def button_delete_word_clicked(self):
        index = self.button_to_index[self.sender()]  # Номер нажатой кнопки
        # Удаление из базы данных и обновление списка
        self.db_helper.delete_word(self.current_title, self.words[index], self.translations[index])
        self.list_widget2_set_data_words()

    # Сохранение номера выбранного элемента списка тем
    def item_selected(self):
        if len(self.listWidget_titles.selectedItems()):
            self.selected_item_index = self.listWidget_titles.selectedItems()[0].data(0)

    # Анимация поля ввода слов
    def word_input_animation(self, direction):
        self.wordInputAnimation.setStartValue(0 if direction else 55)
        self.wordInputAnimation.setEndValue(55 if direction else 0)
        self.wordInputAnimation.setDuration(250)
        self.wordInputAnimation.start()

    def voice(self):
        threading.Thread(
            target=self.text_to_speech, args=(self.sender(),), daemon=True
        ).start()

    # Озвучивание слова
    def text_to_speech(self, sender):
        self.engine.say(self.button_speech_to_word[sender])
        try:
            self.engine.runAndWait()
        except RuntimeError:
            pass

    # Ввод данных в словарь из
    def import_file(self):
        # Выбор файла
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '', '(*.txt);; Все файлы (*)')[0]
        # Проверка названия файла на пустоту
        if len(filename) == 0:
            return
        file = open(filename, encoding='utf8')
        data = file.read()  # Чтение данных из файла
        file.close()

        # Проверка содержимого файла на пустоту
        if len(data.splitlines()) == 0:
            info_dialog = InfoDialog('Выбранный файл пуст. Изменения не внесены')
            info_dialog.exec_()
            return

        f_words, f_translations = [], []  # Данные из файла
        c = 1
        # Построчное чтение файла
        for line in data.splitlines():
            try:
                if '"' in line:
                    raise IncorrectSymbol
                f_word, f_translation = line.split(';')  # Чтение слова и перевода слова из строки
            except ValueError:  # В случае ошибки вызывается диалоговое окно с информацией
                info_dialog = InfoDialog(f'Ошибка в строке {c}. Изменения не внесены')
                info_dialog.exec_()
                return
            except IncorrectSymbol:
                info_dialog = InfoDialog(
                    f'Недопустимый символ (") в строке {c}. Изменения не внесены')
                info_dialog.exec_()
                return
            except Exception:
                info_dialog = InfoDialog(f'Ошибква в файле')
                info_dialog.exec_()
                return
            f_words.append(f_word)
            f_translations.append(f_translation)
            c += 1

        # Подтверждение
        confirmation_dialog = ConfirmationDialog('Данные словаря будут переписаны.\nПродолжить?')
        result = confirmation_dialog.get_results()

        # Выход из функции при отклонении подтверждения
        if not result:
            return

        # Удаление старых слов из базы данных
        for word, translation in zip(self.words, self.translations):
            self.db_helper.delete_word(self.current_title, word, translation)
        # Внесение новых слов в базу данных
        for word, translation in zip(f_words, f_translations):
            self.db_helper.add_word(self.current_title, word, translation)
        # Обновление списка
        self.list_widget2_set_data_words()

    # Сохранение словаря в файл
    def export_file(self):
        # Выбор директории
        pathname = QtWidgets.QFileDialog.getExistingDirectory()
        # Выход из функции если директории нет
        if len(pathname) == 0:
            return

        files = listdir(pathname)  # Список всех файлов в выбранной директории
        filename = self.current_title  # Название сохраняемого файла
        # Проверка на наличие файла с таким же названием в выбранной директории
        if filename + '.txt' in files:
            c = 2
            # Добавление числа к файлу, до тех пор, пока название не окажется свободным
            while True:
                if filename + '_' + str(c) + '.txt' not in files:
                    break
                c += 1
            filename = filename + '_' + str(c)
        filename += '.txt'
        file = open(filename, 'a', encoding='utf8')
        for word, translation in zip(self.words, self.translations):
            file.write(
                word + ";" + translation + "\n")  # Построчная запись в файл в виде слово;перевод
        file.close()


class IncorrectSymbol(Exception):
    pass
