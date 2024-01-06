#!/usr/bin/env python3


from PySide6.QtWidgets import QStackedWidget

from boite.tools.byte_converter.widget import Widget as ByteConverterWidget


class StackedWidget(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.addWidget(ByteConverterWidget())
