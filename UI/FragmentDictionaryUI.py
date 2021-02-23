from src.colors import Colors
from src.styles import Styles
from Elements.WordInput import WordInput
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 333)
        self.horizontalLayout = QtWidgets.QVBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_titles = QtWidgets.QListWidget(self.page)
        self.listWidget_titles.setStyleSheet(Styles.style_list_widget)
        self.listWidget_titles.setSpacing(5)
        self.listWidget_titles.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget_titles)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_words = QtWidgets.QListWidget(self.page_2)
        self.listWidget_words.setObjectName("tableWidgetWords")
        self.listWidget_words.setStyleSheet(Styles.style_list_widget)
        self.verticalLayout_4.addWidget(self.listWidget_words)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.wordInput = WordInput()
        self.wordInput.setObjectName("wordInput")
        self.wordInput.setProperty('maximumHeight', 0)
        self.wordInput.setStyleSheet(
            f"background-color: {Colors.get_color(Colors.wordInputBackground)};"
            f"border-radius: 10px;"
            f"border: 1px solid grey;")
        self.horizontalLayout.addWidget(self.wordInput)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
