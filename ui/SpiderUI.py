# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpiderUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NjztcSpider(object):
    def setupUi(self, NjztcSpider):
        NjztcSpider.setObjectName("NjztcSpider")
        NjztcSpider.resize(1424, 454)
        NjztcSpider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(NjztcSpider)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Tiplabel = QtWidgets.QLabel(NjztcSpider)
        self.Tiplabel.setEnabled(True)
        self.Tiplabel.setObjectName("Tiplabel")
        self.verticalLayout.addWidget(self.Tiplabel)
        self.SpiderInform = QtWidgets.QTextBrowser(NjztcSpider)
        self.SpiderInform.setObjectName("SpiderInform")
        self.verticalLayout.addWidget(self.SpiderInform)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphButton = QtWidgets.QPushButton(NjztcSpider)
        self.graphButton.setObjectName("graphButton")
        self.horizontalLayout_2.addWidget(self.graphButton)
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.SupplyInform = QtWidgets.QTableView(NjztcSpider)
        self.SupplyInform.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.SupplyInform.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.SupplyInform.setObjectName("SupplyInform")
        self.SupplyInform.horizontalHeader().setVisible(True)
        self.SupplyInform.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.SupplyInform)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.spiderButton = QtWidgets.QPushButton(NjztcSpider)
        self.spiderButton.setObjectName("spiderButton")
        self.horizontalLayout.addWidget(self.spiderButton)
        spacerItem2 = QtWidgets.QSpacerItem(13, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancelButton = QtWidgets.QPushButton(NjztcSpider)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(NjztcSpider)
        self.cancelButton.clicked.connect(NjztcSpider.close)
        QtCore.QMetaObject.connectSlotsByName(NjztcSpider)

    def retranslateUi(self, NjztcSpider):
        _translate = QtCore.QCoreApplication.translate
        NjztcSpider.setWindowTitle(_translate("NjztcSpider", "农机需求信息爬取"))
        self.Tiplabel.setText(_translate("NjztcSpider", "点击爬取可爬取数据"))
        self.graphButton.setText(_translate("NjztcSpider", "查看图表"))
        self.spiderButton.setText(_translate("NjztcSpider", "爬取"))
        self.cancelButton.setText(_translate("NjztcSpider", "取消"))
