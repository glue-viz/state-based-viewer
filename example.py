from glue.external.qt import get_qapp, QtGui
from glue.core.session import Session
from glue.core import Data, DataCollection

from data_viewer import ScatterViewer

data = Data(x=[1, 2, 3], y=[1, 3, 2])
dc = DataCollection([data])

app = get_qapp()

session = Session(application=app, data_collection=dc)

viewer = ScatterViewer(session)

window = QtGui.QWidget()

viewer.add_data(data)

vlayout = QtGui.QVBoxLayout()
vlayout.addWidget(viewer._layer_artist_container[0].style_editor)
vlayout.addWidget(viewer.options_widget())
vwidget = QtGui.QWidget()
vwidget.setLayout(vlayout)

hlayout = QtGui.QHBoxLayout()
hlayout.addWidget(vwidget)
hlayout.addWidget(viewer)

window.setLayout(hlayout)

window.show()

app.exec_()
