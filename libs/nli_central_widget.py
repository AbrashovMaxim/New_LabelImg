from PyQt5.QtWidgets import QWidget

class CentralWidget:
    def initCentralWidget(self, parent: QWidget = None) -> None:
        parent.centralWidget = QWidget(parent)
        parent.setCentralWidget(parent.centralWidget)