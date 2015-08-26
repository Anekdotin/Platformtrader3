__author__ = 'ed'
import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import style
style.use('dark_background')


import json
import pandas as pd
import numpy as np
import urllib

f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)




class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)


        self.setWindowTitle("PyQT Mappn!")
#_________________________________________________________________________
#(Menubah)



        self.myQMenuBar = QtGui.QMenuBar(self)
        exitMenu = self.myQMenuBar.addMenu('File')
        exitAction = QtGui.QAction('Exit', self)
        exitAction.triggered.connect(QtGui.qApp.quit)
        exitMenu.addAction(exitAction)


        self.canvas = FigureCanvas(f)
        self.canvas.show()





        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.animate)


        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Menubar')
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

        a.plot_date(buyDates, buys["price"])
        a.plot_date(sellDates, sells["price"])

    #ani = animation.FuncAnimation(f, animate, interval=1000)

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())