from src.colors import Colors


class Styles:
    style_menu_button = f"""
        QPushButton {{
            background-repeat: none;
            background-color: {Colors.get_color(Colors.menuButtonColor)};
            border: 2px solid;
            border-radius: 10px;
            color: {Colors.get_color(Colors.textColor)};
            background-position: center left;
            border-color: {Colors.get_color(Colors.menuButtonColor)};
        }}
        QPushButton:hover {{
            background-color: {Colors.get_color(Colors.menuButtonColorHover)};
            border: 2px solid;
            border-color: {Colors.get_color(Colors.menuButtonBorderColorHover)};
        }}
        QPushButton:pressed {{
            background-color: {Colors.get_color(Colors.colorAccent)};
        }}
    """

    style_dialog_button = f"""
        QPushButton {{
            width: 50px;
            height: 20px;
            border: 2px solid;
            border-color: {Colors.get_color(Colors.dialogBackground)};
            color: {Colors.get_color(Colors.colorAccent)};
        }}
        QPushButton:hover {{
            border: 2px solid;
            border-color: {Colors.get_color(Colors.menuButtonBorderColorHover)};
        }}
    """

    style_list_widget = f"""
        QListWidget {{
            border: none;
            color: {Colors.get_color(Colors.textColor)};
            font-size: 20px;
        }}
    """

    style_dictionary_pair = f"""
                            QFrame {{
                                background-color: {Colors.get_color(Colors.cardColor)};
                                border-radius: 4px;
                                
                            }}
                            QLabel {{
                                border: none;
                                font-size: 16px;
                                color: {Colors.get_color(Colors.textColor)};
                            }}
                            """
    style_frame = f"""
        QFrame {{
            background-color: {Colors.get_color(Colors.cardColor)};
            border-radius: 10px;
        }}
    """

    style_scroll_bar = """QScrollBar:horizontal {
                          height: 16px;
                          margin: 2px 16px 2px 16px;
                          border: 1px solid #32414B;
                          border-radius: 4px;
                          background-color: #19232D;
                        }
                        
                        QScrollBar:vertical {
                          background-color: #19232D;
                          width: 16px;
                          margin: 16px 2px 16px 2px;
                          border: 1px solid #32414B;
                          border-radius: 4px;
                        }
                        
                        QScrollBar::handle:horizontal {
                          background-color: #787878;
                          border: 1px solid #32414B;
                          border-radius: 4px;
                          min-width: 8px;
                        }
                        
                        QScrollBar::handle:horizontal:hover {
                          background-color: #148CD2;
                          border: 1px solid #148CD2;
                          border-radius: 4px;
                          min-width: 8px;
                        }
                        
                        QScrollBar::handle:horizontal:focus {
                          border: 1px solid #1464A0;
                        }
                        
                        QScrollBar::handle:vertical {
                          background-color: #787878;
                          border: 1px solid #32414B;
                          min-height: 8px;
                          border-radius: 4px;
                        }
                        
                        QScrollBar::handle:vertical:hover {
                          background-color: #148CD2;
                          border: 1px solid #148CD2;
                          border-radius: 4px;
                          min-height: 8px;
                        }
                        
                        QScrollBar::handle:vertical:focus {
                          border: 1px solid #1464A0;
                        }
                        
                        QScrollBar::add-line:horizontal {
                          margin: 0px 0px 0px 0px;
                          border-image: url("src/rc/arrow_right_disabled.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: right;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {
                          border-image: url("src/rc/arrow_right.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: right;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::add-line:vertical {
                          margin: 3px 0px 3px 0px;
                          border-image: url("src/rc/arrow_down_disabled.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: bottom;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {
                          border-image: url("src/rc/arrow_down.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: bottom;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::sub-line:horizontal {
                          margin: 0px 3px 0px 3px;
                          border-image: url("src/rc/arrow_left_disabled.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: left;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {
                          border-image: url("src/rc/arrow_left.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: left;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::sub-line:vertical {
                          margin: 3px 0px 3px 0px;
                          border-image: url("src/rc/arrow_up_disabled.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: top;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {
                          border-image: url("src/rc/arrow_up.png");
                          height: 12px;
                          width: 12px;
                          subcontrol-position: top;
                          subcontrol-origin: margin;
                        }
                        
                        QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
                          background: none;
                        }
                        
                        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                          background: none;
                        }
                        
                        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                          background: none;
                        }
                        
                        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                          background: none;
}"""

    style_nice_button = f"""QPushButton {{
                          background-color: {Colors.get_color(Colors.infoBarColor)};
                          color: #F0F0F0;
                          border-radius: 4px;
                          padding: 3px;
                          outline: none;
                          /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
                          min-width: 80px;
                        }}
                        
                        QPushButton:disabled {{
                          background-color: #32414B;
                          border: 1px solid #32414B;
                          color: #787878;
                          border-radius: 4px;
                          padding: 3px;
                        }}
                        
                        QPushButton:checked {{
                          background-color: #32414B;
                          border: 1px solid #32414B;
                          border-radius: 4px;
                          padding: 3px;
                          outline: none;
                        }}
                        
                        QPushButton:checked:disabled {{
                          background-color: #19232D;
                          border: 1px solid #32414B;
                          color: #787878;
                          border-radius: 4px;
                          padding: 3px;
                          outline: none;
                        }}
                        
                        QPushButton:checked:selected {{
                          background: #1464A0;
                          color: #32414B;
                        }}
                        
                        QPushButton::menu-indicator {{
                          subcontrol-origin: padding;
                          subcontrol-position: bottom right;
                          bottom: 4px;
                        }}
                        
                        QPushButton:pressed {{
                          background-color: #19232D;
                          border: 1px solid #19232D;
                        }}
                        
                        QPushButton:pressed:hover {{
                          border: 1px solid #148CD2;
                        }}
                        
                        QPushButton:hover {{
                          border: 1px solid #148CD2;
                          color: #F0F0F0;
                        }}
                        
                        QPushButton:selected {{
                          background: #1464A0;
                          color: #32414B;
                        }}
                        
                        QPushButton:hover {{
                          border: 1px solid #148CD2;
                          color: #F0F0F0;
                        }}
"""

    style_line_edit = """QLineEdit {
                          background-color: #19232D;
                          padding-top: 2px;
                          /* This QLineEdit fix  103, 111 */
                          padding-bottom: 2px;
                          /* This QLineEdit fix  103, 111 */
                          padding-left: 4px;
                          padding-right: 4px;
                          border-style: solid;
                          border: 1px solid #32414B;
                          border-radius: 4px;
                          color: #F0F0F0;
                        }
                        
                        QLineEdit:disabled {
                          background-color: #19232D;
                          color: #787878;
                        }
                        
                        QLineEdit:hover {
                          border: 1px solid #148CD2;
                          color: #F0F0F0;
                        }
                        
                        QLineEdit:focus {
                          border: 1px solid #1464A0;
                        }
                        
                        QLineEdit:selected {
                          background-color: #1464A0;
                          color: #32414B;
                        }"""

    style_label = f"""QLabel {{
                      border: 0px solid #32414B;
                      padding: 2px;
                      margin: 0px;
                      color: #F0F0F0;
                    }}
                    
                    QLabel:disabled {{
                      border: 0px solid #32414B;
                      color: #787878;
                    }}"""

    style_spinbox = """
QAbstractSpinBox {
  background-color: #19232D;
  border: 1px solid #32414B;
  color: #F0F0F0;
  /* This fixes 103, 111 */
  padding-top: 2px;
  /* This fixes 103, 111 */
  padding-bottom: 2px;
  padding-left: 4px;
  padding-right: 4px;
  border-radius: 4px;
  /* min-width: 5px; removed to fix 109 */
}

QAbstractSpinBox:up-button {
  background-color: transparent #19232D;
  subcontrol-origin: border;
  subcontrol-position: top right;
  border-left: 1px solid #32414B;
  border-bottom: 1px solid #32414B;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  margin: 1px;
  width: 12px;
  margin-bottom: -1px;
}

QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {
  image: url("src/rc/arrow_up_disabled.png");
  height: 8px;
  width: 8px;
}

QAbstractSpinBox::up-arrow:hover {
  image: url("src/rc/arrow_up.png");
}

QAbstractSpinBox:down-button {
  background-color: transparent #19232D;
  subcontrol-origin: border;
  subcontrol-position: bottom right;
  border-left: 1px solid #32414B;
  border-top: 1px solid #32414B;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  margin: 1px;
  width: 12px;
  margin-top: -1px;
}

QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {
  image: url("src/rc/arrow_down_disabled.png");
  height: 8px;
  width: 8px;
}

QAbstractSpinBox::down-arrow:hover {
  image: url("src/rc/arrow_down.png");
}

QAbstractSpinBox:hover {
  border: 1px solid #148CD2;
  color: #F0F0F0;
}

QAbstractSpinBox:focus {
  border: 1px solid #1464A0;
}

QAbstractSpinBox:selected {
  background: #1464A0;
  color: #32414B;
}
    """

    style_combo_box = """QComboBox {
    color: #F0F0F0;
  border: 1px solid #32414B;
  border-radius: 4px;
  selection-background-color: #1464A0;
  padding-left: 4px;
  padding-right: 36px;
  /* 4 + 16*2 See scrollbar size */
  /* Fixes #103, #111 */
  min-height: 1.5em;
  /* padding-top: 2px;     removed to fix #132 */
  /* padding-bottom: 2px;  removed to fix #132 */
  /* min-width: 75px;      removed to fix #109 */
  /* Needed to remove indicator - fix #132 */
}

QComboBox QAbstractItemView {
  border: 1px solid #32414B;
  border-radius: 0;
  background-color: #19232D;
  color: #F0F0F0;
  selection-background-color: #1464A0;
}

QComboBox QAbstractItemView:hover {
  background-color: #19232D;
  color: #F0F0F0;
}

QComboBox QAbstractItemView:selected {
  background: #1464A0;
  color: #32414B;
}

QComboBox QAbstractItemView:alternate {
  background: #19232D;
}

QComboBox:disabled {
  background-color: #19232D;
  color: #787878;
}

QComboBox:hover {
  border: 1px solid #148CD2;
}

QComboBox:focus {
  border: 1px solid #1464A0;
}

QComboBox:on {
  selection-background-color: #1464A0;
}

QComboBox::indicator {
  border: none;
  border-radius: 0;
  background-color: transparent;
  selection-background-color: transparent;
  color: transparent;
  selection-color: transparent;
  /* Needed to remove indicator - fix #132 */
}

QComboBox::indicator:alternate {
  background: #19232D;
}

QComboBox::item:alternate {
  background: #19232D;
}

QComboBox::item:checked {
  font-weight: bold;
}

QComboBox::item:selected {
  border: 0px solid transparent;
}

QComboBox::drop-down {
  subcontrol-origin: padding;
  subcontrol-position: top right;
  width: 12px;
  border-left: 1px solid #32414B;
}

QComboBox::down-arrow {
  image: url("src/rc/arrow_down_disabled.png");
  height: 8px;
  width: 8px;
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {
  image: url("src/rc/arrow_down.png");
}"""
