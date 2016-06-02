import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import core.swmm.project
from ui.SWMM.frmProfilePlotDesigner import Ui_frmProfilePlot
from ui.help import HelpHandler


class frmProfilePlot(QtGui.QMainWindow, Ui_frmProfilePlot):

    def __init__(self, main_form):
        QtGui.QMainWindow.__init__(self, main_form)
        self.help_topic = "swmm/src/src/controlrules.htm"
        self.setupUi(self)
        QtCore.QObject.connect(self.cmdOK, QtCore.SIGNAL("clicked()"), self.cmdOK_Clicked)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.cmdCancel_Clicked)

        # self.set_from(parent.project)
        self._main_form = main_form

    # def set_from(self, project):
        # section = core.epanet.project.Control()
        # section = project.find_section("CONTROLS")
        # self.txtControls.setPlainText(str(section.get_text()))

    def cmdOK_Clicked(self):
        # section = self._main_form.project.find_section("CONTROLS")
        # section.set_text(str(self.txtControls.toPlainText()))
        self.close()

    def cmdCancel_Clicked(self):
        self.close()
