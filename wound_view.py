# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wound_view.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_facewindow(object):
    def setupUi(self, facewindow):
        facewindow.setObjectName("facewindow")
        facewindow.resize(848, 565)
        facewindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("wound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        facewindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(facewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Expriment tree")
        self.horizontalLayout_4.addWidget(self.treeWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.view_raw = QtWidgets.QRadioButton(self.groupBox)
        self.view_raw.setObjectName("view_raw")
        self.horizontalLayout_2.addWidget(self.view_raw)
        self.view_stored = QtWidgets.QRadioButton(self.groupBox)
        self.view_stored.setChecked(True)
        self.view_stored.setObjectName("view_stored")
        self.horizontalLayout_2.addWidget(self.view_stored)
        self.view_otf = QtWidgets.QRadioButton(self.groupBox)
        self.view_otf.setObjectName("view_otf")
        self.horizontalLayout_2.addWidget(self.view_otf)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cannysigma = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.cannysigma.setDecimals(2)
        self.cannysigma.setSingleStep(0.1)
        self.cannysigma.setProperty("value", 2.0)
        self.cannysigma.setObjectName("cannysigma")
        self.horizontalLayout.addWidget(self.cannysigma)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.minholes = QtWidgets.QSpinBox(self.groupBox_2)
        self.minholes.setMinimum(1)
        self.minholes.setMaximum(9999)
        self.minholes.setProperty("value", 256)
        self.minholes.setObjectName("minholes")
        self.horizontalLayout.addWidget(self.minholes)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.minobj = QtWidgets.QSpinBox(self.groupBox_2)
        self.minobj.setMinimum(1)
        self.minobj.setMaximum(999)
        self.minobj.setProperty("value", 64)
        self.minobj.setObjectName("minobj")
        self.horizontalLayout.addWidget(self.minobj)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pic = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic.sizePolicy().hasHeightForWidth())
        self.pic.setSizePolicy(sizePolicy)
        self.pic.setMinimumSize(QtCore.QSize(128, 96))
        self.pic.setBaseSize(QtCore.QSize(0, 0))
        self.pic.setStyleSheet("background-color: gray;")
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("../../../VCCRI/Cell migration assay/Stitching/Eleventh Plate - GFP_hP1 stable line +- mBcd (wells 4-5-6) p.26/Day1/Well 1 - Day1/15161743.png"))
        self.pic.setScaledContents(True)
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.pic.setObjectName("pic")
        self.verticalLayout.addWidget(self.pic)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        facewindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(facewindow)
        self.statusBar.setObjectName("statusBar")
        facewindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(facewindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 848, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuExperiment = QtWidgets.QMenu(self.menuBar)
        self.menuExperiment.setObjectName("menuExperiment")
        self.menuTimepoint = QtWidgets.QMenu(self.menuBar)
        self.menuTimepoint.setObjectName("menuTimepoint")
        self.menuWell = QtWidgets.QMenu(self.menuBar)
        self.menuWell.setObjectName("menuWell")
        self.menuPicture = QtWidgets.QMenu(self.menuBar)
        self.menuPicture.setObjectName("menuPicture")
        facewindow.setMenuBar(self.menuBar)
        self.actionLoad = QtWidgets.QAction(facewindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(facewindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAdd = QtWidgets.QAction(facewindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(facewindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionAddWell = QtWidgets.QAction(facewindow)
        self.actionAddWell.setObjectName("actionAddWell")
        self.actionRemoveWell = QtWidgets.QAction(facewindow)
        self.actionRemoveWell.setObjectName("actionRemoveWell")
        self.actionAddPic = QtWidgets.QAction(facewindow)
        self.actionAddPic.setObjectName("actionAddPic")
        self.actionRemovePic = QtWidgets.QAction(facewindow)
        self.actionRemovePic.setObjectName("actionRemovePic")
        self.actionProcess = QtWidgets.QAction(facewindow)
        self.actionProcess.setEnabled(False)
        self.actionProcess.setObjectName("actionProcess")
        self.actionStitch = QtWidgets.QAction(facewindow)
        self.actionStitch.setEnabled(False)
        self.actionStitch.setObjectName("actionStitch")
        self.actionGuess = QtWidgets.QAction(facewindow)
        self.actionGuess.setObjectName("actionGuess")
        self.menuExperiment.addAction(self.actionLoad)
        self.menuExperiment.addAction(self.actionSave)
        self.menuExperiment.addAction(self.actionGuess)
        self.menuTimepoint.addAction(self.actionAdd)
        self.menuTimepoint.addAction(self.actionRemove)
        self.menuWell.addAction(self.actionAddWell)
        self.menuWell.addAction(self.actionRemoveWell)
        self.menuWell.addAction(self.actionProcess)
        self.menuWell.addAction(self.actionStitch)
        self.menuPicture.addAction(self.actionAddPic)
        self.menuPicture.addAction(self.actionRemovePic)
        self.menuBar.addAction(self.menuExperiment.menuAction())
        self.menuBar.addAction(self.menuTimepoint.menuAction())
        self.menuBar.addAction(self.menuWell.menuAction())
        self.menuBar.addAction(self.menuPicture.menuAction())

        self.retranslateUi(facewindow)
        QtCore.QMetaObject.connectSlotsByName(facewindow)

    def retranslateUi(self, facewindow):
        _translate = QtCore.QCoreApplication.translate
        facewindow.setWindowTitle(_translate("facewindow", "MainWindow"))
        self.groupBox.setTitle(_translate("facewindow", "View"))
        self.view_raw.setText(_translate("facewindow", "raw"))
        self.view_stored.setText(_translate("facewindow", "stored"))
        self.view_otf.setText(_translate("facewindow", "on the fly"))
        self.groupBox_2.setTitle(_translate("facewindow", "Segmentation"))
        self.label.setText(_translate("facewindow", "Sensitivity"))
        self.label_2.setText(_translate("facewindow", "Holes"))
        self.label_3.setText(_translate("facewindow", "Cells"))
        self.menuExperiment.setTitle(_translate("facewindow", "Experiment"))
        self.menuTimepoint.setTitle(_translate("facewindow", "Timepoint"))
        self.menuWell.setTitle(_translate("facewindow", "Well"))
        self.menuPicture.setTitle(_translate("facewindow", "Picture"))
        self.actionLoad.setText(_translate("facewindow", "Load"))
        self.actionSave.setText(_translate("facewindow", "Save"))
        self.actionAdd.setText(_translate("facewindow", "Add"))
        self.actionRemove.setText(_translate("facewindow", "Remove"))
        self.actionAddWell.setText(_translate("facewindow", "Add"))
        self.actionRemoveWell.setText(_translate("facewindow", "Remove"))
        self.actionAddPic.setText(_translate("facewindow", "Add"))
        self.actionRemovePic.setText(_translate("facewindow", "Remove"))
        self.actionProcess.setText(_translate("facewindow", "Process"))
        self.actionStitch.setText(_translate("facewindow", "Stitch"))
        self.actionGuess.setText(_translate("facewindow", "Guess"))

