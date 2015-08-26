__author__ = 'ed'
import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import style
#style.use('dark_background')
from matplotlib import pyplot as plt

import json
import pandas as pd
import numpy as np
import urllib

f = Figure()
a = f.add_subplot(111)




class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(500, 300, 800, 600)

        self.setWindowTitle("PyQT Mappn!")
#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)

        FileMenu = self.myQMenuBar.addMenu('File')

#______________


        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Program')
        exitAction.triggered.connect(QtGui.qApp.quit)

        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create new file')
        newAction.triggered.connect(self.newFile)

        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current file')
        saveAction.triggered.connect(self.saveFile)

        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)

        FileMenu.addAction(newAction)
        FileMenu.addAction(saveAction)
        FileMenu.addAction(openAction)
        FileMenu.addAction(exitAction)





#_________________________________________________________________________
#

#Canvas------------------

        self.canvas = FigureCanvas(f)
        self.canvas.show()





        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.animate)




        self.show()



#_________________________________________________________________________
#(down starting from top, from left, continuing, how many rows it spas across)
        grid = QtGui.QGridLayout()

        grid.addWidget(self.canvas, 0, 0, 2, 4)
        grid.addWidget(self.button, 2, 1, 1, 1)


        self.setLayout(grid)
#_________________________________________________________________________


    def animate(i):
        dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
        data = urllib.request.urlopen(dataLink)
        data = data.readall().decode("utf-8")
        data = json.loads(data)


        data = data["btc_usd"]
        data = pd.DataFrame(data)

        buys = data[(data['type']=="bid")]
        buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()


        sells = data[(data['type']=="ask")]
        sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        a.clear()

        a.plot_date(buyDates, buys["price"], '#00A3E0', label="buys")
        a.plot_date(sellDates, sells["price"], '#183a54', label="sells")

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2,borderaxespad=0)

        title = "BTC-e BTCUSD PRices/nLast Price: "+str(data["price"][1999])
        a.set_title(title)

    #ani = animation.FuncAnimation(f, animate, interval=1000)


#_________________________________________________________________________
    #Functions--------------------------------------------------------------


    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()
    def openFile(self):
        pass
    def saveFile(self):
        pass
    def newFile(self):
        pass
#______________________
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())