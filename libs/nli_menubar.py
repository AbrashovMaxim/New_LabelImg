from PyQt5.QtWidgets import QWidget

class MenuBar:
    def initMenuBar(self, parent: QWidget = None) -> None:
        menubar = parent.menuBar()
        # ************************* File *************************
        parent.fileMenu = menubar.addMenu('&File')
        
        parent.fileMenu.addAction(parent.SaveAction)
        parent.fileMenu.addAction(parent.SaveAsAction)

        parent.fileMenu.addAction(parent.OpenAction)
        parent.fileMenu.addAction(parent.OpenFolderAction)

        parent.fileMenu.addAction(parent.ImportAction)
        parent.fileMenu.addAction(parent.ExportAction)

        parent.fileMenu.addAction(parent.ExitAction)
        # ********************* Instruments *********************
        parent.instrumentsMenu = menubar.addMenu('&Instruments')
        parent.instrumentsMenu.addAction(parent.CursorAction)
        parent.instrumentsMenu.addAction(parent.MoveAction)

        parent.instrumentsMenu.addAction(parent.EditAction)
        parent.instrumentsMenu.addAction(parent.DuplicateAction)
        parent.instrumentsMenu.addAction(parent.DeleteAction)

        # ********************** Settings **********************
        parent.settingsMenu = menubar.addMenu('&Settings')