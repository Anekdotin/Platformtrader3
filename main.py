__author__ = 'ed'
import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates



def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


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
        self.button.clicked.connect(self.graph_data)

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
        #grid.addWidget(self.button3, 0, 2, 1, 1)
        self.setLayout(grid)



    def graph_data(self, stock):
        stock= 'TSLA'
        stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
        source_code = urllib.request.urlopen(stock_price_url).read().decode()
        stock_data = []
        split_source = source_code.split('\n')
        for line in split_source:
            split_line = line.split(',')
            if len(split_line) == 6:
                if 'values' not in line and 'labels' not in line:
                    stock_data.append(line)

        date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                              delimiter=',',
                                                              unpack=True,
                                                              # %Y = full year. 2015
                                                              # %y = partial year 15
                                                              # %m = number month
                                                              # %d = number day
                                                              # %H = hours
                                                              # %M = minutes
                                                              # %S = seconds
                                                              # 12-06-2014
                                                              # %m-%d-%Y
                                                              converters={0: bytespdate2num('%Y%m%d')})

        plt.plot_date(date, closep,'-', label='Price')

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Interesting Graph\nCheck it out')
        plt.legend()

        self.canvas.draw()





    def clearplot(ax, data):
        while ax.plot():
            data.close()




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())