from glue.core.layer_artist import LayerArtistBase
from glue.external.echo import CallbackProperty, add_callback
from glue.utils import nonpartial

from .layer_style_editor import ScatterLayerStyleEditor
from .helpers import State


class ScatterLayerState(State):
    layer = CallbackProperty()
    join = CallbackProperty()


class ScatterLayerArtist(LayerArtistBase):

    def __init__(self, layer, axes, viewer_state):

        # Keep a reference to the layer (data or subset) and axes
        self.layer = layer
        self.axes = axes
        self.viewer_state = viewer_state

        # Watch for changes in the viewer state which would require the
        # layers to be redrawn
        # TODO: don't connect to ALL signals here
        self.viewer_state.connect_all(nonpartial(self.update))

        # Set up a state object for the layer artists
        self.layer_state = ScatterLayerState()
        self.layer_state.layer = layer
        self.layer_state.connect_all(self.update)

        # TODO: need to connect to visual properties of layer in one go
        add_callback(self.layer.style, 'color', nonpartial(self.update))
        add_callback(self.layer.style, 'markersize', nonpartial(self.update))

        # Set up the layer style editor
        self.style_editor = ScatterLayerStyleEditor(self.layer_state)

        # Set up an initially empty artist
        self.artist1 = self.axes.plot([], [], 'o')[0]
        self.artist2 = self.axes.plot([], [], '-')[0]

        self.zorder = 0
        self.update()

    def clear(self):
        pass

    def redraw(self):
        self.axes.figure.canvas.draw()

    def update(self):
        x = self.layer[self.viewer_state.xatt[0]]
        y = self.layer[self.viewer_state.yatt[0]]
        for artist in [self.artist1, self.artist2]:
            artist.set_data(x, y)
            artist.set_color(self.layer.style.color)
            artist.set_markersize(self.layer.style.markersize)
        self.artist2.set_visible(self.layer_state.join)
        self.redraw()
