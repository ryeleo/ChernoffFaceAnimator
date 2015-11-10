MayaPy - CIS 510 Class project
======

----Peter M, Ryan L.----

Project details follow:


Graphics:
MayaPy/graphics/face.ma -- will eventualy contain the base face model.

The python application will be separated into a simple layered hierarchy following a basic MVC architecture. From the GUI down to the Nimble Bridge, our architecture will be the following:

MayaPy/resources/widget/Assignment4Widget/widget.ui
Created with QT Creator
Contains a collection of sliders to take user input

MayaPy/src/mayapy/views/assignment4/ChernoffFaceWidget.py
Manages callbacks from Widget.ui
Hands parameter change requests off to FaceController.py.

MayaPy/src/mayapy/views/assignment4/FaceController.py
Programmatically controls the model’s rigging via a Nimble Bridge
Will poll state of the maya model before making alterations
Relies heavily on Model’s naming convention
