# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_profview.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from pyqtgraph.opengl import GLViewWidget

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
        self.profileview = GLViewWidget(self.centralwidget)
        self.profileview.setObjectName(u"profileview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profileview.sizePolicy().hasHeightForWidth())
        self.profileview.setSizePolicy(sizePolicy1)
        self.profileview.setMinimumSize(QSize(525, 580))
        self.profileview.setMaximumSize(QSize(100000, 100000))
        self.profileview.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.profileview, 0, 0, 1, 1)


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

        self.b_SaveIms = QPushButton(self.centralwidget)
        self.b_SaveIms.setObjectName(u"b_SaveIms")
        sizePolicy2.setHeightForWidth(self.b_SaveIms.sizePolicy().hasHeightForWidth())
        self.b_SaveIms.setSizePolicy(sizePolicy2)
        self.b_SaveIms.setMinimumSize(QSize(150, 50))
        self.b_SaveIms.setMaximumSize(QSize(150, 50))

        self.verticalLayout.addWidget(self.b_SaveIms)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(220, 150))
        self.groupBox.setMaximumSize(QSize(220, 150))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.c_showlabels = QCheckBox(self.groupBox)
        self.c_showlabels.setObjectName(u"c_showlabels")
        sizePolicy2.setHeightForWidth(self.c_showlabels.sizePolicy().hasHeightForWidth())
        self.c_showlabels.setSizePolicy(sizePolicy2)
        self.c_showlabels.setMinimumSize(QSize(170, 20))
        self.c_showlabels.setMaximumSize(QSize(170, 20))
        self.c_showlabels.setChecked(False)

        self.verticalLayout_2.addWidget(self.c_showlabels)

        self.c_showrangecircle = QCheckBox(self.groupBox)
        self.c_showrangecircle.setObjectName(u"c_showrangecircle")
        sizePolicy2.setHeightForWidth(self.c_showrangecircle.sizePolicy().hasHeightForWidth())
        self.c_showrangecircle.setSizePolicy(sizePolicy2)
        self.c_showrangecircle.setMinimumSize(QSize(170, 20))
        self.c_showrangecircle.setMaximumSize(QSize(170, 20))
        self.c_showrangecircle.setChecked(True)

        self.verticalLayout_2.addWidget(self.c_showrangecircle)

        self.c_showrangelabel = QCheckBox(self.groupBox)
        self.c_showrangelabel.setObjectName(u"c_showrangelabel")
        sizePolicy2.setHeightForWidth(self.c_showrangelabel.sizePolicy().hasHeightForWidth())
        self.c_showrangelabel.setSizePolicy(sizePolicy2)
        self.c_showrangelabel.setMinimumSize(QSize(170, 20))
        self.c_showrangelabel.setMaximumSize(QSize(170, 20))
        self.c_showrangelabel.setChecked(True)

        self.verticalLayout_2.addWidget(self.c_showrangelabel)

        self.c_showgrid = QCheckBox(self.groupBox)
        self.c_showgrid.setObjectName(u"c_showgrid")
        sizePolicy2.setHeightForWidth(self.c_showgrid.sizePolicy().hasHeightForWidth())
        self.c_showgrid.setSizePolicy(sizePolicy2)
        self.c_showgrid.setMinimumSize(QSize(170, 20))
        self.c_showgrid.setMaximumSize(QSize(170, 20))
        self.c_showgrid.setChecked(True)

        self.verticalLayout_2.addWidget(self.c_showgrid)

        self.c_showbottom = QCheckBox(self.groupBox)
        self.c_showbottom.setObjectName(u"c_showbottom")
        sizePolicy2.setHeightForWidth(self.c_showbottom.sizePolicy().hasHeightForWidth())
        self.c_showbottom.setSizePolicy(sizePolicy2)
        self.c_showbottom.setMinimumSize(QSize(170, 20))
        self.c_showbottom.setMaximumSize(QSize(170, 20))
        self.c_showbottom.setChecked(True)

        self.verticalLayout_2.addWidget(self.c_showbottom)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.b_bwd = QPushButton(self.centralwidget)
        self.b_bwd.setObjectName(u"b_bwd")
        sizePolicy2.setHeightForWidth(self.b_bwd.sizePolicy().hasHeightForWidth())
        self.b_bwd.setSizePolicy(sizePolicy2)
        self.b_bwd.setMinimumSize(QSize(50, 50))
        self.b_bwd.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(36)
        self.b_bwd.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b_bwd)

        self.b_fwd = QPushButton(self.centralwidget)
        self.b_fwd.setObjectName(u"b_fwd")
        sizePolicy2.setHeightForWidth(self.b_fwd.sizePolicy().hasHeightForWidth())
        self.b_fwd.setSizePolicy(sizePolicy2)
        self.b_fwd.setMinimumSize(QSize(50, 50))
        self.b_fwd.setMaximumSize(QSize(50, 50))
        self.b_fwd.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b_fwd)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.b_top = QPushButton(self.centralwidget)
        self.b_top.setObjectName(u"b_top")
        sizePolicy2.setHeightForWidth(self.b_top.sizePolicy().hasHeightForWidth())
        self.b_top.setSizePolicy(sizePolicy2)
        self.b_top.setMinimumSize(QSize(50, 50))
        self.b_top.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.b_top)

        self.b_se = QPushButton(self.centralwidget)
        self.b_se.setObjectName(u"b_se")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.b_se.sizePolicy().hasHeightForWidth())
        self.b_se.setSizePolicy(sizePolicy3)
        self.b_se.setMinimumSize(QSize(50, 50))
        self.b_se.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.b_se)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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
        self.l_legendtop_p = QLineEdit(self.centralwidget)
        self.l_legendtop_p.setObjectName(u"l_legendtop_p")
        sizePolicy2.setHeightForWidth(self.l_legendtop_p.sizePolicy().hasHeightForWidth())
        self.l_legendtop_p.setSizePolicy(sizePolicy2)
        self.l_legendtop_p.setMinimumSize(QSize(220, 20))
        self.l_legendtop_p.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_5.addWidget(self.l_legendtop_p)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


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
        self.b_SaveIms.setText(QCoreApplication.translate("MainWindow", u"Save all images", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Show on map", None))
        self.c_showlabels.setText(QCoreApplication.translate("MainWindow", u"Current vector labels", None))
        self.c_showrangecircle.setText(QCoreApplication.translate("MainWindow", u"Range circle", None))
        self.c_showrangelabel.setText(QCoreApplication.translate("MainWindow", u"Range label", None))
        self.c_showgrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.c_showbottom.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.b_bwd.setText(QCoreApplication.translate("MainWindow", u"bwd", None))
        self.b_fwd.setText(QCoreApplication.translate("MainWindow", u"fwd", None))
        self.b_top.setText("")
        self.b_se.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"This will be added to image legend:", None))
    # retranslateUi

