import os
from glue.external.qt import QtGui
from glue.utils.qt import load_ui
from glue.core.qt.data_combo_helper import ComponentIDComboHelper


class ScatterOptionsWidget(QtGui.QWidget):

    def __init__(self, viewer_state, session, parent=None):

        super(ScatterOptionsWidget, self).__init__(parent=parent)

        self.ui = load_ui('options_widget.ui', self,
                          directory=os.path.dirname(__file__))

        self.xatt_helper = ComponentIDComboHelper(self.ui.combo_xatt,
                                                  session.data_collection)
        self.yatt_helper = ComponentIDComboHelper(self.ui.combo_yatt,
                                                  session.data_collection)

    def add_data(self, data):
        self.xatt_helper.append(data)
        self.yatt_helper.append(data)
