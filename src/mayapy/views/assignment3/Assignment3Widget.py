# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment3Widget
class Assignment3Widget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment3Widget."""
        super(Assignment3Widget, self).__init__(parent, **kwargs)
        self.runBtn.clicked.connect(self._handleRunButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleRunButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder2')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
