from __future__ import division
from glue.external.echo import add_callback, CallbackProperty
from glue.utils.qt.widget_properties import (connect_bool_button, connect_value,
                                             connect_current_combo)
from glue.utils.qt.colors import connect_color


class State(object):

    def __init__(self):
        self._global_callbacks = []

    def connect(self, name, callback):
        add_callback(self, name, callback)

    def connect_all(self, callback):
        self._global_callbacks.append(callback)

    def __setattr__(self, attr, value):
        object.__setattr__(self, attr, value)
        if isinstance(getattr(type(self), attr, None), CallbackProperty):
            for callback in self._global_callbacks:
                callback()


def autoconnect_qt(state, widget):

    for child in widget.children():

        full_name = child.objectName()

        if '_' in full_name:

            wtype, wname = full_name.split('_', 1)

            if hasattr(state, wname):

                item = getattr(widget, full_name)

                if wtype == 'value':
                    connect_value(state, wname, item)
                elif wtype == 'text':
                    connect_text(state, wname, item)
                elif wtype == 'bool':
                    connect_bool_button(state, wname, item)
                elif wtype == 'combo':
                    connect_current_combo(state, wname, item)
                elif wtype == 'color':
                    connect_color(state, wname, item)


def connect_text(client, prop, widget):

    def update_prop():
        val = widget.text()
        setattr(client, prop, val)

    def update_widget(val):
        widget.setText(val)

    add_callback(client, prop, update_widget)
    try:
        widget.editingFinished.connect(update_prop)
    except AttributeError:
        pass
