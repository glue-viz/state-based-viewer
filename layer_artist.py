from glue.core.layer_artist import LayerArtistBase
# from glue.external.echo import CallbackProperty

from layer_style_editor import ScatterLayerStyleEditor
from helpers import State


class ScatterLayerState(State):
    pass


class ScatterLayerArtist(LayerArtistBase):

    def __init__(self, layer, axes, viewer_state):

        # Keep a reference to the layer (data or subset) and axes
        self.layer = layer
        self.axes = axes

        # Set up a state object for the layer artists
        self.layer_state = ScatterLayerState()

        # Set up the layer style editor
        self.style_editor = ScatterLayerStyleEditor(self.layer_state)

    def clear(self):
        pass

    def redraw(self):
        pass

    def update(self):
        pass
