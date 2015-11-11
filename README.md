MayaPy - CIS 510 Class project
======

----Peter M, Ryan L.----

Project details follow:


Graphics:

1. [face.ma](https://github.com/pemj/MayaPy/blob/master/graphics/face.ma)
   * will eventualy contain the base face model.

The python application will be separated into a simple layered hierarchy following a basic MVC architecture. From the GUI down to the Nimble Bridge, our architecture will be the following:

1. [widget.ui](https://github.com/pemj/MayaPy/blob/master/resources/widget/ChernoffFaceWidget/widget.ui)
    * Created with QT Creator
    * Contains a collection of sliders to take user input

2. [ChernoffFaceWidget.py](https://github.com/pemj/MayaPy/blob/master/src/mayapy/views/chernoffface/ChernoffFaceWidget.py)
   * Manages callbacks from [widget.ui](https://github.com/pemj/MayaPy/blob/master/resources/widget/ChernoffFaceWidget/widget.ui)
   * Hands parameter change requests off to [FaceController.py.](https://github.com/pemj/MayaPy/blob/master/src/mayapy/views/chernoffface/FaceController.py)

3. [FaceController.py](https://github.com/pemj/MayaPy/blob/master/src/mayapy/views/chernoffface/FaceController.py)
   * Programmatically controls the model’s rigging via a Nimble Bridge
   * Will poll state of the maya model before making alterations
   * Relies heavily on Model’s naming convention
