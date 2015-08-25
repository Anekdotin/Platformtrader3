__author__ = 'ed'
import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt

import random

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.button2 = QtGui.QPushButton('Clear Plot')
        self.button2.clicked.connect(self.clearplot)

        self.button3 = QtGui.QPushButton('Clear Plot')
        self.button3.clicked.connect(self.clearplot)



#_________________________________________________________________________
#(down starting from top, from left, continuing, how many rows it spas across)
        grid = QtGui.QGridLayout()
        grid.addWidget(self.toolbar, 1, 0, 2, 4)
        grid.addWidget(self.canvas, 2, 0, 2, 4)
        grid.addWidget(self.button, 0, 1, 1, 1)
        grid.addWidget(self.button2, 0, 0, 1, 1)
        grid.addWidget(self.button3, 0, 2, 1, 1)
        self.setLayout(grid)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()
    def clearplot(self):
        self.canvas.clear()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())