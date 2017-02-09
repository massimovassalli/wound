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
        self.selectedItem = None

    def refreshTree(self):
        self.rebuilding = True
        self.ui.treeWidget.clear()
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
                    o.setText(0, p.filename)
                    #o.setForeground(0,QtGui.QColor(255,0,0,255))

            self.ui.treeWidget.addTopLevelItem(el)
        self.rebuilding = False

        #fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', './')

        #q = QtWidgets.QFileDialog()
        #q.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        #q.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        #progress = QtWidgets.QProgressDialog("Opening files...", "Cancel opening", 0, pmax)

    def selectElement(self,item):
        if self.rebuilding is True:
            return
        self.selectedItem = item
        self.ui.statusBar.showMessage('ITEM {} depth {}'.format(item.src.basename,item.src.depth))
        #self.ui.treeWidget.itemWidget()

    def expSave(self):
        filtered = QtWidgets.QFileDialog.getSaveFileName(self,caption='Save the experiment',filter='*.exp')
        if filtered[0] != '':
            filename = filtered[0]
            if filename[-4:] != '.exp':
                filename = filename + '.exp'
            self.exp.save(filename)

    def expLoad(self):
        selection = QtWidgets.QFileDialog.getOpenFileName  (self, caption='Select an experiment file',filter='*.exp')
        filename = selection[0]
        if not os.path.isfile(filename):
            return
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.exp = engine.load(filename)
        self.refreshTree()
        QtWidgets.QApplication.restoreOverrideCursor()

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

    def rewatch(self):
        self.watch()

    def watch(self,element=None):
        if self.rebuilding is True:
            return
        if element is None:
            element = self.selectedItem
        myelement = element.src
        if myelement.is_picture():
            QtWidgets.QApplication.setOverrideCursor( QtGui.QCursor(QtCore.Qt.WaitCursor))
            if self.ui.view_raw.isChecked():
                self.ui.pic.setPixmap( QtGui.QPixmap(myelement.dir) )
            elif self.ui.view_stored.isChecked():
                if myelement.isProcessed():
                    q = QtGui.QPixmap(myelement.dir)
                    q.setMask(QtGui.QBitmap(myelement.saveName))
                    self.ui.pic.setPixmap(q)
                else:
                    self.ui.pic.setPixmap(QtGui.QPixmap(myelement.dir))
            elif self.ui.view_otf.isChecked():
                myelement.process()
                q = QtGui.QPixmap(myelement.dir)
                q.setMask( QtGui.QBitmap(myelement.saveName))
                self.ui.pic.setPixmap(q)
            QtWidgets.QApplication.restoreOverrideCursor()

    def tpAdd(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a TimePoint directory', './')
        if not os.path.isdir(folder):
            return
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        tp = engine.timepoint()
        if tp.guess(folder):
            self.exp.append(tp)
            self.refreshTree()
            QtWidgets.QApplication.restoreOverrideCursor()
        else:
            QtWidgets.QApplication.restoreOverrideCursor()
            QtWidgets.QMessageBox.information(self, 'ERROR', 'The proposed directory could not be guessed as a TimePoint')

    def tpDel(self):
        tp = self.selectedItem.src
        if tp.is_timepoint():
            id = self.exp.index(tp)
            del(self.exp[id])
        self.refreshTree()

    def wellAdd(self):
        tp = self.selectedItem.src
        if tp.is_timepoint():
            folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a TimePoint directory', './')
            if not os.path.isdir(folder):
                return
            QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            well = engine.well()
            if well.guess(folder):
                tp.append(well)
                self.refreshTree()
                QtWidgets.QApplication.restoreOverrideCursor()
            else:
                QtWidgets.QApplication.restoreOverrideCursor()
                QtWidgets.QMessageBox.information(self, 'ERROR', 'The proposed directory could not be guessed as a Well')

    def wellDel(self):
        well = self.selectedItem.src
        if well.is_well():
            id = well.parent.index(well)
            del(well.parent[id])
        self.refreshTree()

    def picDel(self):
        pic = self.selectedItem.src
        if pic.is_picture():
            id = pic.parent.index(pic)
            del (pic.parent[id])
        self.refreshTree()

    def picAdd(self):
        tp = self.selectedItem.src
        if tp.is_well():
            selection = QtWidgets.QFileDialog.getOpenFileName(self, caption='Select a Picture', filter='*.*')
            filename = selection[0]
            if not os.path.isfile(filename):
                return
            QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            pic = engine.picture()
            if pic.guess(filename):
                tp.append(pic)
                self.refreshTree()
                QtWidgets.QApplication.restoreOverrideCursor()
            else:
                QtWidgets.QApplication.restoreOverrideCursor()
                QtWidgets.QMessageBox.information(self, 'ERROR', 'The proposed directory could not be guessed as a Well')

    def setConnections(self):
        
        #clickable1=[self.ui.radio_view,self.ui.radio_deriv,self.ui.radio_smooth]
        #editable =[self.ui.derorder,self.ui.s_mth,self.ui.s_vth,self.ui.sg_fw,self.ui.sg_mm,self.ui.plath,self.ui.lasth]
        #for o in clickable1:
        #    o.clicked.connect(self.refreshCurve)
        #for o in editable:
        #    o.editingFinished.connect(self.updateCurve)
        #    o.valueChanged.connect(self.reddish)

        self.ui.actionGuess.triggered.connect(self.expGuess)
        self.ui.actionLoad.triggered.connect(self.expLoad)
        self.ui.actionSave.triggered.connect(self.expSave)
        self.ui.treeWidget.currentItemChanged.connect(self.selectElement)

        self.ui.actionAdd.triggered.connect(self.tpAdd)
        self.ui.actionRemove.triggered.connect(self.tpDel)
        self.ui.actionAddWell.triggered.connect(self.wellAdd)
        self.ui.actionRemoveWell.triggered.connect(self.wellDel)
        self.ui.actionAddPic.triggered.connect(self.picAdd)
        self.ui.actionRemovePic.triggered.connect(self.picDel)

        self.ui.treeWidget.currentItemChanged.connect(self.watch)
        self.ui.view_stored.clicked.connect(self.rewatch)
        self.ui.view_raw.clicked.connect(self.rewatch)
        self.ui.view_otf.clicked.connect(self.rewatch)


        QtCore.QMetaObject.connectSlotsByName(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName( 'Scratch assay Wizard' )
    canale = woundWindow()
    canale.show()
    #QtCore.QObject.connect( app, QtCore.SIGNAL( 'lastWindowClosed()' ), app, QtCore.SLOT( 'quit()' ) )
    sys.exit(app.exec_())
