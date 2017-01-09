from PyQt5 import QtCore, QtGui, QtWidgets

_fromUtf8 = lambda s: s

import sys,os
import wound_view as view
import engine


class woundWindow ( QtWidgets.QMainWindow ):
    def __init__ ( self, parent = None ):
        QtWidgets.QMainWindow.__init__( self, parent )
        self.setWindowTitle( 'Scratch Test Wizard' )
        self.ui = view.Ui_facewindow()
        self.ui.setupUi( self )
        self.setConnections()
        self.rebuilding = False

    def refreshTree(self):
        self.rebuilding = True
        for i in range(len(self.exp)):
            el = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
            el.src= self.exp[i]
            if self.exp[i].time is None:
                tm = 'T{}'.format(i)
            else:
                tm = self.exp[i].time
            el.setText(0,tm)

            for w in self.exp[i]:
                e = QtWidgets.QTreeWidgetItem(el)
                e.src = w
                e.setText(0,w.basename)
                #e.setBackground(0,QtGui.QColor(255, 0, 0, 127))

                n=1
                for p in w:
                    o = QtWidgets.QTreeWidgetItem(e)
                    o.src = p
                    o.setText(0, p.basename)
                    #o.setForeground(0,QtGui.QColor(255,0,0,255))

            self.ui.treeWidget.addTopLevelItem(el)
            self.rebuilding = False

        #fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', './')

        #q = QtWidgets.QFileDialog()
        #q.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        #q.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        #progress = QtWidgets.QProgressDialog("Opening files...", "Cancel opening", 0, pmax)


    def expGuess(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory', './')
        if not os.path.isdir(folder):
            return
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        exp = engine.exp()
        if exp.guess(folder):
            self.exp = exp
            self.refreshTree()
            QtWidgets.QApplication.restoreOverrideCursor()
        else:
            QtWidgets.QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, 'ERROR', 'The proposed directory could not be guessed as an experiment')

    def watch(self,element):
        if self.rebuilding is True:
            return
        myelement = element.src
        if myelement.is_picture():
            self.ui.pic.setPixmap( QtGui.QPixmap(myelement.dir) )


    def setConnections(self):
        
        #clickable1=[self.ui.radio_view,self.ui.radio_deriv,self.ui.radio_smooth]
        #editable =[self.ui.derorder,self.ui.s_mth,self.ui.s_vth,self.ui.sg_fw,self.ui.sg_mm,self.ui.plath,self.ui.lasth]
        #for o in clickable1:
        #    o.clicked.connect(self.refreshCurve)
        #for o in editable:
        #    o.editingFinished.connect(self.updateCurve)
        #    o.valueChanged.connect(self.reddish)

        self.ui.actionGuess.triggered.connect(self.expGuess)

        self.ui.treeWidget.currentItemChanged.connect(self.watch)

        QtCore.QMetaObject.connectSlotsByName(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName( 'Scratch assay Wizard' )
    canale = woundWindow()
    canale.show()
    #QtCore.QObject.connect( app, QtCore.SIGNAL( 'lastWindowClosed()' ), app, QtCore.SLOT( 'quit()' ) )
    sys.exit(app.exec_())
