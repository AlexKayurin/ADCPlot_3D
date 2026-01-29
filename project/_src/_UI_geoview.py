# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_geoview.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 633)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.geoview = PlotWidget(self.centralwidget)
        self.geoview.setObjectName(u"geoview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.geoview.sizePolicy().hasHeightForWidth())
        self.geoview.setSizePolicy(sizePolicy1)
        self.geoview.setMinimumSize(QSize(525, 580))
        self.geoview.setMaximumSize(QSize(100000, 100000))
        self.geoview.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.geoview, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.b_SaveIm = QPushButton(self.centralwidget)
        self.b_SaveIm.setObjectName(u"b_SaveIm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_SaveIm.sizePolicy().hasHeightForWidth())
        self.b_SaveIm.setSizePolicy(sizePolicy2)
        self.b_SaveIm.setMinimumSize(QSize(150, 50))
        self.b_SaveIm.setMaximumSize(QSize(150, 50))

        self.verticalLayout.addWidget(self.b_SaveIm)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(220, 20))
        self.label.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.l_legendtop_g = QLineEdit(self.centralwidget)
        self.l_legendtop_g.setObjectName(u"l_legendtop_g")
        sizePolicy2.setHeightForWidth(self.l_legendtop_g.sizePolicy().hasHeightForWidth())
        self.l_legendtop_g.setSizePolicy(sizePolicy2)
        self.l_legendtop_g.setMinimumSize(QSize(220, 20))
        self.l_legendtop_g.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_5.addWidget(self.l_legendtop_g)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.c_colorcodedepth = QCheckBox(self.centralwidget)
        self.c_colorcodedepth.setObjectName(u"c_colorcodedepth")
        self.c_colorcodedepth.setMinimumSize(QSize(220, 20))
        self.c_colorcodedepth.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_3.addWidget(self.c_colorcodedepth)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(220, 20))
        self.label_2.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.l_scale = QLineEdit(self.centralwidget)
        self.l_scale.setObjectName(u"l_scale")
        self.l_scale.setMinimumSize(QSize(220, 20))
        self.l_scale.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_7.addWidget(self.l_scale)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.sl_bin = QSlider(self.centralwidget)
        self.sl_bin.setObjectName(u"sl_bin")
        self.sl_bin.setMinimumSize(QSize(50, 300))
        self.sl_bin.setMaximumSize(QSize(50, 300))
        self.sl_bin.setMinimum(1)
        self.sl_bin.setPageStep(1)
        self.sl_bin.setValue(1)
        self.sl_bin.setOrientation(Qt.Orientation.Vertical)
        self.sl_bin.setInvertedAppearance(False)
        self.sl_bin.setInvertedControls(False)
        self.sl_bin.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sl_bin.setTickInterval(10)

        self.verticalLayout.addWidget(self.sl_bin)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_SaveIm.setText(QCoreApplication.translate("MainWindow", u"Save this image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"This will be added to image legend:", None))
        self.c_colorcodedepth.setText(QCoreApplication.translate("MainWindow", u"Animate depth", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vector scale:", None))
        self.l_scale.setText(QCoreApplication.translate("MainWindow", u"1", None))
    # retranslateUi

