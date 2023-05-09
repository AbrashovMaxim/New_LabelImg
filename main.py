from typing import Any
from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QPoint, Qt, QSize
from PyQt5.QtGui import QPainter, QBrush, QColor, QIcon, QCursor, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QLabel, QAction, QToolBar, QMenuBar, QToolButton, QButtonGroup

from libs.nli_action import Actions
from libs.nli_menubar import MenuBar
from libs.nli_toolbar import ToolBar
from libs.nli_dockbar import DockBar
from libs.nli_central_widget import CentralWidget

from libs.nli_events_buttons import Events_ToolButtons


class StatusBar:
    def initStatusBar(self, parent) -> None:
        status = parent.statusBar()
        status.setSizeGripEnabled(True)

class Window(QMainWindow):
    global app

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        CentralWidget().initCentralWidget(self)
        Actions().initActions(self, app)
        MenuBar().initMenuBar(self)
        ToolBar().initToolBar(self)
        DockBar().initDockBar(self)
        StatusBar().initStatusBar(self)

        self.setGeometry(200, 200, 1000, 800)
        self.setWindowTitle('New LableImg')
    

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,30,600,400)
        self.begin = QPoint()
        self.end = QPoint()
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40))  
        qp.setBrush(br)   
        qp.drawRect(QRect(self.begin, self.end))       

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.update()

if __name__ == '__main__':
    app = QApplication([])

    w = Window()
    w.show()
    app.exec_()