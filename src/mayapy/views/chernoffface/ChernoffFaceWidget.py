# ChernoffFaceWidget.py
# (C)2013
# Scott Ernst, Peter McKay, Ryan Leonard.

import nimble
from math import radians, sin, cos
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
import FaceController as fc

#___________________________________________________________________________________________________ ChernoffFaceWidget
class ChernoffFaceWidget(PyGlassWidget):
    """A class for Assignment 1"""
    
#===================================================================================================
#                                                                                       C L A S S
#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment3Widget."""
        super(ChernoffFaceWidget, self).__init__(parent, **kwargs)
        self.eyebrowAngleSlider.valueChanged.connect(self._handleValChange)
        self.mouthAngleSlider.valueChanged.connect(self._handleValChange)
        self.eyeSizeSlider.valueChanged.connect(self._handleValChange)
        self.headShapeSlider.valueChanged.connect(self._handleValChange)
        self.eyeSpacingSlider.valueChanged.connect(self._handleValChange)
		
    #===================================================================================================
    #                                                                                 H A N D L E R S
  
    #___________________________________________________________________________________________________ _handleValChange
    def _handleValChange(self):
		print("eyebrow angle: "+str(self.eyeSpacingSlider.value()))
		print("mouth angle: "+str(self.eyeSpacingSlider.value()))
		print("eye size: "+str(self.eyeSpacingSlider.value()))
		print("head shape: "+str(self.eyeSpacingSlider.value()))
		print("eye spacing: "+str(self.eyeSpacingSlider.value()))
