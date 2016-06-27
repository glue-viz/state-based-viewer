from glue.external.qt import QtGui


class ScatterLayerStyleEditor(QtGui.QWidget):
    def __init__(self, layer_state, parent=None):
        super(ScatterLayerStyleEditor, self).__init__(parent=parent)
