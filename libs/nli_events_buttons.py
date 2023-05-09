from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWidget

class Events_ToolButtons:
    def change_cursor(self, app: QApplication = None, cursor: QCursor = None) -> None:
        if cursor == Qt.ArrowCursor: app.restoreOverrideCursor()
        else: app.setOverrideCursor(cursor)
