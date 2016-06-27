from __future__ import division
from glue.external.echo import add_callback
from glue.utils.qt.widget_properties import (connect_bool_button, connect_value,
                                             connect_current_combo)


class State(object):

    def connect(self, name, callback):
        add_callback(self, name, callback)

    def autoconnect_qt(self, widget):

        for child in widget.children():

            full_name = child.objectName()

            if '_' in full_name:

                wtype, wname = full_name.split('_', 1)

                if wtype == 'value':
                    connect_value(self, wname, getattr(widget, full_name))
                elif wtype == 'text':
                    connect_text(self, wname, getattr(widget, full_name))
                elif wtype == 'bool':
                    connect_bool_button(self, wname, getattr(widget, full_name))
                elif wtype == 'combo':
                    connect_current_combo(self, wname, getattr(widget, full_name))


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
