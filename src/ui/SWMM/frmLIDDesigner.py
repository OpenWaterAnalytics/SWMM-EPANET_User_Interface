# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\SWMM\frmLIDDesigner.ui'
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

class Ui_frmLID(object):
    def setupUi(self, frmLID):
        frmLID.setObjectName(_fromUtf8("frmLID"))
        frmLID.resize(776, 465)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmLID.setFont(font)
        self.centralWidget = QtGui.QWidget(frmLID)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fraTop = QtGui.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtGui.QFrame.Raised)
        self.fraTop.setObjectName(_fromUtf8("fraTop"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.fraTop)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fraLeft = QtGui.QFrame(self.fraTop)
        self.fraLeft.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraLeft.setFrameShadow(QtGui.QFrame.Raised)
        self.fraLeft.setObjectName(_fromUtf8("fraLeft"))
        self.gridLayout = QtGui.QGridLayout(self.fraLeft)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fraTopLeft = QtGui.QFrame(self.fraLeft)
        self.fraTopLeft.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraTopLeft.setFrameShadow(QtGui.QFrame.Raised)
        self.fraTopLeft.setObjectName(_fromUtf8("fraTopLeft"))
        self.gridLayout_12 = QtGui.QGridLayout(self.fraTopLeft)
        self.gridLayout_12.setMargin(11)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.lblControlName = QtGui.QLabel(self.fraTopLeft)
        self.lblControlName.setObjectName(_fromUtf8("lblControlName"))
        self.gridLayout_12.addWidget(self.lblControlName, 0, 0, 1, 1)
        self.txtName = QtGui.QLineEdit(self.fraTopLeft)
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.gridLayout_12.addWidget(self.txtName, 0, 1, 1, 1)
        self.lblLIDType = QtGui.QLabel(self.fraTopLeft)
        self.lblLIDType.setObjectName(_fromUtf8("lblLIDType"))
        self.gridLayout_12.addWidget(self.lblLIDType, 1, 0, 1, 1)
        self.cboLIDType = QtGui.QComboBox(self.fraTopLeft)
        self.cboLIDType.setObjectName(_fromUtf8("cboLIDType"))
        self.gridLayout_12.addWidget(self.cboLIDType, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.fraTopLeft, 0, 0, 1, 2)
        self.lblImage = QtGui.QLabel(self.fraLeft)
        self.lblImage.setText(_fromUtf8(""))
        self.lblImage.setPixmap(QtGui.QPixmap(_fromUtf8("../swmmimages/1bio.png")))
        self.lblImage.setObjectName(_fromUtf8("lblImage"))
        self.gridLayout.addWidget(self.lblImage, 1, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.fraLeft)
        self.tabLID = QtGui.QTabWidget(self.fraTop)
        self.tabLID.setObjectName(_fromUtf8("tabLID"))
        self.Surface = QtGui.QWidget()
        self.Surface.setObjectName(_fromUtf8("Surface"))
        self.gridLayout_11 = QtGui.QGridLayout(self.Surface)
        self.gridLayout_11.setMargin(11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.fraSurface = QtGui.QFrame(self.Surface)
        self.fraSurface.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraSurface.setFrameShadow(QtGui.QFrame.Raised)
        self.fraSurface.setObjectName(_fromUtf8("fraSurface"))
        self.gridLayout_5 = QtGui.QGridLayout(self.fraSurface)
        self.gridLayout_5.setMargin(11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lblSurface5 = QtGui.QLabel(self.fraSurface)
        self.lblSurface5.setWordWrap(True)
        self.lblSurface5.setObjectName(_fromUtf8("lblSurface5"))
        self.gridLayout_5.addWidget(self.lblSurface5, 4, 0, 1, 1)
        self.txtSurface5 = QtGui.QLineEdit(self.fraSurface)
        self.txtSurface5.setObjectName(_fromUtf8("txtSurface5"))
        self.gridLayout_5.addWidget(self.txtSurface5, 4, 1, 1, 1)
        self.txtSurface4 = QtGui.QLineEdit(self.fraSurface)
        self.txtSurface4.setObjectName(_fromUtf8("txtSurface4"))
        self.gridLayout_5.addWidget(self.txtSurface4, 3, 1, 1, 1)
        self.lblSurface4 = QtGui.QLabel(self.fraSurface)
        self.lblSurface4.setWordWrap(True)
        self.lblSurface4.setObjectName(_fromUtf8("lblSurface4"))
        self.gridLayout_5.addWidget(self.lblSurface4, 3, 0, 1, 1)
        self.txtSurface3 = QtGui.QLineEdit(self.fraSurface)
        self.txtSurface3.setObjectName(_fromUtf8("txtSurface3"))
        self.gridLayout_5.addWidget(self.txtSurface3, 2, 1, 1, 1)
        self.lblSurface3 = QtGui.QLabel(self.fraSurface)
        self.lblSurface3.setWordWrap(True)
        self.lblSurface3.setObjectName(_fromUtf8("lblSurface3"))
        self.gridLayout_5.addWidget(self.lblSurface3, 2, 0, 1, 1)
        self.txtSurface2 = QtGui.QLineEdit(self.fraSurface)
        self.txtSurface2.setObjectName(_fromUtf8("txtSurface2"))
        self.gridLayout_5.addWidget(self.txtSurface2, 1, 1, 1, 1)
        self.lblSurface2 = QtGui.QLabel(self.fraSurface)
        self.lblSurface2.setWordWrap(True)
        self.lblSurface2.setObjectName(_fromUtf8("lblSurface2"))
        self.gridLayout_5.addWidget(self.lblSurface2, 1, 0, 1, 1)
        self.txtSurface1 = QtGui.QLineEdit(self.fraSurface)
        self.txtSurface1.setObjectName(_fromUtf8("txtSurface1"))
        self.gridLayout_5.addWidget(self.txtSurface1, 0, 1, 1, 1)
        self.lblSurface1 = QtGui.QLabel(self.fraSurface)
        self.lblSurface1.setWordWrap(True)
        self.lblSurface1.setObjectName(_fromUtf8("lblSurface1"))
        self.gridLayout_5.addWidget(self.lblSurface1, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.fraSurface, 0, 0, 1, 1)
        self.tabLID.addTab(self.Surface, _fromUtf8(""))
        self.Pavement = QtGui.QWidget()
        self.Pavement.setObjectName(_fromUtf8("Pavement"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Pavement)
        self.gridLayout_3.setMargin(11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.fraPavement = QtGui.QFrame(self.Pavement)
        self.fraPavement.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraPavement.setFrameShadow(QtGui.QFrame.Raised)
        self.fraPavement.setObjectName(_fromUtf8("fraPavement"))
        self.gridLayout_8 = QtGui.QGridLayout(self.fraPavement)
        self.gridLayout_8.setMargin(11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lblPavement1 = QtGui.QLabel(self.fraPavement)
        self.lblPavement1.setWordWrap(True)
        self.lblPavement1.setObjectName(_fromUtf8("lblPavement1"))
        self.gridLayout_8.addWidget(self.lblPavement1, 0, 0, 1, 1)
        self.txtPavement1 = QtGui.QLineEdit(self.fraPavement)
        self.txtPavement1.setObjectName(_fromUtf8("txtPavement1"))
        self.gridLayout_8.addWidget(self.txtPavement1, 0, 1, 1, 1)
        self.lblPavement2 = QtGui.QLabel(self.fraPavement)
        self.lblPavement2.setWordWrap(True)
        self.lblPavement2.setObjectName(_fromUtf8("lblPavement2"))
        self.gridLayout_8.addWidget(self.lblPavement2, 1, 0, 1, 1)
        self.txtPavement2 = QtGui.QLineEdit(self.fraPavement)
        self.txtPavement2.setObjectName(_fromUtf8("txtPavement2"))
        self.gridLayout_8.addWidget(self.txtPavement2, 1, 1, 1, 1)
        self.lblPavement3 = QtGui.QLabel(self.fraPavement)
        self.lblPavement3.setWordWrap(True)
        self.lblPavement3.setObjectName(_fromUtf8("lblPavement3"))
        self.gridLayout_8.addWidget(self.lblPavement3, 2, 0, 1, 1)
        self.txtPavement3 = QtGui.QLineEdit(self.fraPavement)
        self.txtPavement3.setObjectName(_fromUtf8("txtPavement3"))
        self.gridLayout_8.addWidget(self.txtPavement3, 2, 1, 1, 1)
        self.lblPavement4 = QtGui.QLabel(self.fraPavement)
        self.lblPavement4.setWordWrap(True)
        self.lblPavement4.setObjectName(_fromUtf8("lblPavement4"))
        self.gridLayout_8.addWidget(self.lblPavement4, 3, 0, 1, 1)
        self.txtPavement4 = QtGui.QLineEdit(self.fraPavement)
        self.txtPavement4.setObjectName(_fromUtf8("txtPavement4"))
        self.gridLayout_8.addWidget(self.txtPavement4, 3, 1, 1, 1)
        self.lblPavement5 = QtGui.QLabel(self.fraPavement)
        self.lblPavement5.setWordWrap(True)
        self.lblPavement5.setObjectName(_fromUtf8("lblPavement5"))
        self.gridLayout_8.addWidget(self.lblPavement5, 4, 0, 1, 1)
        self.txtPavement5 = QtGui.QLineEdit(self.fraPavement)
        self.txtPavement5.setObjectName(_fromUtf8("txtPavement5"))
        self.gridLayout_8.addWidget(self.txtPavement5, 4, 1, 1, 1)
        self.gridLayout_3.addWidget(self.fraPavement, 0, 0, 1, 1)
        self.tabLID.addTab(self.Pavement, _fromUtf8(""))
        self.Soil = QtGui.QWidget()
        self.Soil.setObjectName(_fromUtf8("Soil"))
        self.gridLayout_6 = QtGui.QGridLayout(self.Soil)
        self.gridLayout_6.setMargin(11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.fraSoil = QtGui.QFrame(self.Soil)
        self.fraSoil.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraSoil.setFrameShadow(QtGui.QFrame.Raised)
        self.fraSoil.setObjectName(_fromUtf8("fraSoil"))
        self.gridLayout_2 = QtGui.QGridLayout(self.fraSoil)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblSoil1 = QtGui.QLabel(self.fraSoil)
        self.lblSoil1.setWordWrap(True)
        self.lblSoil1.setObjectName(_fromUtf8("lblSoil1"))
        self.gridLayout_2.addWidget(self.lblSoil1, 0, 0, 1, 1)
        self.txtSoil1 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil1.setObjectName(_fromUtf8("txtSoil1"))
        self.gridLayout_2.addWidget(self.txtSoil1, 0, 1, 1, 1)
        self.lblSoil2 = QtGui.QLabel(self.fraSoil)
        self.lblSoil2.setWordWrap(True)
        self.lblSoil2.setObjectName(_fromUtf8("lblSoil2"))
        self.gridLayout_2.addWidget(self.lblSoil2, 1, 0, 1, 1)
        self.txtSoil2 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil2.setObjectName(_fromUtf8("txtSoil2"))
        self.gridLayout_2.addWidget(self.txtSoil2, 1, 1, 1, 1)
        self.lblSoil3 = QtGui.QLabel(self.fraSoil)
        self.lblSoil3.setWordWrap(True)
        self.lblSoil3.setObjectName(_fromUtf8("lblSoil3"))
        self.gridLayout_2.addWidget(self.lblSoil3, 2, 0, 1, 1)
        self.txtSoil3 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil3.setObjectName(_fromUtf8("txtSoil3"))
        self.gridLayout_2.addWidget(self.txtSoil3, 2, 1, 1, 1)
        self.lblSoil4 = QtGui.QLabel(self.fraSoil)
        self.lblSoil4.setWordWrap(True)
        self.lblSoil4.setObjectName(_fromUtf8("lblSoil4"))
        self.gridLayout_2.addWidget(self.lblSoil4, 3, 0, 1, 1)
        self.txtSoil4 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil4.setObjectName(_fromUtf8("txtSoil4"))
        self.gridLayout_2.addWidget(self.txtSoil4, 3, 1, 1, 1)
        self.lblSoil5 = QtGui.QLabel(self.fraSoil)
        self.lblSoil5.setWordWrap(True)
        self.lblSoil5.setObjectName(_fromUtf8("lblSoil5"))
        self.gridLayout_2.addWidget(self.lblSoil5, 4, 0, 1, 1)
        self.txtSoil5 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil5.setObjectName(_fromUtf8("txtSoil5"))
        self.gridLayout_2.addWidget(self.txtSoil5, 4, 1, 1, 1)
        self.lblSoil6 = QtGui.QLabel(self.fraSoil)
        self.lblSoil6.setWordWrap(True)
        self.lblSoil6.setObjectName(_fromUtf8("lblSoil6"))
        self.gridLayout_2.addWidget(self.lblSoil6, 5, 0, 1, 1)
        self.txtSoil6 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil6.setObjectName(_fromUtf8("txtSoil6"))
        self.gridLayout_2.addWidget(self.txtSoil6, 5, 1, 1, 1)
        self.lblSoil7 = QtGui.QLabel(self.fraSoil)
        self.lblSoil7.setWordWrap(True)
        self.lblSoil7.setObjectName(_fromUtf8("lblSoil7"))
        self.gridLayout_2.addWidget(self.lblSoil7, 6, 0, 1, 1)
        self.txtSoil7 = QtGui.QLineEdit(self.fraSoil)
        self.txtSoil7.setObjectName(_fromUtf8("txtSoil7"))
        self.gridLayout_2.addWidget(self.txtSoil7, 6, 1, 1, 1)
        self.gridLayout_6.addWidget(self.fraSoil, 0, 0, 1, 1)
        self.tabLID.addTab(self.Soil, _fromUtf8(""))
        self.Storage = QtGui.QWidget()
        self.Storage.setObjectName(_fromUtf8("Storage"))
        self.gridLayout_7 = QtGui.QGridLayout(self.Storage)
        self.gridLayout_7.setMargin(11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.fraStorage = QtGui.QFrame(self.Storage)
        self.fraStorage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraStorage.setFrameShadow(QtGui.QFrame.Raised)
        self.fraStorage.setObjectName(_fromUtf8("fraStorage"))
        self.gridLayout_9 = QtGui.QGridLayout(self.fraStorage)
        self.gridLayout_9.setMargin(11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.lblStorage1 = QtGui.QLabel(self.fraStorage)
        self.lblStorage1.setWordWrap(True)
        self.lblStorage1.setObjectName(_fromUtf8("lblStorage1"))
        self.gridLayout_9.addWidget(self.lblStorage1, 0, 0, 1, 1)
        self.txtStorage1 = QtGui.QLineEdit(self.fraStorage)
        self.txtStorage1.setObjectName(_fromUtf8("txtStorage1"))
        self.gridLayout_9.addWidget(self.txtStorage1, 0, 1, 1, 1)
        self.lblStorage2 = QtGui.QLabel(self.fraStorage)
        self.lblStorage2.setWordWrap(True)
        self.lblStorage2.setObjectName(_fromUtf8("lblStorage2"))
        self.gridLayout_9.addWidget(self.lblStorage2, 1, 0, 1, 1)
        self.txtStorage2 = QtGui.QLineEdit(self.fraStorage)
        self.txtStorage2.setObjectName(_fromUtf8("txtStorage2"))
        self.gridLayout_9.addWidget(self.txtStorage2, 1, 1, 1, 1)
        self.lblStorage3 = QtGui.QLabel(self.fraStorage)
        self.lblStorage3.setWordWrap(True)
        self.lblStorage3.setObjectName(_fromUtf8("lblStorage3"))
        self.gridLayout_9.addWidget(self.lblStorage3, 2, 0, 1, 1)
        self.txtStorage3 = QtGui.QLineEdit(self.fraStorage)
        self.txtStorage3.setObjectName(_fromUtf8("txtStorage3"))
        self.gridLayout_9.addWidget(self.txtStorage3, 2, 1, 1, 1)
        self.lblStorage4 = QtGui.QLabel(self.fraStorage)
        self.lblStorage4.setWordWrap(True)
        self.lblStorage4.setObjectName(_fromUtf8("lblStorage4"))
        self.gridLayout_9.addWidget(self.lblStorage4, 3, 0, 1, 1)
        self.txtStorage4 = QtGui.QLineEdit(self.fraStorage)
        self.txtStorage4.setObjectName(_fromUtf8("txtStorage4"))
        self.gridLayout_9.addWidget(self.txtStorage4, 3, 1, 1, 1)
        self.gridLayout_7.addWidget(self.fraStorage, 0, 0, 1, 1)
        self.tabLID.addTab(self.Storage, _fromUtf8(""))
        self.Drain = QtGui.QWidget()
        self.Drain.setObjectName(_fromUtf8("Drain"))
        self.gridLayout_10 = QtGui.QGridLayout(self.Drain)
        self.gridLayout_10.setMargin(11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.frame = QtGui.QFrame(self.Drain)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fraDrain = QtGui.QFrame(self.frame)
        self.fraDrain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraDrain.setFrameShadow(QtGui.QFrame.Raised)
        self.fraDrain.setObjectName(_fromUtf8("fraDrain"))
        self.gridLayout_4 = QtGui.QGridLayout(self.fraDrain)
        self.gridLayout_4.setMargin(11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lblDrain1 = QtGui.QLabel(self.fraDrain)
        self.lblDrain1.setWordWrap(True)
        self.lblDrain1.setObjectName(_fromUtf8("lblDrain1"))
        self.gridLayout_4.addWidget(self.lblDrain1, 0, 0, 1, 1)
        self.txtDrain1 = QtGui.QLineEdit(self.fraDrain)
        self.txtDrain1.setObjectName(_fromUtf8("txtDrain1"))
        self.gridLayout_4.addWidget(self.txtDrain1, 0, 1, 1, 1)
        self.lblDrain2 = QtGui.QLabel(self.fraDrain)
        self.lblDrain2.setWordWrap(True)
        self.lblDrain2.setObjectName(_fromUtf8("lblDrain2"))
        self.gridLayout_4.addWidget(self.lblDrain2, 1, 0, 1, 1)
        self.txtDrain2 = QtGui.QLineEdit(self.fraDrain)
        self.txtDrain2.setObjectName(_fromUtf8("txtDrain2"))
        self.gridLayout_4.addWidget(self.txtDrain2, 1, 1, 1, 1)
        self.lblDrain3 = QtGui.QLabel(self.fraDrain)
        self.lblDrain3.setWordWrap(True)
        self.lblDrain3.setObjectName(_fromUtf8("lblDrain3"))
        self.gridLayout_4.addWidget(self.lblDrain3, 2, 0, 1, 1)
        self.txtDrain3 = QtGui.QLineEdit(self.fraDrain)
        self.txtDrain3.setObjectName(_fromUtf8("txtDrain3"))
        self.gridLayout_4.addWidget(self.txtDrain3, 2, 1, 1, 1)
        self.lblDrain4 = QtGui.QLabel(self.fraDrain)
        self.lblDrain4.setWordWrap(True)
        self.lblDrain4.setObjectName(_fromUtf8("lblDrain4"))
        self.gridLayout_4.addWidget(self.lblDrain4, 3, 0, 1, 1)
        self.txtDrain4 = QtGui.QLineEdit(self.fraDrain)
        self.txtDrain4.setObjectName(_fromUtf8("txtDrain4"))
        self.gridLayout_4.addWidget(self.txtDrain4, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.fraDrain)
        self.lblText = QtGui.QLabel(self.frame)
        self.lblText.setWordWrap(True)
        self.lblText.setObjectName(_fromUtf8("lblText"))
        self.verticalLayout.addWidget(self.lblText)
        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 1)
        self.tabLID.addTab(self.Drain, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabLID)
        self.verticalLayout_2.addWidget(self.fraTop)
        self.fraOKCancel = QtGui.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtGui.QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QtGui.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtGui.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout_2.addWidget(self.fraOKCancel)
        frmLID.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmLID)
        self.tabLID.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmLID)

    def retranslateUi(self, frmLID):
        frmLID.setWindowTitle(_translate("frmLID", "SWMM LID Control Editor", None))
        self.lblControlName.setText(_translate("frmLID", "Control Name:", None))
        self.lblLIDType.setText(_translate("frmLID", "LID Type:", None))
        self.lblSurface5.setText(_translate("frmLID", "Surface Prop 5", None))
        self.lblSurface4.setText(_translate("frmLID", "Surface Prop 4", None))
        self.lblSurface3.setText(_translate("frmLID", "Surface Prop 3", None))
        self.lblSurface2.setText(_translate("frmLID", "Surface Prop 2", None))
        self.lblSurface1.setText(_translate("frmLID", "Surface Prop 1", None))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Surface), _translate("frmLID", "Surface", None))
        self.lblPavement1.setText(_translate("frmLID", "Pavement 1", None))
        self.lblPavement2.setText(_translate("frmLID", "Pavement 2", None))
        self.lblPavement3.setText(_translate("frmLID", "Pavement 3", None))
        self.lblPavement4.setText(_translate("frmLID", "Pavement 4", None))
        self.lblPavement5.setText(_translate("frmLID", "Pavement 5", None))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Pavement), _translate("frmLID", "Pavement", None))
        self.lblSoil1.setText(_translate("frmLID", "Soil 1", None))
        self.lblSoil2.setText(_translate("frmLID", "Soil 2", None))
        self.lblSoil3.setText(_translate("frmLID", "Soil 3", None))
        self.lblSoil4.setText(_translate("frmLID", "Soil 4", None))
        self.lblSoil5.setText(_translate("frmLID", "Soil 5", None))
        self.lblSoil6.setText(_translate("frmLID", "Soil 6", None))
        self.lblSoil7.setText(_translate("frmLID", "Soil 7", None))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Soil), _translate("frmLID", "Soil", None))
        self.lblStorage1.setText(_translate("frmLID", "Storage 1", None))
        self.lblStorage2.setText(_translate("frmLID", "Storage 2", None))
        self.lblStorage3.setText(_translate("frmLID", "Storage 3", None))
        self.lblStorage4.setText(_translate("frmLID", "Storage 4", None))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Storage), _translate("frmLID", "Storage", None))
        self.lblDrain1.setText(_translate("frmLID", "Drain 1", None))
        self.lblDrain2.setText(_translate("frmLID", "Drain 2", None))
        self.lblDrain3.setText(_translate("frmLID", "Drain 3", None))
        self.lblDrain4.setText(_translate("frmLID", "Drain 4", None))
        self.lblText.setText(_translate("frmLID", "Explanatory Text", None))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Drain), _translate("frmLID", "Drain", None))
        self.cmdOK.setText(_translate("frmLID", "OK", None))
        self.cmdCancel.setText(_translate("frmLID", "Cancel", None))

