import PySide6.QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
                               QMenuBar, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
                               QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget, QGraphicsLineItem, QAbstractItemView)
import ui_files.dark_blue.style


models=['MOD. 2021','MOD. 2024']
opciones= ['TODO','COMPLETO','INCOMPLETO']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 600)
        MainWindow.setStyleSheet(u" /*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR AN"
                        "Y CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
""
                        "{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #FEC614;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #FFFFFF;\n"
"    margin-bottom: 2px;\n"
"    background: rgba(142,153,162,80);\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/chec"
                        "kbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeter"
                        "minate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
""
                        "QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
""
                        "    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"  "
                        " (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:chec"
                        "ked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #3"
                        "02F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
""
                        "{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
""
                        "{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
""
                        "    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: rgba(31,31,31,150);\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #000000;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
""
                        "QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-col"
                        "or: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #FFFFFF;\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #E4CD80;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F"
                        ";\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"/*QPushButton:focus {\n"
"    \n"
"    color: white;\n"
"}*/\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"	color: #FEC614;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FEC614;\n"
"    border: 2px solid #78879b;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color"
                        ": silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: #FEC614;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
""
                        "    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:of"
                        "f\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{   background-color: transparent;\n"
"    color: #FFFFFF;\n"
"	border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/d"
                        "ark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
""
                        "QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
""
                        "/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton:"
                        ":left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branc"
                        "h:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView"
                        "::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #FEC614;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
""
                        "\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button *"
                        "/\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arr"
                        "ow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #FEC614;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;"
                        "\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: "
                        "2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
""
                        "QListWidget {\n"
"    background-color: rgba(192,192,192,150);\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon	: url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon	: url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon	: url(:/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"\n"
"\n"
"\n"
"#centralwidget{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}\n"
"\n"
"Line{\n"
""
                        " background-color:#FBCC1A;\n"
"}\n"
"\n"
"#logo{\n"
"	border-image: url(:/dark_blue/img/logoCat.png);\n"
"	border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-size: expanding; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"#tab{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dataTableLog = QTableWidget(self.tab)
        if (self.dataTableLog.columnCount() < 7):
            self.dataTableLog.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.dataTableLog.rowCount() < 13):
            self.dataTableLog.setRowCount(13)
        self.dataTableLog.setObjectName(u"dataTableLog")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTableLog.sizePolicy().hasHeightForWidth())
        self.dataTableLog.setSizePolicy(sizePolicy)
        self.dataTableLog.setFrameShape(QFrame.Panel)
        self.dataTableLog.setFrameShadow(QFrame.Plain)
        self.dataTableLog.setLineWidth(1)
        self.dataTableLog.setMidLineWidth(2)
        self.dataTableLog.setGridStyle(Qt.SolidLine)
        self.dataTableLog.setSortingEnabled(False)
        self.dataTableLog.setRowCount(13)
        self.dataTableLog.setColumnCount(7)
        self.dataTableLog.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableLog.horizontalHeader().setHighlightSections(False)
        self.dataTableLog.horizontalHeader().setProperty("showSortIndicator", False)
        self.dataTableLog.horizontalHeader().setStretchLastSection(True)
        self.dataTableLog.verticalHeader().setCascadingSectionResizes(True)
        self.dataTableLog.verticalHeader().setProperty("showSortIndicator", False)
        self.dataTableLog.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.dataTableLog)

        self.horizontalSpacer_3 = QSpacerItem(800, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBoxLog = QCheckBox(self.tab)
        self.checkBoxLog.setObjectName(u"checkBoxLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBoxLog.sizePolicy().hasHeightForWidth())
        self.checkBoxLog.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.checkBoxLog)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lineEditDesdeLog = QLineEdit(self.tab)
        self.lineEditDesdeLog.setObjectName(u"lineEditDesdeLog")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditDesdeLog.sizePolicy().hasHeightForWidth())
        self.lineEditDesdeLog.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.lineEditDesdeLog)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEditHastaLog = QLineEdit(self.tab)
        self.lineEditHastaLog.setObjectName(u"lineEditHastaLog")
        sizePolicy2.setHeightForWidth(self.lineEditHastaLog.sizePolicy().hasHeightForWidth())
        self.lineEditHastaLog.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.lineEditHastaLog)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushBuscarLog = QPushButton(self.tab)
        self.pushBuscarLog.setObjectName(u"pushBuscarLog")
        sizePolicy1.setHeightForWidth(self.pushBuscarLog.sizePolicy().hasHeightForWidth())
        self.pushBuscarLog.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushBuscarLog)

        self.labelModel = QLabel(self.tab)
        self.labelModel.setObjectName(u"labelModel")

        self.verticalLayout.addWidget(self.labelModel)

        self.comboModelLog = QComboBox(self.tab)
        self.comboModelLog.setObjectName(u"comboModelLog")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboModelLog.sizePolicy().hasHeightForWidth())
        self.comboModelLog.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.comboModelLog)

        self.labelStatus = QLabel(self.tab)
        self.labelStatus.setObjectName(u"labelStatus")

        self.verticalLayout.addWidget(self.labelStatus)

        self.comboStatusLog = QComboBox(self.tab)
        self.comboStatusLog.setObjectName(u"comboStatusLog")
        sizePolicy3.setHeightForWidth(self.comboStatusLog.sizePolicy().hasHeightForWidth())
        self.comboStatusLog.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.comboStatusLog)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushBuscarEnLogs = QPushButton(self.tab)
        self.pushBuscarEnLogs.setObjectName(u"pushBuscarEnLogs")

        self.horizontalLayout_3.addWidget(self.pushBuscarEnLogs)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 232, 64))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelDataView = QLabel(self.scrollAreaWidgetContents_2)
        self.labelDataView.setObjectName(u"labelDataView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelDataView.sizePolicy().hasHeightForWidth())
        self.labelDataView.setSizePolicy(sizePolicy5)
        self.labelDataView.setFrameShape(QFrame.Panel)
        self.labelDataView.setFrameShadow(QFrame.Sunken)
        self.labelDataView.setTextFormat(Qt.AutoText)
        self.labelDataView.setScaledContents(False)
        self.labelDataView.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.labelDataView)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add2DataBase = QPushButton(self.tab)
        self.add2DataBase.setObjectName(u"add2DataBase")

        self.horizontalLayout_4.addWidget(self.add2DataBase)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"#tab_2{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_11 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.dataTableSQL = QTableWidget(self.tab_2)
        if (self.dataTableSQL.columnCount() < 7):
            self.dataTableSQL.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        if (self.dataTableSQL.rowCount() < 13):
            self.dataTableSQL.setRowCount(13)
        self.dataTableSQL.setObjectName(u"dataTableSQL")
        sizePolicy.setHeightForWidth(self.dataTableSQL.sizePolicy().hasHeightForWidth())
        self.dataTableSQL.setSizePolicy(sizePolicy)
        self.dataTableSQL.setFrameShape(QFrame.Panel)
        self.dataTableSQL.setFrameShadow(QFrame.Plain)
        self.dataTableSQL.setLineWidth(1)
        self.dataTableSQL.setMidLineWidth(2)
        self.dataTableSQL.setGridStyle(Qt.SolidLine)
        self.dataTableSQL.setSortingEnabled(False)
        self.dataTableSQL.setRowCount(13)
        self.dataTableSQL.setColumnCount(7)
        self.dataTableSQL.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableSQL.horizontalHeader().setHighlightSections(False)
        self.dataTableSQL.horizontalHeader().setProperty("showSortIndicator", False)
        self.dataTableSQL.horizontalHeader().setStretchLastSection(True)
        self.dataTableSQL.verticalHeader().setCascadingSectionResizes(True)
        self.dataTableSQL.verticalHeader().setProperty("showSortIndicator", False)
        self.dataTableSQL.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.dataTableSQL)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_info = QLabel(self.tab_2)
        self.label_info.setObjectName(u"label_info")

        self.horizontalLayout_17.addWidget(self.label_info)

        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_17.addItem(self.verticalSpacer_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalSpacer_12 = QSpacerItem(800, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_12)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBoxSQL = QCheckBox(self.tab_2)
        self.checkBoxSQL.setObjectName(u"checkBoxSQL")
        sizePolicy1.setHeightForWidth(self.checkBoxSQL.sizePolicy().hasHeightForWidth())
        self.checkBoxSQL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.checkBoxSQL)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.lineEditDesdeSQL = QLineEdit(self.tab_2)
        self.lineEditDesdeSQL.setObjectName(u"lineEditDesdeSQL")
        sizePolicy2.setHeightForWidth(self.lineEditDesdeSQL.sizePolicy().hasHeightForWidth())
        self.lineEditDesdeSQL.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.lineEditDesdeSQL)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.lineEditHastaSQL = QLineEdit(self.tab_2)
        self.lineEditHastaSQL.setObjectName(u"lineEditHastaSQL")
        sizePolicy2.setHeightForWidth(self.lineEditHastaSQL.sizePolicy().hasHeightForWidth())
        self.lineEditHastaSQL.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.lineEditHastaSQL)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.labelModel_3 = QLabel(self.tab_2)
        self.labelModel_3.setObjectName(u"labelModel_3")

        self.verticalLayout_9.addWidget(self.labelModel_3)

        self.comboModelSQL = QComboBox(self.tab_2)
        self.comboModelSQL.setObjectName(u"comboModelSQL")
        sizePolicy3.setHeightForWidth(self.comboModelSQL.sizePolicy().hasHeightForWidth())
        self.comboModelSQL.setSizePolicy(sizePolicy3)

        self.verticalLayout_9.addWidget(self.comboModelSQL)

        self.labelStatus_3 = QLabel(self.tab_2)
        self.labelStatus_3.setObjectName(u"labelStatus_3")

        self.verticalLayout_9.addWidget(self.labelStatus_3)

        self.comboStatusSQL = QComboBox(self.tab_2)
        self.comboStatusSQL.setObjectName(u"comboStatusSQL")
        sizePolicy3.setHeightForWidth(self.comboStatusSQL.sizePolicy().hasHeightForWidth())
        self.comboStatusSQL.setSizePolicy(sizePolicy3)

        self.verticalLayout_9.addWidget(self.comboStatusSQL)

        self.verticalSpacer_16 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer_16)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushBuscarSQL = QPushButton(self.tab_2)
        self.pushBuscarSQL.setObjectName(u"pushBuscarSQL")

        self.horizontalLayout_19.addWidget(self.pushBuscarSQL)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_29)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 220, 50))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labelDataSql = QLabel(self.scrollAreaWidgetContents)
        self.labelDataSql.setObjectName(u"labelDataSql")

        self.verticalLayout_16.addWidget(self.labelDataSql)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_7.addWidget(self.scrollArea)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pb_getDatapz = QPushButton(self.tab_2)
        self.pb_getDatapz.setObjectName(u"pb_getDatapz")

        self.horizontalLayout_18.addWidget(self.pb_getDatapz)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_28)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_17)

        self.pb_getReport = QPushButton(self.tab_2)
        self.pb_getReport.setObjectName(u"pb_getReport")

        self.verticalLayout_9.addWidget(self.pb_getReport)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.horizontalSpacer_14 = QSpacerItem(160, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_14)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"#tab_3{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.verticalSpacer_7)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSpacer_15 = QSpacerItem(100, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_15)

        self.logo = QLabel(self.tab_3)
        self.logo.setObjectName(u"logo")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy7)

        self.verticalLayout_11.addWidget(self.logo)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_13 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_13)

        self.line = QFrame(self.tab_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_10.addItem(self.verticalSpacer_8)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_11.addItem(self.verticalSpacer_3)

        self.event_list = QListWidget(self.tab_3)
        QListWidgetItem(self.event_list)
        QListWidgetItem(self.event_list)
        QListWidgetItem(self.event_list)
        QListWidgetItem(self.event_list)
        self.event_list.setObjectName(u"event_list")

        self.horizontalLayout_11.addWidget(self.event_list)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_26)

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_16.addWidget(self.pushButton)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_27)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_18)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_12.addItem(self.verticalSpacer_4)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8)

        self.client_cb = QComboBox(self.tab_3)
        self.client_cb.addItem("")
        self.client_cb.addItem("")
        self.client_cb.setObjectName(u"client_cb")

        self.verticalLayout_13.addWidget(self.client_cb)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_13.addItem(self.verticalSpacer_10)

        self.msg_edit = QTextEdit(self.tab_3)
        self.msg_edit.setObjectName(u"msg_edit")

        self.horizontalLayout_13.addWidget(self.msg_edit)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_15.addItem(self.verticalSpacer_11)

        self.sendMsg_bt = QPushButton(self.tab_3)
        self.sendMsg_bt.setObjectName(u"sendMsg_bt")

        self.horizontalLayout_15.addWidget(self.sendMsg_bt)

        self.sendAll_cb = QCheckBox(self.tab_3)
        self.sendAll_cb.setObjectName(u"sendAll_cb")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.sendAll_cb.sizePolicy().hasHeightForWidth())
        self.sendAll_cb.setSizePolicy(sizePolicy8)
        self.sendAll_cb.setIconSize(QSize(0, 0))

        self.horizontalLayout_15.addWidget(self.sendAll_cb)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_23)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_24)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_25)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 790, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)

        #######################################

        self.dataTableSQL.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.comboModelSQL.addItems(models)
        self.comboModelLog.addItems(models)
        self.comboStatusSQL.addItems(opciones)

        self.checkBoxSQL.clicked.connect(self.enablerange)
        self.lineEditDesdeSQL.setEnabled(False)
        self.lineEditHastaSQL.setEnabled(False)

        self.dataTableSQL.removeColumn(self.dataTableSQL.columnCount() - 1)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REGISTROS CATERPILLAR", None))
        ___qtablewidgetitem = self.dataTableLog.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem1 = self.dataTableLog.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ET05", None));
        ___qtablewidgetitem2 = self.dataTableLog.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ET04", None));
        ___qtablewidgetitem3 = self.dataTableLog.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ET03", None));
        ___qtablewidgetitem4 = self.dataTableLog.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ET02", None));
        ___qtablewidgetitem5 = self.dataTableLog.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ET01", None));
        ___qtablewidgetitem6 = self.dataTableLog.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.checkBoxLog.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Desde : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hasta : ", None))
        self.pushBuscarLog.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.labelModel.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.labelStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.pushBuscarEnLogs.setText(QCoreApplication.translate("MainWindow", u"Buscar en logs", None))
        self.labelDataView.setText(QCoreApplication.translate("MainWindow", u"dwfdfdfdsfffffffffffffffffffffffffff\n"
"ffffffffffffffff\n"
"ffffffffffffffffffffffsdsdsfdsfdsewdewdewdewd\n"
"ew", None))
        self.add2DataBase.setText(QCoreApplication.translate("MainWindow", u"Agregar a Base de Datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Log Data", None))
        ___qtablewidgetitem7 = self.dataTableSQL.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem8 = self.dataTableSQL.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ET05", None));
        ___qtablewidgetitem9 = self.dataTableSQL.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ET04", None));
        ___qtablewidgetitem10 = self.dataTableSQL.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ET03", None));
        ___qtablewidgetitem11 = self.dataTableSQL.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ET02", None));
        ___qtablewidgetitem12 = self.dataTableSQL.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ET01", None));
        ___qtablewidgetitem13 = self.dataTableSQL.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Piezas status INCOMPLETO MOD. 2024 en el rango [0,10]", None))
        self.checkBoxSQL.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Desde : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hasta : ", None))
        self.labelModel_3.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.labelStatus_3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.pushBuscarSQL.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.labelDataSql.setText(QCoreApplication.translate("MainWindow", u"ffffffffffffffsdsdsfdsfdsewdewdewdewd\n"
"ew", None))
        self.pb_getDatapz.setText(QCoreApplication.translate("MainWindow", u"Ver datos de pieza", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"SQL Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Server status", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.logo.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Server event", None))

        __sortingEnabled = self.event_list.isSortingEnabled()
        self.event_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.event_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nueva conexion 192.168.100.10", None));
        ___qlistwidgetitem1 = self.event_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mensaje 192.168.100.10 : Proceso terminado", None));
        ___qlistwidgetitem2 = self.event_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nueva conexion 192.168.100.8", None));
        ___qlistwidgetitem3 = self.event_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Desconexion 192.168.100.10", None));
        self.event_list.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select client", None))
        self.client_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"192.168.100.10", None))
        self.client_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"192.168.100.8", None))

        self.msg_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hola desde el server</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.sendMsg_bt.setText(QCoreApplication.translate("MainWindow", u"Send Mensage", None))
        self.sendAll_cb.setText(QCoreApplication.translate("MainWindow", u"Send all", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Server", None))
        self.pb_getReport.setText(QCoreApplication.translate("MainWindow", u"Generar reporte", None))
    # retranslateUi


    def enablerange(self, state):
        self.lineEditDesdeSQL.setEnabled(state)
        self.lineEditHastaSQL.setEnabled(state)


"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 600)
        MainWindow.setStyleSheet(u" /*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR AN"
                        "Y CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
""
                        "{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #FEC614;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #FFFFFF;\n"
"    margin-bottom: 2px;\n"
"    background: rgba(142,153,162,80);\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/chec"
                        "kbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeter"
                        "minate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
""
                        "QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
""
                        "    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"  "
                        " (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:chec"
                        "ked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
" border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #3"
                        "02F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
""
                        "{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
""
                        "{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
""
                        "    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: rgba(31,31,31,150);\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #000000;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
""
                        "QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-col"
                        "or: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #FFFFFF;\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #E4CD80;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F"
                        ";\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"/*QPushButton:focus {\n"
"    \n"
"    color: white;\n"
"}*/\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"	color: #FEC614;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FEC614;\n"
"    border: 2px solid #78879b;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color"
                        ": silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: #FEC614;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
""
                        "    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:of"
                        "f\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{   background-color: transparent;\n"
"    color: #FFFFFF;\n"
"	border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/d"
                        "ark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
""
                        "QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
""
                        "/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton:"
                        ":left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branc"
                        "h:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView"
                        "::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #FEC614;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
""
                        "\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button *"
                        "/\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arr"
                        "ow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #FEC614;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;"
                        "\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: "
                        "2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
""
                        "QListWidget {\n"
"    background-color: rgba(192,192,192,150);\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon	: url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon	: url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon	: url(:/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"\n"
"\n"
"\n"
"#centralwidget{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}\n"
"#line{\n"
" background-color:#FBCC1A;\n"
"}\n"
"\n"
"#logo{\n"
"	border-image: url(:/dark_blue/img/logoCat.png);\n"
"	border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-size: expanding; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")


        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"#tab{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dataTableLog = QTableWidget(self.tab)
        if (self.dataTableLog.columnCount() < 7):
            self.dataTableLog.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.dataTableLog.rowCount() < 13):
            self.dataTableLog.setRowCount(13)
        self.dataTableLog.setObjectName(u"dataTableLog")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTableLog.sizePolicy().hasHeightForWidth())
        self.dataTableLog.setSizePolicy(sizePolicy)
        self.dataTableLog.setFrameShape(QFrame.Panel)
        self.dataTableLog.setFrameShadow(QFrame.Plain)
        self.dataTableLog.setLineWidth(1)
        self.dataTableLog.setMidLineWidth(2)
        self.dataTableLog.setGridStyle(Qt.SolidLine)
        self.dataTableLog.setSortingEnabled(False)
        self.dataTableLog.setRowCount(13)
        self.dataTableLog.setColumnCount(7)
        self.dataTableLog.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableLog.horizontalHeader().setHighlightSections(False)
        self.dataTableLog.horizontalHeader().setProperty("showSortIndicator", False)
        self.dataTableLog.horizontalHeader().setStretchLastSection(True)
        self.dataTableLog.verticalHeader().setCascadingSectionResizes(True)
        self.dataTableLog.verticalHeader().setProperty("showSortIndicator", False)
        self.dataTableLog.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.dataTableLog)

        self.horizontalSpacer_3 = QSpacerItem(800, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBoxLog = QCheckBox(self.tab)
        self.checkBoxLog.setObjectName(u"checkBoxLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBoxLog.sizePolicy().hasHeightForWidth())
        self.checkBoxLog.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.checkBoxLog)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lineEditDesdeLog = QLineEdit(self.tab)
        self.lineEditDesdeLog.setObjectName(u"lineEditDesdeLog")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditDesdeLog.sizePolicy().hasHeightForWidth())
        self.lineEditDesdeLog.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.lineEditDesdeLog)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEditHastaLog = QLineEdit(self.tab)
        self.lineEditHastaLog.setObjectName(u"lineEditHastaLog")
        sizePolicy2.setHeightForWidth(self.lineEditHastaLog.sizePolicy().hasHeightForWidth())
        self.lineEditHastaLog.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.lineEditHastaLog)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushBuscarLog = QPushButton(self.tab)
        self.pushBuscarLog.setObjectName(u"pushBuscarLog")
        sizePolicy1.setHeightForWidth(self.pushBuscarLog.sizePolicy().hasHeightForWidth())
        self.pushBuscarLog.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushBuscarLog)

        self.labelModel = QLabel(self.tab)
        self.labelModel.setObjectName(u"labelModel")

        self.verticalLayout.addWidget(self.labelModel)

        self.comboModelLog = QComboBox(self.tab)
        self.comboModelLog.setObjectName(u"comboModelLog")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboModelLog.sizePolicy().hasHeightForWidth())
        self.comboModelLog.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.comboModelLog)

        self.labelStatus = QLabel(self.tab)
        self.labelStatus.setObjectName(u"labelStatus")

        self.verticalLayout.addWidget(self.labelStatus)

        self.comboStatusLog = QComboBox(self.tab)
        self.comboStatusLog.setObjectName(u"comboStatusLog")
        sizePolicy3.setHeightForWidth(self.comboStatusLog.sizePolicy().hasHeightForWidth())
        self.comboStatusLog.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.comboStatusLog)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushBuscarEnLogs = QPushButton(self.tab)
        self.pushBuscarEnLogs.setObjectName(u"pushBuscarEnLogs")

        self.horizontalLayout_3.addWidget(self.pushBuscarEnLogs)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 232, 64))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelDataView = QLabel(self.scrollAreaWidgetContents_2)
        self.labelDataView.setObjectName(u"labelDataView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelDataView.sizePolicy().hasHeightForWidth())
        self.labelDataView.setSizePolicy(sizePolicy5)
        self.labelDataView.setFrameShape(QFrame.Panel)
        self.labelDataView.setFrameShadow(QFrame.Sunken)
        self.labelDataView.setTextFormat(Qt.AutoText)
        self.labelDataView.setScaledContents(False)
        self.labelDataView.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.labelDataView)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add2DataBase = QPushButton(self.tab)
        self.add2DataBase.setObjectName(u"add2DataBase")

        self.horizontalLayout_4.addWidget(self.add2DataBase)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"#tab_2{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_11 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.dataTableSQL = QTableWidget(self.tab_2)
        if (self.dataTableSQL.columnCount() < 7):
            self.dataTableSQL.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        if (self.dataTableSQL.rowCount() < 13):
            self.dataTableSQL.setRowCount(13)
        self.dataTableSQL.setObjectName(u"dataTableSQL")
        sizePolicy.setHeightForWidth(self.dataTableSQL.sizePolicy().hasHeightForWidth())
        self.dataTableSQL.setSizePolicy(sizePolicy)
        self.dataTableSQL.setFrameShape(QFrame.Panel)
        self.dataTableSQL.setFrameShadow(QFrame.Plain)
        self.dataTableSQL.setLineWidth(1)
        self.dataTableSQL.setMidLineWidth(2)
        self.dataTableSQL.setGridStyle(Qt.SolidLine)
        self.dataTableSQL.setSortingEnabled(False)
        self.dataTableSQL.setRowCount(13)
        self.dataTableSQL.setColumnCount(7)
        self.dataTableSQL.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableSQL.horizontalHeader().setHighlightSections(False)
        self.dataTableSQL.horizontalHeader().setProperty("showSortIndicator", False)
        self.dataTableSQL.horizontalHeader().setStretchLastSection(True)
        self.dataTableSQL.verticalHeader().setCascadingSectionResizes(True)
        self.dataTableSQL.verticalHeader().setProperty("showSortIndicator", False)
        self.dataTableSQL.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.dataTableSQL)

        self.horizontalSpacer_12 = QSpacerItem(800, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_info = QLabel(self.tab_2)
        self.label_info.setObjectName(u"label_info")

        self.horizontalLayout_17.addWidget(self.label_info)

        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_17.addItem(self.verticalSpacer_15)

        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBoxSQL = QCheckBox(self.tab_2)
        self.checkBoxSQL.setObjectName(u"checkBoxSQL")
        sizePolicy1.setHeightForWidth(self.checkBoxSQL.sizePolicy().hasHeightForWidth())
        self.checkBoxSQL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.checkBoxSQL)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.lineEditDesdeSQL = QLineEdit(self.tab_2)
        self.lineEditDesdeSQL.setObjectName(u"lineEditDesdeSQL")
        sizePolicy2.setHeightForWidth(self.lineEditDesdeSQL.sizePolicy().hasHeightForWidth())
        self.lineEditDesdeSQL.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.lineEditDesdeSQL)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.lineEditHastaSQL = QLineEdit(self.tab_2)
        self.lineEditHastaSQL.setObjectName(u"lineEditHastaSQL")
        sizePolicy2.setHeightForWidth(self.lineEditHastaSQL.sizePolicy().hasHeightForWidth())
        self.lineEditHastaSQL.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.lineEditHastaSQL)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.labelModel_3 = QLabel(self.tab_2)
        self.labelModel_3.setObjectName(u"labelModel_3")

        self.verticalLayout_9.addWidget(self.labelModel_3)

        self.comboModelSQL = QComboBox(self.tab_2)
        self.comboModelSQL.setObjectName(u"comboModelSQL")
        sizePolicy3.setHeightForWidth(self.comboModelSQL.sizePolicy().hasHeightForWidth())
        self.comboModelSQL.setSizePolicy(sizePolicy3)

        self.verticalLayout_9.addWidget(self.comboModelSQL)

        self.labelStatus_3 = QLabel(self.tab_2)
        self.labelStatus_3.setObjectName(u"labelStatus_3")

        self.verticalLayout_9.addWidget(self.labelStatus_3)

        self.comboStatusSQL = QComboBox(self.tab_2)
        self.comboStatusSQL.setObjectName(u"comboStatusSQL")
        sizePolicy3.setHeightForWidth(self.comboStatusSQL.sizePolicy().hasHeightForWidth())
        self.comboStatusSQL.setSizePolicy(sizePolicy3)

        self.verticalLayout_9.addWidget(self.comboStatusSQL)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushBuscarSQL = QPushButton(self.tab_2)
        self.pushBuscarSQL.setObjectName(u"pushBuscarSQL")
        sizePolicy1.setHeightForWidth(self.pushBuscarSQL.sizePolicy().hasHeightForWidth())
        self.pushBuscarSQL.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.pushBuscarSQL)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.horizontalSpacer_14 = QSpacerItem(160, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_14)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"#tab_3{\n"
