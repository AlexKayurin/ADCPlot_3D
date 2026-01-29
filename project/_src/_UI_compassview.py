# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_compassview.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

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
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_compass = QGridLayout()
        self.gridLayout_compass.setObjectName(u"gridLayout_compass")
        self.gridLayout_compass.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_compass.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_2.addLayout(self.gridLayout_compass)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lab_0 = QLabel(self.centralwidget)
        self.lab_0.setObjectName(u"lab_0")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_0.sizePolicy().hasHeightForWidth())
        self.lab_0.setSizePolicy(sizePolicy)
        self.lab_0.setMinimumSize(QSize(200, 20))
        self.lab_0.setMaximumSize(QSize(200, 20))
        self.lab_0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lab_0, 2, 0, 1, 1)

        self.lab_4 = QLabel(self.centralwidget)
        self.lab_4.setObjectName(u"lab_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lab_4.sizePolicy().hasHeightForWidth())
        self.lab_4.setSizePolicy(sizePolicy1)
        self.lab_4.setMinimumSize(QSize(0, 20))
        self.lab_4.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.lab_4, 14, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 0, 1, 1)

        self.b_SaveIm = QPushButton(self.centralwidget)
        self.b_SaveIm.setObjectName(u"b_SaveIm")
        self.b_SaveIm.setMinimumSize(QSize(150, 50))
        self.b_SaveIm.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.b_SaveIm, 0, 0, 1, 1)

        self.l_imheight = QLineEdit(self.centralwidget)
        self.l_imheight.setObjectName(u"l_imheight")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_imheight.sizePolicy().hasHeightForWidth())
        self.l_imheight.setSizePolicy(sizePolicy2)
        self.l_imheight.setMinimumSize(QSize(100, 20))
        self.l_imheight.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.l_imheight, 15, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.b_bwd = QPushButton(self.centralwidget)
        self.b_bwd.setObjectName(u"b_bwd")
        self.b_bwd.setMinimumSize(QSize(50, 50))
        self.b_bwd.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(36)
        self.b_bwd.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b_bwd)

        self.b_cnt = QPushButton(self.centralwidget)
        self.b_cnt.setObjectName(u"b_cnt")
        self.b_cnt.setMinimumSize(QSize(50, 50))
        self.b_cnt.setMaximumSize(QSize(50, 50))
        font2 = QFont()
        font2.setPointSize(36)
        font2.setBold(True)
        self.b_cnt.setFont(font2)

        self.horizontalLayout_3.addWidget(self.b_cnt)

        self.b_fwd = QPushButton(self.centralwidget)
        self.b_fwd.setObjectName(u"b_fwd")
        self.b_fwd.setMinimumSize(QSize(50, 50))
        self.b_fwd.setMaximumSize(QSize(50, 50))
        self.b_fwd.setFont(font1)

        self.horizontalLayout_3.addWidget(self.b_fwd)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.l_scale = QLineEdit(self.centralwidget)
        self.l_scale.setObjectName(u"l_scale")
        sizePolicy2.setHeightForWidth(self.l_scale.sizePolicy().hasHeightForWidth())
        self.l_scale.setSizePolicy(sizePolicy2)
        self.l_scale.setMinimumSize(QSize(70, 20))
        self.l_scale.setMaximumSize(QSize(70, 20))

        self.horizontalLayout_4.addWidget(self.l_scale)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.c_showlegend = QCheckBox(self.centralwidget)
        self.c_showlegend.setObjectName(u"c_showlegend")
        self.c_showlegend.setMinimumSize(QSize(200, 20))
        self.c_showlegend.setMaximumSize(QSize(200, 20))
        self.c_showlegend.setChecked(True)

        self.gridLayout.addWidget(self.c_showlegend, 8, 0, 1, 1)

        self.l_imwidth = QLineEdit(self.centralwidget)
        self.l_imwidth.setObjectName(u"l_imwidth")
        sizePolicy2.setHeightForWidth(self.l_imwidth.sizePolicy().hasHeightForWidth())
        self.l_imwidth.setSizePolicy(sizePolicy2)
        self.l_imwidth.setMinimumSize(QSize(100, 20))
        self.l_imwidth.setMaximumSize(QSize(100, 20))

        self.gridLayout.addWidget(self.l_imwidth, 16, 0, 1, 1)

        self.b_SaveIms = QPushButton(self.centralwidget)
        self.b_SaveIms.setObjectName(u"b_SaveIms")
        self.b_SaveIms.setMinimumSize(QSize(150, 50))
        self.b_SaveIms.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.b_SaveIms, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.l_legendtop_c = QLineEdit(self.centralwidget)
        self.l_legendtop_c.setObjectName(u"l_legendtop_c")
        sizePolicy1.setHeightForWidth(self.l_legendtop_c.sizePolicy().hasHeightForWidth())
        self.l_legendtop_c.setSizePolicy(sizePolicy1)
        self.l_legendtop_c.setMinimumSize(QSize(220, 20))
        self.l_legendtop_c.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_6.addWidget(self.l_legendtop_c)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_6, 12, 0, 1, 1)

        self.c_showbt = QCheckBox(self.centralwidget)
        self.c_showbt.setObjectName(u"c_showbt")
        self.c_showbt.setMinimumSize(QSize(200, 20))
        self.c_showbt.setMaximumSize(QSize(200, 20))
        self.c_showbt.setChecked(True)

        self.gridLayout.addWidget(self.c_showbt, 9, 0, 1, 1)

        self.lab_1 = QLabel(self.centralwidget)
        self.lab_1.setObjectName(u"lab_1")
        sizePolicy1.setHeightForWidth(self.lab_1.sizePolicy().hasHeightForWidth())
        self.lab_1.setSizePolicy(sizePolicy1)
        self.lab_1.setMinimumSize(QSize(200, 20))
        self.lab_1.setMaximumSize(QSize(200, 20))
        self.lab_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lab_1, 6, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_2 = QLabel(self.centralwidget)
        self.lab_2.setObjectName(u"lab_2")
        sizePolicy1.setHeightForWidth(self.lab_2.sizePolicy().hasHeightForWidth())
        self.lab_2.setSizePolicy(sizePolicy1)
        self.lab_2.setMinimumSize(QSize(220, 20))
        self.lab_2.setMaximumSize(QSize(220, 20))

        self.horizontalLayout_5.addWidget(self.lab_2)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_5, 11, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.l_mindepth = QLineEdit(self.centralwidget)
        self.l_mindepth.setObjectName(u"l_mindepth")
        sizePolicy2.setHeightForWidth(self.l_mindepth.sizePolicy().hasHeightForWidth())
        self.l_mindepth.setSizePolicy(sizePolicy2)
        self.l_mindepth.setMinimumSize(QSize(70, 20))
        self.l_mindepth.setMaximumSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.l_mindepth)

        self.l_3 = QLabel(self.centralwidget)
        self.l_3.setObjectName(u"l_3")
        sizePolicy1.setHeightForWidth(self.l_3.sizePolicy().hasHeightForWidth())
        self.l_3.setSizePolicy(sizePolicy1)
        self.l_3.setMinimumSize(QSize(30, 20))
        self.l_3.setMaximumSize(QSize(30, 20))
        self.l_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.l_3)

        self.l_maxdepth = QLineEdit(self.centralwidget)
        self.l_maxdepth.setObjectName(u"l_maxdepth")
        sizePolicy2.setHeightForWidth(self.l_maxdepth.sizePolicy().hasHeightForWidth())
        self.l_maxdepth.setSizePolicy(sizePolicy2)
        self.l_maxdepth.setMinimumSize(QSize(70, 20))
        self.l_maxdepth.setMaximumSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.l_maxdepth)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        self.b_resize = QPushButton(self.centralwidget)
        self.b_resize.setObjectName(u"b_resize")
        self.b_resize.setMinimumSize(QSize(100, 30))
        self.b_resize.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.b_resize, 17, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

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
        self.lab_0.setText(QCoreApplication.translate("MainWindow", u"Vector scale:", None))
        self.lab_4.setText(QCoreApplication.translate("MainWindow", u"Set image size:", None))
        self.b_SaveIm.setText(QCoreApplication.translate("MainWindow", u"Save this image", None))
        self.b_bwd.setText(QCoreApplication.translate("MainWindow", u"BWD", None))
        self.b_cnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b_fwd.setText(QCoreApplication.translate("MainWindow", u"FWD", None))
        self.l_scale.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.c_showlegend.setText(QCoreApplication.translate("MainWindow", u"Show ensemble data", None))
        self.b_SaveIms.setText(QCoreApplication.translate("MainWindow", u"Save all images", None))
        self.c_showbt.setText(QCoreApplication.translate("MainWindow", u"Show bottom track", None))
        self.lab_1.setText(QCoreApplication.translate("MainWindow", u"View depth range:", None))
        self.lab_2.setText(QCoreApplication.translate("MainWindow", u"This will be added to image legend:", None))
        self.l_3.setText(QCoreApplication.translate("MainWindow", u" - ", None))
        self.b_resize.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
    # retranslateUi

