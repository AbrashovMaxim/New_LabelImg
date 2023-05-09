from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDockWidget, QVBoxLayout, QListWidget

class DockBar:
    def initDockBar(self, parent: QWidget = None) -> None:
        parent.dockBarBox = DockWidget(parent = parent, feature = QDockWidget.NoDockWidgetFeatures)
        parent.dockBarBox.setFloating(False)

        parent.addDockWidget(Qt.RightDockWidgetArea, parent.dockBarBox)

        test = QWidget(parent)
        parent.dockBarBox.setWidget(test)
        test.setLayout(QVBoxLayout())

        one = DockWidget(text = "Все классы", feature = QDockWidget.NoDockWidgetFeatures)
        two = DockWidget(text = "Слои", feature = QDockWidget.NoDockWidgetFeatures)
        three = DockWidget(text = "Файлы", feature = QDockWidget.NoDockWidgetFeatures)

        test.layout().addWidget(one)
        test.layout().addWidget(two)
        test.layout().addWidget(three)

class DockWidget(QDockWidget):
    def __init__(self, text: str = None, parent: QWidget = None, feature: any = None) -> None:
        super().__init__(text, parent)
        self.setFeatures(feature)
