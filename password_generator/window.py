# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_generator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 120))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_generate_view = QtWidgets.QVBoxLayout()
        self.layout_generate_view.setObjectName("layout_generate_view")
        self.display_password_area = QtWidgets.QLineEdit(self.centralwidget)
        self.display_password_area.setReadOnly(True)
        self.display_password_area.setClearButtonEnabled(False)
        self.display_password_area.setObjectName("display_password_area")
        self.layout_generate_view.addWidget(self.display_password_area)
        self.button_generate = QtWidgets.QPushButton(self.centralwidget)
        self.button_generate.setObjectName("button_generate")
        self.layout_generate_view.addWidget(self.button_generate)
        self.horizontalLayout.addLayout(self.layout_generate_view)
        self.layout_length_selection = QtWidgets.QVBoxLayout()
        self.layout_length_selection.setObjectName("layout_length_selection")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.layout_length_selection.addWidget(self.label)
        self.pass_len_box = QtWidgets.QSpinBox(self.centralwidget)
        self.pass_len_box.setMaximum(74)
        self.pass_len_box.setProperty("value", 16)
        self.pass_len_box.setObjectName("pass_len_box")
        self.layout_length_selection.addWidget(self.pass_len_box)
        self.horizontalLayout.addLayout(self.layout_length_selection)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.menu.addAction(self.action_save)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Password generator"))
        self.button_generate.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.action_save.setText(_translate("MainWindow", "Save password"))
