from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, qApp, QAction, QActionGroup
from libs.nli_events_buttons import Events_ToolButtons

class Actions:
    def initActions(self, parent: QWidget = None, app: QApplication = None) -> None:
        parent.ActionGroup = QActionGroup(parent)

        parent.CursorAction = Action(parent, './icons/dark/cursor.png', '&Cursor', 'Ctrl+T', 'Select box', lambda e: Events_ToolButtons().change_cursor(app, Qt.ArrowCursor), True)
        parent.CursorAction.setChecked(True)
        parent.MoveAction = Action(parent, './icons/dark/move.png', '&Move', 'Ctrl+M', 'Move box', lambda e: Events_ToolButtons().change_cursor(app, Qt.SizeAllCursor), True)

        parent.EditAction = Action(parent, './icons/dark/edit.png', '&Edit', 'Ctrl+D', 'Edit box', None, True)
        parent.DuplicateAction = Action(parent, './icons/dark/duplicate.png', '&Duplicate', 'Ctrl+B', 'Duplicate box', None, True)
        parent.DeleteAction = Action(parent, './icons/dark/delete.png', '&Delete', 'Ctrl+Delete', 'Delete box', None, True)

        parent.SaveAction = Action(parent, './icons/dark/save.png', '&Save', 'Ctrl+S', 'Save current image')
        parent.SaveAsAction = Action(parent, './icons/dark/save.png', '&Save as', 'Ctrl+Shift+S', 'Save as current image')

        parent.OpenAction = Action(parent, './icons/dark/folder.png', '&Open', 'Ctrl+O', 'Open image')
        parent.OpenFolderAction = Action(parent, './icons/dark/folder.png', '&Open folder', 'Ctrl+Shift+O', 'Open folder images')

        parent.ImportAction = Action(parent, './icons/dark/import.png', '&Import', 'Ctrl+I', 'Import classes')
        parent.ExportAction = Action(parent, './icons/dark/export.png', '&Export', 'Ctrl+E', 'Export classes')

        parent.ExitAction = Action(parent, './icons/dark/exit.png', '&Exit', 'Ctrl+Q', 'Exit application', qApp.quit)


class Action(QAction):

    def __init__(self, parent: QWidget = None, icon: str = None, text: str = None, shortcut: str = None, tooltip: str = None, event: any = None, tools: bool = False) -> None:
        super().__init__(parent)
        if text is not None: self.setIcon(QIcon(icon))
        if text is not None and icon is not None: self.setText(text)
        if shortcut is not None: self.setShortcut(shortcut)
        if tooltip is not None: self.setToolTip(tooltip); self.setStatusTip(tooltip)
        if event is not None: self.triggered.connect(event)
        if tools: self.setCheckable(True)

        parent.ActionGroup.addAction(self)