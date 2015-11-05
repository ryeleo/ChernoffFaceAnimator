# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from math import radians, sin, cos
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
        self.runBtn.clicked.connect(self._handleRunBtn)
        self.kickBtn.clicked.connect(self._handleKickBtn)
        self.raiseBtn.clicked.connect(self._handleRaiseBtn)
        self.rotateBtn.clicked.connect(self._handleRotBtn)
        self.undoBtn.clicked.connect(self._handleUndoBtn)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.timeBox.valueChanged.connect(self._handleValChange)
        self.distBox.valueChanged.connect(self._handleValChange)
        self.rotDial.valueChanged.connect(self._handleValChange)
    #===================================================================================================
    #                                                                                 H A N D L E R S
    
    #___________________________________________________________________________________________________ _handleRunBtn
    def _handleRunBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.
        
        """
        time = self.currTime
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder2')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
        


    #___________________________________________________________________________________________________ _handleRotBtn
    def _handleRotBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.
        
        """
        time = self.currTime
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder2')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)     

        


    #___________________________________________________________________________________________________ _handleKickBtn
    def _handleKickBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.
        
        """
        time = self.currTime
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder2')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)

        
    #___________________________________________________________________________________________________ _handleRaiseBtn
    def _handleRaiseBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.
        
        """
        time = self.currTime
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder2')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
        


    #___________________________________________________________________________________________________ _getX
    def _getX(self):
        currTime = self.timeBox.value()
        currDist = self.distBox.value()
        currAngle = self.rotDial.value()
        rad = radians(currAngle)
        h = currDist
        return(cos(rad) * h)
    

    #___________________________________________________________________________________________________ _getY
    def _getY(self):
        currTime = self.timeBox.value()
        currDist = self.distBox.value()
        currAngle = self.rotDial.value()
        rad = radians(currAngle)
        h = currDist
        return(sin(rad) * h)
    

    #___________________________________________________________________________________________________ _updateDisplays
    def _updateDisplays(self):
        self.frameDisplay.display(self.timeBox.value())
        self.xDisplay.display(self._getX())
        self.yDisplay.display(self._getY())



    #___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')


    #___________________________________________________________________________________________________ _handleTimeChange
    def _handleValChange(self):
        self._updateDisplays()
