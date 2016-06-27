import os

from glue.external.qt import QtGui
from glue.utils.qt import load_ui

from .helpers import autoconnect_qt


class ScatterLayerStyleEditor(QtGui.QWidget):

    def __init__(self, layer_state, parent=None):

        super(ScatterLayerStyleEditor, self).__init__(parent=parent)

        self.ui = load_ui('layer_style_editor.ui', self,
                          directory=os.path.dirname(__file__))

        autoconnect_qt(layer_state, self)
        autoconnect_qt(layer_state.layer.style, self)

        # layer_state.layer.style
        # self.viewer_state = viewer_state
        # self.viewer_state.autoconnect_qt(self)
        # self.viewer_state.connect('layers', self._update_combo_data)
