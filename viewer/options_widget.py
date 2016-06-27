import os

from glue.external.qt import QtGui
from glue.utils.qt import load_ui
from glue.core.qt.data_combo_helper import ComponentIDComboHelper

from .helpers import autoconnect_qt


class ScatterOptionsWidget(QtGui.QWidget):

    def __init__(self, viewer_state, session, parent=None):

        super(ScatterOptionsWidget, self).__init__(parent=parent)

        self.ui = load_ui('options_widget.ui', self,
                          directory=os.path.dirname(__file__))

        self.viewer_state = viewer_state
        autoconnect_qt(self.viewer_state, self)

        self.viewer_state.connect('layers', self._update_combo_data)

        self.xatt_helper = ComponentIDComboHelper(self.ui.combo_xatt,
                                                  session.data_collection)
        self.yatt_helper = ComponentIDComboHelper(self.ui.combo_yatt,
                                                  session.data_collection)

    def _update_combo_data(self, *args):
        # TODO: we need to make it possible to set all the data in one go
        #       to avoid this inefficiency which will also cause the current
        #       value to not be selected anymore.
        self.xatt_helper.clear()
        self.yatt_helper.clear()
        for data in self.viewer_state.layers:
            self.xatt_helper.append(data)
            self.yatt_helper.append(data)
