import sqlite3

DATABASE = 'database.sqlite'
TABLE_DICTIONARIES = 'dictionaries'
TABLE_DICTIONARIES_COLUMN = 'title'

TABLE_DICTIONARY_COLUMN_WORD = 'word'
TABLE_DICTIONARY_COLUMN_TRANSLATION = 'translation'


class Helper:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.connection.row_factory = lambda cursor, row: row[0]  # теперь SELECT возвращает список
        self.connection.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_DICTIONARIES} ({TABLE_DICTIONARIES_COLUMN} TEXT)")
        self.cursor = self.connection.cursor()

    # Возвращает список заголовков
    def get_titles(self) -> list:
        return self.cursor.execute(f"SELECT {TABLE_DICTIONARIES_COLUMN} FROM {TABLE_DICTIONARIES}").fetchall()

    # Добавляет заголовок
    def add_title(self, title: str) -> None:
        self.cursor.execute(f"INSERT INTO {TABLE_DICTIONARIES}({TABLE_DICTIONARIES_COLUMN}) VALUES(\"{title}\")")
        self.connection.execute(
            f"CREATE TABLE IF NOT EXISTS \"{title}\" "
            f"({TABLE_DICTIONARY_COLUMN_WORD} TEXT, {TABLE_DICTIONARY_COLUMN_TRANSLATION} TEXT)")
        self.connection.commit()

    # Удаляет заголовок и все слова, связанные с ним
    def delete_title(self, title: str) -> None:
        self.cursor.execute(f"DELETE FROM {TABLE_DICTIONARIES} WHERE title = \"{title}\"")
        self.connection.execute(f"DROP TABLE \"{title}\"")
        self.connection.commit()

    # Возвращает список слов и переводов
    def get_words_by_title(self, title: str) -> tuple:
        words = (self.cursor.execute(f"SELECT {TABLE_DICTIONARY_COLUMN_WORD} FROM \"{title}\"").fetchall())
        translations = (self.cursor.execute(f"SELECT {TABLE_DICTIONARY_COLUMN_TRANSLATION} FROM \"{title}\"").fetchall())
        return words, translations

    # Добавляет слово
    def add_word(self, value: str, word: str, translation: str) -> None:
        self.cursor.execute(
            f"INSERT INTO \"{value}\" ({TABLE_DICTIONARY_COLUMN_WORD}, {TABLE_DICTIONARY_COLUMN_TRANSLATION}) "
            f"VALUES(\"{word}\", \"{translation}\")")
        self.connection.commit()

    # Удаляет слово
    def delete_word(self, title: str, word: str, translation: str) -> None:
        self.cursor.execute(f"DELETE FROM \"{title}\" WHERE {TABLE_DICTIONARY_COLUMN_WORD} = \"{word}\" AND "
                            f"{TABLE_DICTIONARY_COLUMN_TRANSLATION} = \"{translation}\"")
        self.connection.commit()
