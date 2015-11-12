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

Other files of interest include:

1. [mpl_cfaces.py] (https://gist.github.com/pemj/c32df80f53e0ccfdbd55) is a bit of code that generates 2D chernoff faces.  Interface is, uh, suboptimal, but we can probably encapsulate it without too much issue.

2. [Main Window](https://github.com/pemj/MayaPy/blob/master/src/mayapy/MayaPyMainWindow.py) is a file that describes the homepage of the project interface.  It currently contains a link to the stubbed out version of the project screen.

2. [Home Screen](https://github.com/pemj/MayaPy/blob/master/src/mayapy/views/home/MayaPyHomeWidget.py) is a file that dictates the semantics of the home page.  That is to say, it listens to buttons and executes the code to display other screens (or to connect to maya).