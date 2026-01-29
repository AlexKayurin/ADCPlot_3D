# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_help.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 727)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"How to use", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The application is intended to visualize and save data obtained from ADCP sensors and stored in Matlab (mat) format in winADCP software. winADCP saves ADCP data in Matlab Level 1 format. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00a0 </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\">The application consists of 4 windows: </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Main control</span> represents two tabs: Header tab, containing data file header, and Data tab, containing ADCP data for loaded file. Multiple files can be loaded and browsed through the window. There are options to export ADCP data in Excel format (either loaded file or all available) and export all the loaded data (multiple files) into single GIS compatible GEOJSON or WKT ASCII file as point with relevant attributes. Combobox is used to navigate through loaded files. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Profile view</span> represents 3D view of single ADCP profile along with its data in numeric format. Mouse wheel is used to n"
                        "avigate through the window. Buttons <span style=\" font-weight:700;\">'BWD'</span>/<span style=\" font-weight:700;\">'FWD'</span> are used to navigate through profiles. View may be set in orthographic or perspective projection by <span style=\" font-weight:700;\">'Ortho'</span>/<span style=\" font-weight:700;\">'Persp'</span> buttons. Current image may be saved in <span style=\" font-weight:700;\">png</span> format by pressing <span style=\" font-weight:700;\">'Save this image'</span> button. <span style=\" font-weight:700;\">'Save all images'</span> button is used to save all the profiles of the loaded file with the same settings. Text entry is used to type text to be plotted on the top of legend of the exported images. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Compass view</span> represents vertical compass view of the current and neighbouring profiles along with relevant metadata (time"
                        "stamp, Lat, Lon). The view is centered on the current profile. Number of visible profiles may be changed by mouse wheel. View limits and vector scale may be set using relevant text entries. Buttons <span style=\" font-weight:700;\">'BWD'</span>/<span style=\" font-weight:700;\">'FWD'</span> are used to navigate through profiles. Current image may be saved in <span style=\" font-weight:700;\">png</span> format by pressing <span style=\" font-weight:700;\">'Save this image'</span> button. <span style=\" font-weight:700;\">'Save all images'</span> button is used to save all the profiles of the loaded file with the same settings. Text entry is used to type text to be plotted on the top of legend of the exported images. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Map view</span> represents geographical view of all the loaded ADCP data. Vector scale may be set using scale text entry. Slider is us"
                        "ed to navigate through bins (depths). <span style=\" font-weight:700;\">'Animate depth'</span> checkbox used to turn on/off background color change with depth. Current image may be saved in <span style=\" font-weight:700;\">png</span> format by pressing <span style=\" font-weight:700;\">'Save this image'</span> button. Text entry is used to type text to be plotted on the top of legend of the exported image. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00a0 </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p></body></html>", None))
    # retranslateUi

