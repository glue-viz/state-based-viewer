from glue.viewers.common.qt.data_viewer import DataViewer
from glue.viewers.common.qt.mpl_widget import MplWidget
from glue.external.echo import CallbackProperty

from .layer_artist import ScatterLayerArtist
from .options_widget import ScatterOptionsWidget
from .helpers import State


class ScatterViewerState(State):
    xatt = CallbackProperty()
    yatt = CallbackProperty()
    layers = CallbackProperty(())


class ScatterViewer(DataViewer):

    def __init__(self, session, parent=None):

        super(ScatterViewer, self).__init__(session, parent)

        # Use MplWidget to set up a Matplotlib canvas inside the Qt window
        self.mpl_widget = MplWidget()
        self._axes = self.mpl_widget.canvas.figure.add_subplot(1, 1, 1)
        self._axes.set_xlim(-10, 10)
        self._axes.set_ylim(-10, 10)
        self.setCentralWidget(self.mpl_widget)

        # Set up the state which will contain everything needed to represent
        # the current state of the viewer
        self.viewer_state = ScatterViewerState()

        # Set up the options widget, which will include options that control the
        # viewer state
        self.options = ScatterOptionsWidget(viewer_state=self.viewer_state,
                                            session=session)

        self.viewer_state.connect_all(self.update)

    def add_data(self, data):

        if data in self.viewer_state.layers:
            return

        # Add data to the list of layers
        # TODO: make callback iterable which callbacks when changed to avoid
        # using tuples here - this is messy at the moment, and removing is not
        # going to be much fun.
        self.viewer_state.layers += (data,)

        # Create scatter layer artist and add to container
        layer = ScatterLayerArtist(data, self._axes, self.viewer_state)
        self._layer_artist_container.append(layer)

    def options_widget(self):
        return self.options
