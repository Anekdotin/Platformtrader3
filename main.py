#! /usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
#style.use('dark_background')
from matplotlib import pyplot as plt

import json
import pandas as pd
import numpy as np
import urllib

f = Figure()
a = f.add_subplot(111)


exchange = "btce"
DatCounter = 9000
programName = "btce"


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(500, 300, 800, 600)

        self.setWindowTitle("PyQT Mappn!")
#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)

        FileMenu = self.myQMenuBar.addMenu('File')

        AboutMenu = self.myQMenuBar.addMenu('About')

        exchangeChoice = self.myQMenuBar.addMenu('Exchanges')

        dataTF = self.myQMenuBar.addMenu('Data Time')

        OHLCI = self.myQMenuBar.addMenu('OHLC Interval')
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

        popupmsgAction = QtGui.QAction('Open', self)
        popupmsgAction.setStatusTip('Popup')
        popupmsgAction.triggered.connect(self.popupmsg)
#-----

        exchange2 = QtGui.QAction('BTC-E', self)
        exchange2.setStatusTip('BTC-E')
        exchange2.triggered.connect(self.btce)

        exchange1 = QtGui.QAction('BITFINEX', self)
        exchange1.setStatusTip('BITFINEX')
        exchange1.triggered.connect(self.bitfinex)

        exchange3 = QtGui.QAction('Bitstamp', self)
        exchange3.setStatusTip('bitstamp')
        exchange3.triggered.connect(self.bitstamp)

#_________
        tick = QtGui.QAction('Tick', self)
        tick.setStatusTip('Tick Data')
        tick.triggered.connect(self.btce)

        oned = QtGui.QAction('1 day', self)
        oned.setStatusTip('One Day')
        oned.triggered.connect(self.bitfinex)

        threed = QtGui.QAction('3 day', self)
        threed.setStatusTip('three day')
        threed.triggered.connect(self.bitstamp)

        sevend = QtGui.QAction('7 day', self)
        sevend.setStatusTip('seven day')
        sevend.triggered.connect(self.bitstamp)
#__________

        tick1 = QtGui.QAction('tick', self)
        tick1.setStatusTip('seven day')
        tick1.triggered.connect(self.bitstamp)

        onem = QtGui.QAction('1 minute', 0.0005,  self)
        onem.setStatusTip('seven day')
        onem.triggered.connect(self.bitstamp)


        fivem = QtGui.QAction('5 minute', 0.003, self)
        fivem.setStatusTip('seven day')
        fivem.triggered.connect(self.bitstamp)

        fifteenm = QtGui.QAction('15 minute', 0.008, self)
        fifteenm.setStatusTip('seven day')
        fifteenm.triggered.connect(self.bitstamp)

        thirtymin = QtGui.QAction('30 mins', 0.016, self)
        thirtymin.setStatusTip('seven day')
        thirtymin.triggered.connect(self.bitstamp)

        oneh = QtGui.QAction('1 hour', 0.032, self)
        oneh.setStatusTip('seven day')
        oneh.triggered.connect(self.bitstamp)

        threeh = QtGui.QAction('3 hour', 0.096, self)
        threeh.setStatusTip('seven day')
        threeh.triggered.connect(self.bitstamp)




        FileMenu.addAction(newAction)
        FileMenu.addAction(saveAction)
        FileMenu.addAction(openAction)
        FileMenu.addAction(exitAction)

        AboutMenu.addAction(popupmsgAction)

        exchangeChoice.addAction(exchange1)
        exchangeChoice.addAction(exchange2)
        exchangeChoice.addAction(exchange3)

        dataTF.addAction(tick)
        dataTF.addAction(oned)
        dataTF.addAction(threed)
        dataTF.addAction(sevend)

        OHLCI.addAction(tick1)
        OHLCI.addAction(onem)
        OHLCI.addAction(fivem)
        OHLCI.addAction(fifteenm)
        OHLCI.addAction(thirtymin)
        OHLCI.addAction(oneh)
        OHLCI.addAction(threeh)







#_________________________________________________________________________
#

#Canvas------------------

        self.canvas = FigureCanvas(f)
        self.canvas.show()
        self.show()








#_________________________________________________________________________
#(down starting from top, from left, continuing, how many rows it spas across)
        grid = QtGui.QGridLayout()

        grid.addWidget(self.canvas, 0, 0, 2, 4)




        self.setLayout(grid)
#_________________________________________________________________________




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


    def popupmsg(self):
        msg = QtGui.QMessageBox.question(self, "Error!",
                                         "Not supported just yet..",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:
            print("Exiting!!!!")
            sys.exit()
        else:
            pass

    def changeExchange(self, toWhat, pn):
        global exchange
        global DatCounter
        global programName

        exchange = toWhat
        programName=pn
        DatCounter=9000


    def btce(self):
        pass
    def bitfinex(self):
        pass
    def bitstamp(self):
        pass






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
    timer = QtCore.QTimer()
    timer.timeout.connect(animate)
    timer.start(1000)

#_____________________
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()
    #ani = animation.FuncAnimation(f, animate, interval=1000)
    sys.exit(app.exec_())
