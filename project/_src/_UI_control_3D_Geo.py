# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_control_3D_Geo.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QHBoxLayout, QHeaderView, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 901)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        font1 = QFont()
        font1.setPointSize(10)
        self.actionLicense.setFont(font1)
        self.actionakayurin_gmail_com = QAction(MainWindow)
        self.actionakayurin_gmail_com.setObjectName(u"actionakayurin_gmail_com")
        self.actionakayurin_gmail_com.setFont(font1)
        self.actionHow_to_use = QAction(MainWindow)
        self.actionHow_to_use.setObjectName(u"actionHow_to_use")
        self.actionHow_to_use.setFont(font1)
        self.actionver = QAction(MainWindow)
        self.actionver.setObjectName(u"actionver")
        self.actionver.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.c_filenames = QComboBox(self.centralwidget)
        self.c_filenames.setObjectName(u"c_filenames")
        self.c_filenames.setMinimumSize(QSize(300, 20))
        self.c_filenames.setMaximumSize(QSize(300, 20))
        self.c_filenames.setMaxVisibleItems(15)

        self.horizontalLayout.addWidget(self.c_filenames)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_header = QWidget()
        self.tab_header.setObjectName(u"tab_header")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_header = QTextEdit(self.tab_header)
        self.txt_header.setObjectName(u"txt_header")
        self.txt_header.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txt_header)

        self.tabWidget.addTab(self.tab_header, "")
        self.tab_table = QWidget()
        self.tab_table.setObjectName(u"tab_table")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_table)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.t_data = QTableWidget(self.tab_table)
        self.t_data.setObjectName(u"t_data")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(8)
        self.t_data.setFont(font2)
        self.t_data.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.t_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout_3.addWidget(self.t_data)

        self.tabWidget.addTab(self.tab_table, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.b_open = QPushButton(self.centralwidget)
        self.b_open.setObjectName(u"b_open")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_open.sizePolicy().hasHeightForWidth())
        self.b_open.setSizePolicy(sizePolicy)
        self.b_open.setMinimumSize(QSize(130, 40))
        self.b_open.setMaximumSize(QSize(130, 40))
        self.b_open.setFont(font)

        self.verticalLayout.addWidget(self.b_open)

        self.b_exportxl = QPushButton(self.centralwidget)
        self.b_exportxl.setObjectName(u"b_exportxl")
        self.b_exportxl.setMinimumSize(QSize(130, 40))
        self.b_exportxl.setMaximumSize(QSize(130, 40))
        self.b_exportxl.setFont(font)

        self.verticalLayout.addWidget(self.b_exportxl)

        self.b_exportxlall = QPushButton(self.centralwidget)
        self.b_exportxlall.setObjectName(u"b_exportxlall")
        self.b_exportxlall.setMinimumSize(QSize(130, 40))
        self.b_exportxlall.setMaximumSize(QSize(130, 40))

        self.verticalLayout.addWidget(self.b_exportxlall)

        self.b_exportgis = QPushButton(self.centralwidget)
        self.b_exportgis.setObjectName(u"b_exportgis")
        self.b_exportgis.setMinimumSize(QSize(130, 40))
        self.b_exportgis.setMaximumSize(QSize(130, 40))

        self.verticalLayout.addWidget(self.b_exportgis)

        self.c_showprofview = QCheckBox(self.centralwidget)
        self.c_showprofview.setObjectName(u"c_showprofview")
        self.c_showprofview.setMinimumSize(QSize(200, 20))
        self.c_showprofview.setMaximumSize(QSize(200, 20))
        self.c_showprofview.setChecked(True)

        self.verticalLayout.addWidget(self.c_showprofview)

        self.c_showcompview = QCheckBox(self.centralwidget)
        self.c_showcompview.setObjectName(u"c_showcompview")
        self.c_showcompview.setMinimumSize(QSize(200, 20))
        self.c_showcompview.setMaximumSize(QSize(200, 20))
        self.c_showcompview.setChecked(True)

        self.verticalLayout.addWidget(self.c_showcompview)

        self.c_showmapview = QCheckBox(self.centralwidget)
        self.c_showmapview.setObjectName(u"c_showmapview")
        self.c_showmapview.setMinimumSize(QSize(200, 20))
        self.c_showmapview.setMaximumSize(QSize(200, 20))

        self.verticalLayout.addWidget(self.c_showmapview)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1089, 33))
        self.menuRead_here = QMenu(self.menubar)
        self.menuRead_here.setObjectName(u"menuRead_here")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuRead_here.menuAction())
        self.menuRead_here.addAction(self.actionHow_to_use)
        self.menuRead_here.addAction(self.actionLicense)
        self.menuRead_here.addAction(self.actionakayurin_gmail_com)
        self.menuRead_here.addAction(self.actionver)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ADCPlot 3D Geo", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.actionakayurin_gmail_com.setText(QCoreApplication.translate("MainWindow", u"akayurin@gmail.com", None))
        self.actionHow_to_use.setText(QCoreApplication.translate("MainWindow", u"How to use", None))
        self.actionver.setText(QCoreApplication.translate("MainWindow", u"ver. 28-Jan-2026", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_header), QCoreApplication.translate("MainWindow", u"Header", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_table), QCoreApplication.translate("MainWindow", u"Data", None))
        self.b_open.setText(QCoreApplication.translate("MainWindow", u"Open ADCP", None))
        self.b_exportxl.setText(QCoreApplication.translate("MainWindow", u"Export this to Excel", None))
        self.b_exportxlall.setText(QCoreApplication.translate("MainWindow", u"Export all to Excel", None))
        self.b_exportgis.setText(QCoreApplication.translate("MainWindow", u"Export to GIS", None))
        self.c_showprofview.setText(QCoreApplication.translate("MainWindow", u"Show profile view", None))
        self.c_showcompview.setText(QCoreApplication.translate("MainWindow", u"Show compass view", None))
        self.c_showmapview.setText(QCoreApplication.translate("MainWindow", u"Show map view", None))
        self.menuRead_here.setTitle(QCoreApplication.translate("MainWindow", u"Read here", None))
    # retranslateUi

