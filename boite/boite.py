#!/usr/bin/env python3

import sys
from PySide6.QtWidgets import QApplication, QSplitter, QVBoxLayout, QWidget

from boite.ui.category_widget import CategoryWidget
from boite.ui.stacked_widget import StackedWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_components()

    def init_components(self):
        self.splitter = QSplitter()
        self.splitter.addWidget(CategoryWidget())
        self.splitter.addWidget(StackedWidget())
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 4)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.splitter)


def main():
    app = QApplication([])

    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
