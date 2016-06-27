from glue.viewers.common.qt.data_viewer import DataViewer
from glue.viewers.common.qt.mpl_widget import MplWidget
from glue.external.echo import CallbackProperty

from layer_artist import ScatterLayerArtist
from options_widget import ScatterOptionsWidget
from helpers import State


class ScatterViewerState(State):
    xatt = CallbackProperty()
    yatt = CallbackProperty()


class ScatterViewer(DataViewer):

    def __init__(self, session, parent=None):

        super(ScatterViewer, self).__init__(session, parent)

        # Use MplWidget to set up a Matplotlib canvas inside the Qt window
        self.mpl_widget = MplWidget()
        self.setCentralWidget(self.mpl_widget)

        # Set up the state which will contain everything needed to represent
        # the current state of the viewer
        self.viewer_state = ScatterViewerState()

        # Set up the options widget, which will include options that control the
        # viewer state
        self.options = ScatterOptionsWidget(viewer_state=self.viewer_state,
                                            session=session)

    def add_data(self, data):

        self.options.add_data(data)

        # Create scatter layer artist and add to container
        layer = ScatterLayerArtist(data, self.mpl_widget, self.viewer_state)
        layer.zorder = 0
        self._layer_artist_container.append(layer)

    def options_widget(self):
        return self.options


if __name__ == "__main__":

    from glue.external.qt import get_qapp, QtGui
    from glue.core.session import Session
    from glue.core import Data, DataCollection

    data = Data(x=[1, 2, 3], y=[1, 3, 2])
    dc = DataCollection([data])

    app = get_qapp()

    session = Session(application=app, data_collection=dc)

    viewer = ScatterViewer(session)

    window = QtGui.QWidget()
    layout = QtGui.QHBoxLayout()
    layout.addWidget(viewer.options_widget())
    layout.addWidget(viewer)
    window.setLayout(layout)

    window.show()

    viewer.add_data(data)

    app.exec_()
