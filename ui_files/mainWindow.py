# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QAbstractItemView,
    QWidget)

models=['MOD. 2021','MOD. 2024']
opciones= ['TODO','COMPLETO','INCOMPLETO']
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 600)
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

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 250, 69))
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

        self.horizontalSpacer_4 = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
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

        self.dataTableSQL.removeColumn(self.dataTableSQL.columnCount() - 1)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"BASE DE DATOS CATERPILLAR", None))
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

    def enablerange(self,state):
        self.lineEditDesdeSQL.setEnabled(state)
        self.lineEditHastaSQL.setEnabled(state)
    # retranslateUi

