from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QToolButton, QToolBar

class ToolBar:
    def initButtonToolBar(self, parent: QWidget = None) -> None:
        parent.button_cursor = ToolButtons(parent, "./icons/dark/cursor.png", "Cursor", parent.CursorAction)
        parent.button_move = ToolButtons(parent, "./icons/dark/move.png", "Move", parent.MoveAction)
        parent.button_edit = ToolButtons(parent, "./icons/dark/edit.png", "Edit", parent.EditAction)
        parent.button_duplicate = ToolButtons(parent, "./icons/dark/duplicate.png", "Duplicate", parent.DuplicateAction)
        parent.button_delete = ToolButtons(parent, "./icons/dark/delete.png", "Delete", parent.DeleteAction)

    def initToolBar(self, parent: QWidget = None) -> None:
        self.initButtonToolBar(parent)

        parent.toolbarBox = QToolBar("Меню", parent)
        parent.toolbarBox.setMovable(False)
        
        parent.toolbarBox.addWidget(parent.button_cursor)
        parent.toolbarBox.addWidget(parent.button_move)

        parent.toolbarBox.addSeparator()

        parent.toolbarBox.addWidget(parent.button_edit)
        parent.toolbarBox.addWidget(parent.button_duplicate)
        parent.toolbarBox.addWidget(parent.button_delete)
        parent.toolbarBox.addSeparator()
        parent.toolbar = parent.addToolBar(Qt.LeftToolBarArea, parent.toolbarBox)

class ToolButtons(QToolButton):
    minSize = (60, 60)

    def __init__(self, parent: QWidget = None, icon: str = None, text: str = None, action: any = None) -> None:
        super().__init__(parent)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        if text is not None: self.setText(text)
        if text is not None: self.setStatusTip(text)
        if text is not None: self.setToolTip(text)
        if text is not None: self.setToolTipDuration(3000)
        if icon is not None: self.setIcon(QIcon(icon))
        if action is not None: self.setDefaultAction(action)

    def minimumSizeHint(self) -> None:
        ms = super(ToolButtons, self).minimumSizeHint()
        w1, h1 = ms.width(), ms.height()
        w2, h2 = self.minSize
        self.minSize = max(w1, w2), max(h1, h2)
        return QSize(*self.minSize)