"    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
"    border-repeat: no-repeat;\n"
"    border-position: center;\n"
"    border-attachment: fixed;\n"
"    border-size: cover; /* Opcional: ajusta el tama\u00f1o de la imagen para cubrir todo el \u00e1rea */\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.verticalSpacer_7)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSpacer_15 = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_15)

        self.logo = QLabel(self.tab_3)
        self.logo.setObjectName(u"logo")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy7)

        self.verticalLayout_11.addWidget(self.logo)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_13 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_13)

        self.line = QFrame(self.tab_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_10.addItem(self.verticalSpacer_8)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_11.addItem(self.verticalSpacer_3)

        self.event_list = QListWidget(self.tab_3)
        QListWidgetItem(self.event_list)
        QListWidgetItem(self.event_list)
        QListWidgetItem(self.event_list)
        QListWidgetItem(self.event_list)
        self.event_list.setObjectName(u"event_list")

        self.horizontalLayout_11.addWidget(self.event_list)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_26)

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_16.addWidget(self.pushButton)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_27)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_18)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_12.addItem(self.verticalSpacer_4)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8)

        self.client_cb = QComboBox(self.tab_3)
        self.client_cb.addItem("")
        self.client_cb.addItem("")
        self.client_cb.setObjectName(u"client_cb")

        self.verticalLayout_13.addWidget(self.client_cb)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_13.addItem(self.verticalSpacer_10)

        self.msg_edit = QTextEdit(self.tab_3)
        self.msg_edit.setObjectName(u"msg_edit")

        self.horizontalLayout_13.addWidget(self.msg_edit)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_15.addItem(self.verticalSpacer_11)

        self.sendMsg_bt = QPushButton(self.tab_3)
        self.sendMsg_bt.setObjectName(u"sendMsg_bt")

        self.horizontalLayout_15.addWidget(self.sendMsg_bt)

        self.sendAll_cb = QCheckBox(self.tab_3)
        self.sendAll_cb.setObjectName(u"sendAll_cb")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.sendAll_cb.sizePolicy().hasHeightForWidth())
        self.sendAll_cb.setSizePolicy(sizePolicy8)
        self.sendAll_cb.setIconSize(QSize(0, 0))

        self.horizontalLayout_15.addWidget(self.sendAll_cb)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_23)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_24)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_25)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 790, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        #######################################

        self.dataTableSQL.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.comboModelSQL.addItems(models)
        self.comboModelLog.addItems(models)
        self.comboStatusSQL.addItems(opciones)

        self.checkBoxSQL.clicked.connect(self.enablerange)
        self.lineEditDesdeSQL.setEnabled(False)
        self.lineEditHastaSQL.setEnabled(False)

        self.dataTableSQL.removeColumn(self.dataTableSQL.columnCount()-1)






    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REGISTROS CATERPILLAR", None))
        ___qtablewidgetitem = self.dataTableLog.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem1 = self.dataTableLog.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ET05", None));
        ___qtablewidgetitem2 = self.dataTableLog.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ET04", None));
        ___qtablewidgetitem3 = self.dataTableLog.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ET03", None));
        ___qtablewidgetitem4 = self.dataTableLog.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ET02", None));
        ___qtablewidgetitem5 = self.dataTableLog.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ET01", None));
        ___qtablewidgetitem6 = self.dataTableLog.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.checkBoxLog.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Desde : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hasta : ", None))
        self.pushBuscarLog.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.labelModel.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.labelStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.pushBuscarEnLogs.setText(QCoreApplication.translate("MainWindow", u"Buscar en logs", None))
        self.labelDataView.setText(QCoreApplication.translate("MainWindow", u"dwfdfdfdsfffffffffffffffffffffffffff\n"
"ffffffffffffffff\n"
"ffffffffffffffffffffffsdsdsfdsfdsewdewdewdewd\n"
"ew", None))
        self.add2DataBase.setText(QCoreApplication.translate("MainWindow", u"Agregar a Base de Datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Log Data", None))
        ___qtablewidgetitem7 = self.dataTableSQL.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem8 = self.dataTableSQL.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ET05", None));
        ___qtablewidgetitem9 = self.dataTableSQL.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ET04", None));
        ___qtablewidgetitem10 = self.dataTableSQL.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ET03", None));
        ___qtablewidgetitem11 = self.dataTableSQL.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ET02", None));
        ___qtablewidgetitem12 = self.dataTableSQL.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ET01", None));
        ___qtablewidgetitem13 = self.dataTableSQL.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.checkBoxSQL.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Desde : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hasta : ", None))
        self.labelModel_3.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.labelStatus_3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.pushBuscarSQL.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"SQL Data", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Server status", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.logo.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Server event", None))

        __sortingEnabled = self.event_list.isSortingEnabled()
        self.event_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.event_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nueva conexion 192.168.100.10", None));
        ___qlistwidgetitem1 = self.event_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mensaje 192.168.100.10 : Proceso terminado", None));
        ___qlistwidgetitem2 = self.event_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nueva conexion 192.168.100.8", None));
        ___qlistwidgetitem3 = self.event_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Desconexion 192.168.100.10", None));
        self.event_list.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select client", None))
        self.client_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"192.168.100.10", None))
        self.client_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"192.168.100.8", None))

        self.msg_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hola desde el server</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.sendMsg_bt.setText(QCoreApplication.translate("MainWindow", u"Send Mensage", None))
        self.sendAll_cb.setText(QCoreApplication.translate("MainWindow", u"Send all", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Server", None))

    def enablerange(self,state):
        self.lineEditDesdeSQL.setEnabled(state)
        self.lineEditHastaSQL.setEnabled(state)



    # retranslateUi
"""

"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 600)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setStyleSheet("#tab{\n"
                                     "    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
                                     "    border-repeat: no-repeat;\n"
                                     "    border-position: center;\n"
                                     "    border-attachment: fixed;\n"
                                     "    border-size: cover; /* Opcional: ajusta el tamaño de la imagen para cubrir todo el área */\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dataTableLog = QtWidgets.QTableWidget(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTableLog.sizePolicy().hasHeightForWidth())
        self.dataTableLog.setSizePolicy(sizePolicy)
        self.dataTableLog.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.dataTableLog.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.dataTableLog.setLineWidth(1)
        self.dataTableLog.setMidLineWidth(2)
        self.dataTableLog.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.dataTableLog.setRowCount(13)
        self.dataTableLog.setColumnCount(7)
        self.dataTableLog.setObjectName("dataTableLog")
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableLog.setHorizontalHeaderItem(6, item)
        self.dataTableLog.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableLog.horizontalHeader().setHighlightSections(False)
        self.dataTableLog.horizontalHeader().setSortIndicatorShown(False)
        self.dataTableLog.horizontalHeader().setStretchLastSection(True)
        self.dataTableLog.verticalHeader().setCascadingSectionResizes(True)
        self.dataTableLog.verticalHeader().setSortIndicatorShown(False)
        self.dataTableLog.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.dataTableLog)
        spacerItem3 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxLog = QtWidgets.QCheckBox(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxLog.sizePolicy().hasHeightForWidth())
        self.checkBoxLog.setSizePolicy(sizePolicy)
        self.checkBoxLog.setText("")
        self.checkBoxLog.setObjectName("checkBoxLog")
        self.horizontalLayout_2.addWidget(self.checkBoxLog)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditDesdeLog = QtWidgets.QLineEdit(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDesdeLog.sizePolicy().hasHeightForWidth())
        self.lineEditDesdeLog.setSizePolicy(sizePolicy)
        self.lineEditDesdeLog.setObjectName("lineEditDesdeLog")
        self.verticalLayout_2.addWidget(self.lineEditDesdeLog)
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEditHastaLog = QtWidgets.QLineEdit(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHastaLog.sizePolicy().hasHeightForWidth())
        self.lineEditHastaLog.setSizePolicy(sizePolicy)
        self.lineEditHastaLog.setObjectName("lineEditHastaLog")
        self.verticalLayout_2.addWidget(self.lineEditHastaLog)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushBuscarLog = QtWidgets.QPushButton(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBuscarLog.sizePolicy().hasHeightForWidth())
        self.pushBuscarLog.setSizePolicy(sizePolicy)
        self.pushBuscarLog.setObjectName("pushBuscarLog")
        self.verticalLayout.addWidget(self.pushBuscarLog)
        self.labelModel = QtWidgets.QLabel(parent=self.tab)
        self.labelModel.setObjectName("labelModel")
        self.verticalLayout.addWidget(self.labelModel)
        self.comboModelLog = QtWidgets.QComboBox(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboModelLog.sizePolicy().hasHeightForWidth())
        self.comboModelLog.setSizePolicy(sizePolicy)
        self.comboModelLog.setObjectName("comboModelLog")
        self.verticalLayout.addWidget(self.comboModelLog)
        self.labelStatus = QtWidgets.QLabel(parent=self.tab)
        self.labelStatus.setObjectName("labelStatus")
        self.verticalLayout.addWidget(self.labelStatus)
        self.comboStatusLog = QtWidgets.QComboBox(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboStatusLog.sizePolicy().hasHeightForWidth())
        self.comboStatusLog.setSizePolicy(sizePolicy)
        self.comboStatusLog.setObjectName("comboStatusLog")
        self.verticalLayout.addWidget(self.comboStatusLog)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushBuscarEnLogs = QtWidgets.QPushButton(parent=self.tab)
        self.pushBuscarEnLogs.setObjectName("pushBuscarEnLogs")
        self.horizontalLayout_3.addWidget(self.pushBuscarEnLogs)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -17, 232, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelDataView = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDataView.sizePolicy().hasHeightForWidth())
        self.labelDataView.setSizePolicy(sizePolicy)
        self.labelDataView.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.labelDataView.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.labelDataView.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelDataView.setScaledContents(False)
        self.labelDataView.setWordWrap(True)
        self.labelDataView.setObjectName("labelDataView")
        self.verticalLayout_6.addWidget(self.labelDataView)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add2DataBase = QtWidgets.QPushButton(parent=self.tab)
        self.add2DataBase.setObjectName("add2DataBase")
        self.horizontalLayout_4.addWidget(self.add2DataBase)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem9)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("#tab_2{\n"
                                 "    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
                                 "    border-repeat: no-repeat;\n"
                                 "    border-position: center;\n"
                                 "    border-attachment: fixed;\n"
                                 "    border-size: cover; /* Opcional: ajusta el tamaño de la imagen para cubrir todo el área */\n"
                                 "}")
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 0, 2, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.dataTableSQL = QtWidgets.QTableWidget(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTableSQL.sizePolicy().hasHeightForWidth())
        self.dataTableSQL.setSizePolicy(sizePolicy)
        self.dataTableSQL.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.dataTableSQL.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.dataTableSQL.setLineWidth(1)
        self.dataTableSQL.setMidLineWidth(2)
        self.dataTableSQL.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.dataTableSQL.setRowCount(13)
        self.dataTableSQL.setColumnCount(7)
        self.dataTableSQL.setObjectName("dataTableSQL")
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTableSQL.setHorizontalHeaderItem(6, item)
        self.dataTableSQL.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTableSQL.horizontalHeader().setHighlightSections(False)
        self.dataTableSQL.horizontalHeader().setSortIndicatorShown(False)
        self.dataTableSQL.horizontalHeader().setStretchLastSection(True)
        self.dataTableSQL.verticalHeader().setCascadingSectionResizes(True)
        self.dataTableSQL.verticalHeader().setSortIndicatorShown(False)
        self.dataTableSQL.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.dataTableSQL)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_info = QtWidgets.QLabel(parent=self.tab_2)
        self.label_info.setObjectName("label_info")
        self.horizontalLayout_17.addWidget(self.label_info)
        spacerItem11 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Fixed)
        self.horizontalLayout_17.addItem(spacerItem11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        spacerItem12 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_8.addItem(spacerItem12)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBoxSQL = QtWidgets.QCheckBox(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxSQL.sizePolicy().hasHeightForWidth())
        self.checkBoxSQL.setSizePolicy(sizePolicy)
        self.checkBoxSQL.setText("")
        self.checkBoxSQL.setObjectName("checkBoxSQL")
        self.horizontalLayout_6.addWidget(self.checkBoxSQL)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.lineEditDesdeSQL = QtWidgets.QLineEdit(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDesdeSQL.sizePolicy().hasHeightForWidth())
        self.lineEditDesdeSQL.setSizePolicy(sizePolicy)
        self.lineEditDesdeSQL.setObjectName("lineEditDesdeSQL")
        self.verticalLayout_10.addWidget(self.lineEditDesdeSQL)
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.lineEditHastaSQL = QtWidgets.QLineEdit(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHastaSQL.sizePolicy().hasHeightForWidth())
        self.lineEditHastaSQL.setSizePolicy(sizePolicy)
        self.lineEditHastaSQL.setObjectName("lineEditHastaSQL")
        self.verticalLayout_10.addWidget(self.lineEditHastaSQL)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.labelModel_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.labelModel_3.setObjectName("labelModel_3")
        self.verticalLayout_9.addWidget(self.labelModel_3)
        self.comboModelSQL = QtWidgets.QComboBox(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboModelSQL.sizePolicy().hasHeightForWidth())
        self.comboModelSQL.setSizePolicy(sizePolicy)
        self.comboModelSQL.setObjectName("comboModelSQL")
        self.verticalLayout_9.addWidget(self.comboModelSQL)
        self.labelStatus_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.labelStatus_3.setObjectName("labelStatus_3")
        self.verticalLayout_9.addWidget(self.labelStatus_3)
        self.comboStatusSQL = QtWidgets.QComboBox(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboStatusSQL.sizePolicy().hasHeightForWidth())
        self.comboStatusSQL.setSizePolicy(sizePolicy)
        self.comboStatusSQL.setObjectName("comboStatusSQL")
        self.verticalLayout_9.addWidget(self.comboStatusSQL)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushBuscarSQL = QtWidgets.QPushButton(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBuscarSQL.sizePolicy().hasHeightForWidth())
        self.pushBuscarSQL.setSizePolicy(sizePolicy)
        self.pushBuscarSQL.setObjectName("pushBuscarSQL")
        self.horizontalLayout_7.addWidget(self.pushBuscarSQL)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-5, 0, 67, 47))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.labelDataSQL = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.labelDataSQL.setObjectName("labelDataSQL")
        self.verticalLayout_16.addWidget(self.labelDataSQL)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_18.addWidget(self.scrollArea)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pb_getInfoSQL = QtWidgets.QPushButton(parent=self.tab_2)
        self.pb_getInfoSQL.setObjectName("pb_getInfoSQL")
        self.horizontalLayout_19.addWidget(self.pb_getInfoSQL)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem16)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_9.addItem(spacerItem18)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("#tab_3{\n"
                                 "    border-image: url(:/dark_blue/img/CATbgrnd.jpg);\n"
                                 "    border-repeat: no-repeat;\n"
                                 "    border-position: center;\n"
                                 "    border-attachment: fixed;\n"
                                 "    border-size: cover; /* Opcional: ajusta el tamaño de la imagen para cubrir todo el área */\n"
                                 "}")
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem19 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem19)
        self.label_3 = QtWidgets.QLabel(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        spacerItem20 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem20)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem21 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_11.addItem(spacerItem21)
        self.logo = QtWidgets.QLabel(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.verticalLayout_11.addWidget(self.logo)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_14.addLayout(self.horizontalLayout_8)
        spacerItem22 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_14.addItem(spacerItem22)
        self.line = QtWidgets.QFrame(parent=self.tab_3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_14.addWidget(self.line)
        spacerItem23 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_14.addItem(spacerItem23)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem24)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Fixed)
        self.horizontalLayout_10.addItem(spacerItem25)
        self.label_4 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem27)
        self.event_list = QtWidgets.QListWidget(parent=self.tab_3)
        self.event_list.setObjectName("event_list")
        item = QtWidgets.QListWidgetItem()
        self.event_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.event_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.event_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.event_list.addItem(item)
        self.horizontalLayout_11.addWidget(self.event_list)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem28)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem29)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_16.addWidget(self.pushButton)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem30)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem31)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem32)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem33)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem34)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Fixed)
        self.horizontalLayout_12.addItem(spacerItem35)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.client_cb = QtWidgets.QComboBox(parent=self.tab_3)
        self.client_cb.setObjectName("client_cb")
        self.client_cb.addItem("")
        self.client_cb.addItem("")
        self.verticalLayout_13.addWidget(self.client_cb)
        self.horizontalLayout_12.addLayout(self.verticalLayout_13)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem36)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout_13.addItem(spacerItem37)
        self.msg_edit = QtWidgets.QTextEdit(parent=self.tab_3)
        self.msg_edit.setObjectName("msg_edit")
        self.horizontalLayout_13.addWidget(self.msg_edit)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem38)
        self.verticalLayout_12.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout_15.addItem(spacerItem39)
        self.sendMsg_bt = QtWidgets.QPushButton(parent=self.tab_3)
        self.sendMsg_bt.setObjectName("sendMsg_bt")
        self.horizontalLayout_15.addWidget(self.sendMsg_bt)
        self.sendAll_cb = QtWidgets.QCheckBox(parent=self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendAll_cb.sizePolicy().hasHeightForWidth())
        self.sendAll_cb.setSizePolicy(sizePolicy)
        self.sendAll_cb.setIconSize(QtCore.QSize(0, 0))
        self.sendAll_cb.setObjectName("sendAll_cb")
        self.horizontalLayout_15.addWidget(self.sendAll_cb)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem40)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem41)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_12.addItem(spacerItem42)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem43)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ############################################

        self.dataTableSQL.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.comboModelSQL.addItems(models)
        self.comboModelLog.addItems(models)
        self.comboStatusSQL.addItems(opciones)

        self.checkBoxSQL.clicked.connect(self.enablerange)
        self.lineEditDesdeSQL.setEnabled(False)
        self.lineEditHastaSQL.setEnabled(False)

        self.dataTableSQL.removeColumn(self.dataTableSQL.columnCount() - 1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "REGISTROS CATERPILLAR"))
        self.dataTableLog.setSortingEnabled(False)
        item = self.dataTableLog.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Number"))
        item = self.dataTableLog.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ET05"))
        item = self.dataTableLog.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ET04"))
        item = self.dataTableLog.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ET03"))
        item = self.dataTableLog.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ET02"))
        item = self.dataTableLog.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ET01"))
        item = self.dataTableLog.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Desde : "))
        self.label_2.setText(_translate("MainWindow", "Hasta : "))
        self.pushBuscarLog.setText(_translate("MainWindow", "Buscar"))
        self.labelModel.setText(_translate("MainWindow", "Modelo"))
        self.labelStatus.setText(_translate("MainWindow", "Status"))
        self.pushBuscarEnLogs.setText(_translate("MainWindow", "Buscar en logs"))
        self.labelDataView.setText(_translate("MainWindow", "dwfdfdfdsfffffffffffffffffffffffffff\n"
                                                            "ffffffffffffffff\n"
                                                            "ffffffffffffffffffffffsdsdsfdsfdsewdewdewdewd\n"
                                                            "ew"))
        self.add2DataBase.setText(_translate("MainWindow", "Agregar a Base de Datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Log Data"))
        self.dataTableSQL.setSortingEnabled(False)
        item = self.dataTableSQL.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Number"))
        item = self.dataTableSQL.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ET05"))
        item = self.dataTableSQL.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ET04"))
        item = self.dataTableSQL.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ET03"))
        item = self.dataTableSQL.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ET02"))
        item = self.dataTableSQL.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ET01"))
        item = self.dataTableSQL.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Status"))
        self.label_info.setText(_translate("MainWindow", "Piezas status INCOMPLETO MOD. 2024 en el rango [0,10]"))
        self.label_6.setText(_translate("MainWindow", "Desde : "))
        self.label_7.setText(_translate("MainWindow", "Hasta : "))
        self.labelModel_3.setText(_translate("MainWindow", "Modelo"))
        self.labelStatus_3.setText(_translate("MainWindow", "Status"))
        self.pushBuscarSQL.setText(_translate("MainWindow", "Buscar"))
        self.labelDataSQL.setText(_translate("MainWindow", "TextLabel"))
        self.pb_getInfoSQL.setText(_translate("MainWindow", "Ver datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SQL Data"))
        self.label_3.setText(_translate("MainWindow", "Server status"))
        self.pushButton_2.setText(_translate("MainWindow", "Status"))
        self.label_4.setText(_translate("MainWindow", "Server event"))
        __sortingEnabled = self.event_list.isSortingEnabled()
        self.event_list.setSortingEnabled(False)
        item = self.event_list.item(0)
        item.setText(_translate("MainWindow", "Nueva conexion 192.168.100.10"))
        item = self.event_list.item(1)
        item.setText(_translate("MainWindow", "Mensaje 192.168.100.10 : Proceso terminado"))
        item = self.event_list.item(2)
        item.setText(_translate("MainWindow", "Nueva conexion 192.168.100.8"))
        item = self.event_list.item(3)
        item.setText(_translate("MainWindow", "Desconexion 192.168.100.10"))
        self.event_list.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Clear All"))
        self.label_8.setText(_translate("MainWindow", "Select client"))
        self.client_cb.setItemText(0, _translate("MainWindow", "192.168.100.10"))
        self.client_cb.setItemText(1, _translate("MainWindow", "192.168.100.8"))
        self.msg_edit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hola desde el server</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendMsg_bt.setText(_translate("MainWindow", "Send Mensage"))
        self.sendAll_cb.setText(_translate("MainWindow", "Send all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Server"))

    def enablerange(self, state):
        self.lineEditDesdeSQL.setEnabled(state)
        self.lineEditHastaSQL.setEnabled(state)
"""
