from glue.external.qt import QtGui


class ScatterOptionsWidget(QtGui.QWidget):
    def __init__(self, viewer_state, parent=None):
        super(ScatterOptionsWidget, self).__init__(self, parent=parent)
