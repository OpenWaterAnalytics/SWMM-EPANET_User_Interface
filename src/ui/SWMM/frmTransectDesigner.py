# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\SWMM\frmTransectDesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmTransect(object):
    def setupUi(self, frmTransect):
        frmTransect.setObjectName(_fromUtf8("frmTransect"))
        frmTransect.resize(546, 503)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmTransect.setFont(font)
        self.centralWidget = QtGui.QWidget(frmTransect)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fraTop = QtGui.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtGui.QFrame.Raised)
        self.fraTop.setObjectName(_fromUtf8("fraTop"))
        self.gridLayout_2 = QtGui.QGridLayout(self.fraTop)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblDescription = QtGui.QLabel(self.fraTop)
        self.lblDescription.setObjectName(_fromUtf8("lblDescription"))
        self.gridLayout_2.addWidget(self.lblDescription, 1, 0, 1, 1)
        self.txtName = QtGui.QLineEdit(self.fraTop)
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.gridLayout_2.addWidget(self.txtName, 0, 2, 1, 1)
        self.lblGroup = QtGui.QLabel(self.fraTop)
        self.lblGroup.setObjectName(_fromUtf8("lblGroup"))
        self.gridLayout_2.addWidget(self.lblGroup, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.txtDescription = QtGui.QLineEdit(self.fraTop)
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.gridLayout_2.addWidget(self.txtDescription, 1, 2, 1, 2)
        self.verticalLayout.addWidget(self.fraTop)
        self.fraMiddle = QtGui.QFrame(self.centralWidget)
        self.fraMiddle.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraMiddle.setFrameShadow(QtGui.QFrame.Raised)
        self.fraMiddle.setObjectName(_fromUtf8("fraMiddle"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.fraMiddle)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tblTransect = QtGui.QTableWidget(self.fraMiddle)
        self.tblTransect.setRowCount(100)
        self.tblTransect.setObjectName(_fromUtf8("tblTransect"))
        self.tblTransect.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        self.tblTransect.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblTransect.setHorizontalHeaderItem(1, item)
        self.tblTransect.horizontalHeader().setCascadingSectionResizes(False)
        self.tblTransect.horizontalHeader().setDefaultSectionSize(100)
        self.tblTransect.horizontalHeader().setStretchLastSection(True)
        self.tblTransect.verticalHeader().setDefaultSectionSize(30)
        self.tblTransect.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.tblTransect)
        self.gbxProperties = QtGui.QGroupBox(self.fraMiddle)
        self.gbxProperties.setObjectName(_fromUtf8("gbxProperties"))
        self.gridLayout = QtGui.QGridLayout(self.gbxProperties)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblElevations = QtGui.QLabel(self.gbxProperties)
        self.lblElevations.setObjectName(_fromUtf8("lblElevations"))
        self.gridLayout.addWidget(self.lblElevations, 9, 0, 1, 1)
        self.lblStations = QtGui.QLabel(self.gbxProperties)
        self.lblStations.setObjectName(_fromUtf8("lblStations"))
        self.gridLayout.addWidget(self.lblStations, 8, 0, 1, 1)
        self.txtLeftSta = QtGui.QLineEdit(self.gbxProperties)
        self.txtLeftSta.setObjectName(_fromUtf8("txtLeftSta"))
        self.gridLayout.addWidget(self.txtLeftSta, 5, 1, 1, 1)
        self.txtRightSta = QtGui.QLineEdit(self.gbxProperties)
        self.txtRightSta.setObjectName(_fromUtf8("txtRightSta"))
        self.gridLayout.addWidget(self.txtRightSta, 6, 1, 1, 1)
        self.lblRight = QtGui.QLabel(self.gbxProperties)
        self.lblRight.setObjectName(_fromUtf8("lblRight"))
        self.gridLayout.addWidget(self.lblRight, 6, 0, 1, 1)
        self.lblLeft = QtGui.QLabel(self.gbxProperties)
        self.lblLeft.setObjectName(_fromUtf8("lblLeft"))
        self.gridLayout.addWidget(self.lblLeft, 5, 0, 1, 1)
        self.lblBankStations = QtGui.QLabel(self.gbxProperties)
        self.lblBankStations.setObjectName(_fromUtf8("lblBankStations"))
        self.gridLayout.addWidget(self.lblBankStations, 4, 0, 1, 1)
        self.lblModifiers = QtGui.QLabel(self.gbxProperties)
        self.lblModifiers.setObjectName(_fromUtf8("lblModifiers"))
        self.gridLayout.addWidget(self.lblModifiers, 7, 0, 1, 1)
        self.lblMeander = QtGui.QLabel(self.gbxProperties)
        self.lblMeander.setObjectName(_fromUtf8("lblMeander"))
        self.gridLayout.addWidget(self.lblMeander, 10, 0, 1, 1)
        self.txtStations = QtGui.QLineEdit(self.gbxProperties)
        self.txtStations.setObjectName(_fromUtf8("txtStations"))
        self.gridLayout.addWidget(self.txtStations, 8, 1, 1, 1)
        self.txtRightBank = QtGui.QLineEdit(self.gbxProperties)
        self.txtRightBank.setObjectName(_fromUtf8("txtRightBank"))
        self.gridLayout.addWidget(self.txtRightBank, 2, 1, 1, 1)
        self.lblRightBank = QtGui.QLabel(self.gbxProperties)
        self.lblRightBank.setObjectName(_fromUtf8("lblRightBank"))
        self.gridLayout.addWidget(self.lblRightBank, 2, 0, 1, 1)
        self.lblLeftBank = QtGui.QLabel(self.gbxProperties)
        self.lblLeftBank.setObjectName(_fromUtf8("lblLeftBank"))
        self.gridLayout.addWidget(self.lblLeftBank, 1, 0, 1, 1)
        self.txtLeftBank = QtGui.QLineEdit(self.gbxProperties)
        self.txtLeftBank.setObjectName(_fromUtf8("txtLeftBank"))
        self.gridLayout.addWidget(self.txtLeftBank, 1, 1, 1, 1)
        self.lblRough = QtGui.QLabel(self.gbxProperties)
        self.lblRough.setObjectName(_fromUtf8("lblRough"))
        self.gridLayout.addWidget(self.lblRough, 0, 0, 1, 1)
        self.txtChannel = QtGui.QLineEdit(self.gbxProperties)
        self.txtChannel.setObjectName(_fromUtf8("txtChannel"))
        self.gridLayout.addWidget(self.txtChannel, 3, 1, 1, 1)
        self.lblChannel = QtGui.QLabel(self.gbxProperties)
        self.lblChannel.setObjectName(_fromUtf8("lblChannel"))
        self.gridLayout.addWidget(self.lblChannel, 3, 0, 1, 1)
        self.txtElevations = QtGui.QLineEdit(self.gbxProperties)
        self.txtElevations.setObjectName(_fromUtf8("txtElevations"))
        self.gridLayout.addWidget(self.txtElevations, 9, 1, 1, 1)
        self.txtMeander = QtGui.QLineEdit(self.gbxProperties)
        self.txtMeander.setObjectName(_fromUtf8("txtMeander"))
        self.gridLayout.addWidget(self.txtMeander, 10, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.gbxProperties)
        self.verticalLayout.addWidget(self.fraMiddle)
        self.fraOKCancel = QtGui.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtGui.QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnView = QtGui.QPushButton(self.fraOKCancel)
        self.btnView.setObjectName(_fromUtf8("btnView"))
        self.horizontalLayout.addWidget(self.btnView)
        spacerItem1 = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cmdOK = QtGui.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtGui.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmTransect.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmTransect)
        QtCore.QMetaObject.connectSlotsByName(frmTransect)

    def retranslateUi(self, frmTransect):
        frmTransect.setWindowTitle(_translate("frmTransect", "SWMM Transect Editor", None))
        self.lblDescription.setText(_translate("frmTransect", "Description", None))
        self.lblGroup.setText(_translate("frmTransect", "Transect Name", None))
        item = self.tblTransect.horizontalHeaderItem(0)
        item.setText(_translate("frmTransect", "Station (ft)", None))
        item = self.tblTransect.horizontalHeaderItem(1)
        item.setText(_translate("frmTransect", "Elevation (ft)", None))
        self.gbxProperties.setTitle(_translate("frmTransect", "Properties", None))
        self.lblElevations.setText(_translate("frmTransect", "  Elevations", None))
        self.lblStations.setText(_translate("frmTransect", "  Stations", None))
        self.lblRight.setText(_translate("frmTransect", "  Right", None))
        self.lblLeft.setText(_translate("frmTransect", "  Left", None))
        self.lblBankStations.setText(_translate("frmTransect", "Bank Stations:", None))
        self.lblModifiers.setText(_translate("frmTransect", "Modifiers:", None))
        self.lblMeander.setText(_translate("frmTransect", "  Meander", None))
        self.lblRightBank.setText(_translate("frmTransect", "  Right Bank", None))
        self.lblLeftBank.setText(_translate("frmTransect", "  Left Bank", None))
        self.lblRough.setText(_translate("frmTransect", "Roughness:", None))
        self.lblChannel.setText(_translate("frmTransect", "  Channel", None))
        self.btnView.setText(_translate("frmTransect", "View...", None))
        self.cmdOK.setText(_translate("frmTransect", "OK", None))
        self.cmdCancel.setText(_translate("frmTransect", "Cancel", None))

