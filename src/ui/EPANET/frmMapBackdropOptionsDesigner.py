# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\EPANET\frmmapBackdropOptionsDesigner.ui'
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

class Ui_frmMapBackdropOptions(object):
    def setupUi(self, frmMapBackdropOptions):
        frmMapBackdropOptions.setObjectName(_fromUtf8("frmMapBackdropOptions"))
        frmMapBackdropOptions.resize(662, 419)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmMapBackdropOptions.setFont(font)
        self.centralWidget = QtGui.QWidget(frmMapBackdropOptions)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fraMapFile = QtGui.QFrame(self.centralWidget)
        self.fraMapFile.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraMapFile.setFrameShadow(QtGui.QFrame.Raised)
        self.fraMapFile.setObjectName(_fromUtf8("fraMapFile"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.fraMapFile)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblMapFile = QtGui.QLabel(self.fraMapFile)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMapFile.setFont(font)
        self.lblMapFile.setObjectName(_fromUtf8("lblMapFile"))
        self.horizontalLayout_2.addWidget(self.lblMapFile)
        self.txtMapFile = QtGui.QLineEdit(self.fraMapFile)
        self.txtMapFile.setObjectName(_fromUtf8("txtMapFile"))
        self.horizontalLayout_2.addWidget(self.txtMapFile)
        self.verticalLayout.addWidget(self.fraMapFile)
        self.gbxMap = QtGui.QGroupBox(self.centralWidget)
        self.gbxMap.setObjectName(_fromUtf8("gbxMap"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.gbxMap)
        self.horizontalLayout_4.setMargin(11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gbxLL = QtGui.QGroupBox(self.gbxMap)
        self.gbxLL.setObjectName(_fromUtf8("gbxLL"))
        self.formLayout = QtGui.QFormLayout(self.gbxLL)
        self.formLayout.setMargin(11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblLLX = QtGui.QLabel(self.gbxLL)
        self.lblLLX.setObjectName(_fromUtf8("lblLLX"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblLLX)
        self.txtLLX = QtGui.QLineEdit(self.gbxLL)
        self.txtLLX.setObjectName(_fromUtf8("txtLLX"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtLLX)
        self.lblLLY = QtGui.QLabel(self.gbxLL)
        self.lblLLY.setObjectName(_fromUtf8("lblLLY"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblLLY)
        self.txtLLY = QtGui.QLineEdit(self.gbxLL)
        self.txtLLY.setObjectName(_fromUtf8("txtLLY"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtLLY)
        self.horizontalLayout_4.addWidget(self.gbxLL)
        self.gbxUR = QtGui.QGroupBox(self.gbxMap)
        self.gbxUR.setObjectName(_fromUtf8("gbxUR"))
        self.formLayout_2 = QtGui.QFormLayout(self.gbxUR)
        self.formLayout_2.setMargin(11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblURX = QtGui.QLabel(self.gbxUR)
        self.lblURX.setObjectName(_fromUtf8("lblURX"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblURX)
        self.txtURX = QtGui.QLineEdit(self.gbxUR)
        self.txtURX.setObjectName(_fromUtf8("txtURX"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtURX)
        self.lblURY = QtGui.QLabel(self.gbxUR)
        self.lblURY.setObjectName(_fromUtf8("lblURY"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblURY)
        self.txtURY = QtGui.QLineEdit(self.gbxUR)
        self.txtURY.setObjectName(_fromUtf8("txtURY"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtURY)
        self.horizontalLayout_4.addWidget(self.gbxUR)
        self.verticalLayout.addWidget(self.gbxMap)
        self.fraMapUnits = QtGui.QFrame(self.centralWidget)
        self.fraMapUnits.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraMapUnits.setFrameShadow(QtGui.QFrame.Raised)
        self.fraMapUnits.setObjectName(_fromUtf8("fraMapUnits"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.fraMapUnits)
        self.horizontalLayout_5.setMargin(11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblMapUnits = QtGui.QLabel(self.fraMapUnits)
        self.lblMapUnits.setObjectName(_fromUtf8("lblMapUnits"))
        self.horizontalLayout_5.addWidget(self.lblMapUnits)
        self.cboMapUnits = QtGui.QComboBox(self.fraMapUnits)
        self.cboMapUnits.setObjectName(_fromUtf8("cboMapUnits"))
        self.horizontalLayout_5.addWidget(self.cboMapUnits)
        spacerItem = QtGui.QSpacerItem(484, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addWidget(self.fraMapUnits)
        self.fraBackdrop = QtGui.QFrame(self.centralWidget)
        self.fraBackdrop.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraBackdrop.setFrameShadow(QtGui.QFrame.Raised)
        self.fraBackdrop.setObjectName(_fromUtf8("fraBackdrop"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.fraBackdrop)
        self.horizontalLayout_6.setMargin(11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lblBackdrop = QtGui.QLabel(self.fraBackdrop)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblBackdrop.setFont(font)
        self.lblBackdrop.setObjectName(_fromUtf8("lblBackdrop"))
        self.horizontalLayout_6.addWidget(self.lblBackdrop)
        self.txtBackdropFile = QtGui.QLineEdit(self.fraBackdrop)
        self.txtBackdropFile.setObjectName(_fromUtf8("txtBackdropFile"))
        self.horizontalLayout_6.addWidget(self.txtBackdropFile)
        self.verticalLayout.addWidget(self.fraBackdrop)
        self.gbxBackdrop = QtGui.QGroupBox(self.centralWidget)
        self.gbxBackdrop.setObjectName(_fromUtf8("gbxBackdrop"))
        self.gridLayout = QtGui.QGridLayout(self.gbxBackdrop)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txtBackdropY = QtGui.QLineEdit(self.gbxBackdrop)
        self.txtBackdropY.setObjectName(_fromUtf8("txtBackdropY"))
        self.gridLayout.addWidget(self.txtBackdropY, 1, 3, 1, 1)
        self.lblX = QtGui.QLabel(self.gbxBackdrop)
        self.lblX.setObjectName(_fromUtf8("lblX"))
        self.gridLayout.addWidget(self.lblX, 1, 0, 1, 1)
        self.txtBackdropX = QtGui.QLineEdit(self.gbxBackdrop)
        self.txtBackdropX.setObjectName(_fromUtf8("txtBackdropX"))
        self.gridLayout.addWidget(self.txtBackdropX, 1, 1, 1, 1)
        self.lblY = QtGui.QLabel(self.gbxBackdrop)
        self.lblY.setObjectName(_fromUtf8("lblY"))
        self.gridLayout.addWidget(self.lblY, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.gbxBackdrop)
        self.fraOKCancel = QtGui.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtGui.QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cmdOK = QtGui.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtGui.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmMapBackdropOptions.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmMapBackdropOptions)
        QtCore.QMetaObject.connectSlotsByName(frmMapBackdropOptions)

    def retranslateUi(self, frmMapBackdropOptions):
        frmMapBackdropOptions.setWindowTitle(_translate("frmMapBackdropOptions", "EPANET Map/Backdrop Options", None))
        self.lblMapFile.setText(_translate("frmMapBackdropOptions", "Map File Name", None))
        self.gbxMap.setTitle(_translate("frmMapBackdropOptions", "Map Dimensions", None))
        self.gbxLL.setTitle(_translate("frmMapBackdropOptions", "Lower Left", None))
        self.lblLLX.setText(_translate("frmMapBackdropOptions", "X-Coordinate", None))
        self.lblLLY.setText(_translate("frmMapBackdropOptions", "Y-Coordinate", None))
        self.gbxUR.setTitle(_translate("frmMapBackdropOptions", "Upper Right", None))
        self.lblURX.setText(_translate("frmMapBackdropOptions", "X-Coordinate", None))
        self.lblURY.setText(_translate("frmMapBackdropOptions", "Y-Coordinate", None))
        self.lblMapUnits.setText(_translate("frmMapBackdropOptions", "Map Units", None))
        self.lblBackdrop.setText(_translate("frmMapBackdropOptions", "Backdrop File Name", None))
        self.gbxBackdrop.setTitle(_translate("frmMapBackdropOptions", "Backdrop Offsets", None))
        self.lblX.setText(_translate("frmMapBackdropOptions", "X", None))
        self.lblY.setText(_translate("frmMapBackdropOptions", "Y", None))
        self.cmdOK.setText(_translate("frmMapBackdropOptions", "OK", None))
        self.cmdCancel.setText(_translate("frmMapBackdropOptions", "Cancel", None))

