from glue.viewers.common.qt import DataViewer
from glue.viewers.common.qt.mpl_widget import MplWidget
from glue.external.echo import CallbackProperty

from layer_artist import NewScatterLayerArtist
from options_widget import ScatterOptionsWidget


class ScatterViewerState(object):
    xatt = CallbackProperty()
    yatt = CallbackProperty()


class ScatterViewer(DataViewer):

    def __init__(self, session, parent=None):

        super(ScatterViewer, self).__init__(session, parent)

        # Use MplWidget to set up a Matplotlib canvas inside the Qt window
        self.mpl_widget = MplWidget()
        self.setCentralWidget(self.central_widget)

        # Set up the state which will contain everything needed to represent
        # the current state of the viewer
        self.state = ScatterViewerState()

        # Set up the options widget, which will include options that control the
        # viewer state
        self.options = ScatterOptionsWidget(viewer_state=self.state)

    def add_data(self, data):

        # Create scatter layer artist and add to container
        layer = NewScatterLayerArtist(data, self.mpl_widget.axes)
        self._layer_artist_container.append(layer)
