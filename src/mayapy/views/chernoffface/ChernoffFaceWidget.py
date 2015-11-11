# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from math import radians, sin, cos
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from Assignment3Tools import findName, bAlter, limbRotate

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
        #first we raise the leg, then halfway through the leg raise, we start jumping a bit, and raise the back leg in reverse
        currTime = self.timeBox.value()
        changeTime = (self.distBox.value()*10)
        endTime = currTime + changeTime
        cmds.currentTime(currTime, edit=True)
        RArm = findName("arm_R")
        LArm = findName("arm_L")
        arm = ""
        leg = ""
        R = findName("leg_R")
        L = findName("left_L")
        bod = findName("body")
        
        
        #we start by beginning the X/Z translation keys at the same time
        cmds.currentTime(currTime, edit=True)
        bAlter(bod, changeTime, self._getX(), "translateX")
        cmds.currentTime(currTime, edit=True)
        bAlter(bod, changeTime, self._getZ(), "translateZ")
        #then, while currTime < endTime, move the legs, hop up and down.
        while (currTime < endTime):
            #move the right leg up
            limbRotate(R, 10, -60) 
            #while doing so, move the left arm up
            cmds.currentTime(currTime, edit=True)
            limbRotate(LArm, 10, -60)   
            #while doing so, move the right arm slightly back
            cmds.currentTime(currTime, edit=True)
            limbRotate(RArm, 10, 30)
            #while doings so, move the left leg slightly back
            cmds.currentTime(currTime, edit=True)
            limbRotate(L, 10, 30)        
            #meanwhile, we also need to start hopping.
            cmds.currentTime(currTime, edit=True)
            bAlter(bod, 10, 1, "translateY")
            currTime += 10            
            #move the right leg down
            limbRotate(R, 10, 60) 
            #while doing so, move the left arm down
            cmds.currentTime(currTime, edit=True)
            limbRotate(LArm, 10, 60)   
            #while doing so, move the right arm back forward
            cmds.currentTime(currTime, edit=True)
            limbRotate(RArm, 10, -30)
            #while doings so, move the left leg back forward
            cmds.currentTime(currTime, edit=True)
            limbRotate(L, 10, -30)    
            #no we're at the peak, everything back to neutral
            cmds.currentTime(currTime, edit=True)
            bAlter(bod, 10, -1, "translateY")
            currTime += 10
            arm = RArm
            RArm = LArm
            LArm = arm

            leg = R
            R = L
            L = leg
        self.frameDisplay.display(endTime)

    #___________________________________________________________________________________________________ _handleRotBtn
    def _handleRotBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.
        
        """
        cmds.currentTime(self.timeBox.value(), edit=True)
        currAngle = self.rotDial.value()
        changeTime = currAngle * (20.0/90.0)
        bod = findName("body")
        bAlter(bod, changeTime, currAngle, "rotateY")
        self.frameDisplay.display(self.timeBox.value() + changeTime)

        


    #___________________________________________________________________________________________________ _handleUndoBtn
    def _handleUndoBtn(self):
        """
        This callback undoes the last action.
        
        """
        cmds.undo()       


    #___________________________________________________________________________________________________ _handleKickBtn
    def _handleKickBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.
        
        """
        cmds.currentTime(self.timeBox.value(), edit=True)
        limb = findName("leg_R")
        limbRotate(limb, 10, 35)
        cmds.currentTime(self.timeBox.value() + 10, edit=True)
        limbRotate(limb, 15, -100) 
        self.frameDisplay.display(self.timeBox.value() + 35)


        
    #___________________________________________________________________________________________________ _handleRaiseBtn
    def _handleRaiseBtn(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        cmds.currentTime(self.timeBox.value(), edit=True)
        arm_l = findName("arm_L")
        limbRotate(arm_l, 20, -140) 
        self.frameDisplay.display(self.timeBox.value() + 20)


    #___________________________________________________________________________________________________ _getX
    def _getZ(self):
        currDist = self.distBox.value()
        currAngle = self.rotDial.value()
        rad = radians(currAngle)
        h = currDist
        return(cos(rad) * h)
    

    #___________________________________________________________________________________________________ _getZ
    def _getX(self):
        currDist = self.distBox.value()
        currAngle = self.rotDial.value()
        rad = radians(currAngle)
        h = currDist
        return(sin(rad) * h)
    

    #___________________________________________________________________________________________________ _updateDisplays
    def _updateDisplays(self):
        #self.frameDisplay.display(self.timeBox.value())
        self.xDisplay.display(self._getX())
        self.zDisplay.display(self._getZ())



    #___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')


    #___________________________________________________________________________________________________ _handleTimeChange
    def _handleValChange(self):
        self._updateDisplays()
