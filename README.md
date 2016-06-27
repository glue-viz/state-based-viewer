About
-----

This repository contains a prototype viewer for glue which uses state objects
to carry around the state for various ui elements. All communication between
classes is effectively done by modifying the state and having callbacks. The
main classes/objects are the following:

``ScatterViewer``: the main ``DataViewer`` class - rather than have attributes,
this class has a ``viewer_state`` attribute that contains an instance of the
``ScatterViewerState`` class, which contains all the information required to
describe the viewer itself. This includes ``xatt``, ``yatt``, and ``layers`` (a
set of all the datasets and subsets currently in the viewer).

The options for the ``ScatterViewer`` are controlled from the
``ScatterOptionsWidget`` widget, which is given access to the
``ScatterViewerState``. The appearance of this widget is defined in the
``optins_widget.ui`` file, and we auto-link the widgets in that layout to the
attributes in the ``ScatterViewerState`` (we do this based on the name of the
widgets and state attributes).

The ``ScatterViewer`` instantiates ``ScatterLayerArtist`` objects which are
given the ``ScatterViewerState`` as well as the Matplotlib Axes. In this way,
the layer artists can register to receive callbacks from the
``ScatterViewerState`` whenever e.g. one of the x or y attributes is changed. In
addition, the ``ScatterLayerArtist`` defines its own state object for things
related to the visual settings or that particular layer artist. However, some
of the settings are actually already defined in the ``style`` attribute of
``Data`` objects, so essentially the ``ScatterLayerArtist`` has two state
objects, one global one for the data, and one with additional options specific
to this viewer.

In the example here, the marker size and color are global ``Data`` attributes,
while we have a third option to join or not the points, which is an option
local to this viewer.

To run the example, simply do:

    python example.py
