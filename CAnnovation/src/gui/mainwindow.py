# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Apr 23 17:47:26 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(265, 580)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.treeWidget)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.objectsTab = QtGui.QWidget()
        self.objectsTab.setObjectName(_fromUtf8("objectsTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.objectsTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.eggPool = QtGui.QListWidget(self.objectsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eggPool.sizePolicy().hasHeightForWidth())
        self.eggPool.setSizePolicy(sizePolicy)
        self.eggPool.setTabKeyNavigation(False)
        self.eggPool.setResizeMode(QtGui.QListView.Fixed)
        self.eggPool.setSpacing(0)
        self.eggPool.setViewMode(QtGui.QListView.ListMode)
        self.eggPool.setObjectName(_fromUtf8("eggPool"))
        self.verticalLayout_2.addWidget(self.eggPool)
        self.tabWidget.addTab(self.objectsTab, _fromUtf8(""))
        self.terrainsTab = QtGui.QWidget()
        self.terrainsTab.setObjectName(_fromUtf8("terrainsTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.terrainsTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.createTerrainButton = QtGui.QPushButton(self.terrainsTab)
        self.createTerrainButton.setObjectName(_fromUtf8("createTerrainButton"))
        self.horizontalLayout.addWidget(self.createTerrainButton)
        self.modifyTerrainButton = QtGui.QPushButton(self.terrainsTab)
        self.modifyTerrainButton.setObjectName(_fromUtf8("modifyTerrainButton"))
        self.horizontalLayout.addWidget(self.modifyTerrainButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.terrainPool = QtGui.QListWidget(self.terrainsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terrainPool.sizePolicy().hasHeightForWidth())
        self.terrainPool.setSizePolicy(sizePolicy)
        self.terrainPool.setTabKeyNavigation(False)
        self.terrainPool.setResizeMode(QtGui.QListView.Fixed)
        self.terrainPool.setSpacing(0)
        self.terrainPool.setViewMode(QtGui.QListView.ListMode)
        self.terrainPool.setObjectName(_fromUtf8("terrainPool"))
        self.verticalLayout_3.addWidget(self.terrainPool)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.terrainsTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuWorkspace = QtGui.QMenu(self.menubar)
        self.menuWorkspace.setObjectName(_fromUtf8("menuWorkspace"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuShaders = QtGui.QMenu(self.menubar)
        self.menuShaders.setObjectName(_fromUtf8("menuShaders"))
        MainWindow.setMenuBar(self.menubar)
        self.actionScene = QtGui.QAction(MainWindow)
        self.actionScene.setObjectName(_fromUtf8("actionScene"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionNew_2 = QtGui.QAction(MainWindow)
        self.actionNew_2.setObjectName(_fromUtf8("actionNew_2"))
        self.actionSave_Scene = QtGui.QAction(MainWindow)
        self.actionSave_Scene.setObjectName(_fromUtf8("actionSave_Scene"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionAdvanced_featues = QtGui.QAction(MainWindow)
        self.actionAdvanced_featues.setObjectName(_fromUtf8("actionAdvanced_featues"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionPPL = QtGui.QAction(MainWindow)
        self.actionPPL.setCheckable(True)
        self.actionPPL.setChecked(False)
        self.actionPPL.setObjectName(_fromUtf8("actionPPL"))
        self.actionToonShading = QtGui.QAction(MainWindow)
        self.actionToonShading.setCheckable(True)
        self.actionToonShading.setObjectName(_fromUtf8("actionToonShading"))
        self.actionAmbientOcclusion = QtGui.QAction(MainWindow)
        self.actionAmbientOcclusion.setCheckable(True)
        self.actionAmbientOcclusion.setObjectName(_fromUtf8("actionAmbientOcclusion"))
        self.menuFile.addAction(self.actionNew_2)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_Scene)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuWorkspace.addAction(self.actionRefresh)
        self.menuSettings.addAction(self.actionAdvanced_featues)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionAbout)
        self.menuShaders.addAction(self.actionPPL)
        self.menuShaders.addAction(self.actionToonShading)
        self.menuShaders.addAction(self.actionAmbientOcclusion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWorkspace.menuAction())
        self.menubar.addAction(self.menuShaders.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "P3D Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Lighting", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "add PointLight", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "add DirectionalLight", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "add Spotlight", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Modifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "use model as Brush", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.eggPool.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.objectsTab), QtGui.QApplication.translate("MainWindow", "Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.createTerrainButton.setText(QtGui.QApplication.translate("MainWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.modifyTerrainButton.setText(QtGui.QApplication.translate("MainWindow", "Modify", None, QtGui.QApplication.UnicodeUTF8))
        self.terrainPool.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.terrainsTab), QtGui.QApplication.translate("MainWindow", "Terrains", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWorkspace.setTitle(QtGui.QApplication.translate("MainWindow", "Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.menuShaders.setTitle(QtGui.QApplication.translate("MainWindow", "Shaders", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScene.setText(QtGui.QApplication.translate("MainWindow", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_2.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Scene.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdvanced_featues.setText(QtGui.QApplication.translate("MainWindow", "Visit website...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPPL.setText(QtGui.QApplication.translate("MainWindow", "PerPixel Lighting", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToonShading.setText(QtGui.QApplication.translate("MainWindow", "Toon Shading", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAmbientOcclusion.setText(QtGui.QApplication.translate("MainWindow", "Ambient Occlusion", None, QtGui.QApplication.UnicodeUTF8))
