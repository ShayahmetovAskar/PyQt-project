from src.styles import Styles
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 81)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 55))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditWord = QtWidgets.QLineEdit(self.frame)
        self.lineEditWord.setObjectName("lineEdit")
        self.lineEditWord.setPlaceholderText('Введите слово')
        self.lineEditWord.setStyleSheet(Styles.style_line_edit)
        self.horizontalLayout.addWidget(self.lineEditWord)
        self.lineEditTranslation = QtWidgets.QLineEdit(self.frame)
        self.lineEditTranslation.setPlaceholderText('Введите перевод слова')
        self.lineEditTranslation.setObjectName("lineEdit_2")
        self.lineEditTranslation.setStyleSheet(Styles.style_line_edit)
        self.horizontalLayout.addWidget(self.lineEditTranslation)
        self.pushButtonAddToDictionary = QtWidgets.QPushButton(self.frame)
        self.pushButtonAddToDictionary.setObjectName("Добавить")
        self.pushButtonAddToDictionary.setStyleSheet(Styles.style_nice_button)
        self.horizontalLayout.addWidget(self.pushButtonAddToDictionary)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonAddToDictionary.setText(_translate("Form", "Добавить"))
