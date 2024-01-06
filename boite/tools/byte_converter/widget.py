#!/usr/bin/env python3


from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.current_num = 0
        self.is_updating = False

        self.init_components()
        self.init_inputs()

    def init_components(self):
        self.form_layout = QFormLayout()

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)

        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.clear_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.form_layout)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addStretch()

        self.setLayout(self.main_layout)

    def init_inputs(self):
        double_validator = QDoubleValidator()

        self.inputs = {
            "bit": {
                "label": "bit (b):",
                "widget": QLineEdit("0"),
                "base": 8796093022208,
                "func": self.update_for_bit,
            },
            "byte": {
                "label": "byte (B):",
                "widget": QLineEdit("0"),
                "base": 1099511627776,
                "func": self.update_for_byte,
            },
            "kilobyte": {
                "label": "kilobyte (kB):",
                "widget": QLineEdit("0"),
                "base": 1073741824,
                "func": self.update_for_kilobyte,
            },
            "megabyte": {
                "label": "megabyte (MB):",
                "widget": QLineEdit("0"),
                "base": 1048576,
                "func": self.update_for_megabyte,
            },
            "gigabyte": {
                "label": "gigabyte (GB):",
                "widget": QLineEdit("0"),
                "base": 1024,
                "func": self.update_for_gigabyte,
            },
            "terabyte": {
                "label": "terabyte (TB):",
                "widget": QLineEdit("0"),
                "base": 1,
                "func": self.update_for_terabyte,
            },
        }

        for _, input in self.inputs.items():
            input["widget"].setValidator(double_validator)
            input["widget"].textChanged.connect(input["func"])
            self.form_layout.addRow(input["label"], input["widget"])

    def update(self, text, base):
        if self.is_updating == True:
            return
        self.is_updating = True
        print(float(text))
        print(float(text) / base)
        print()
        for _, input in self.inputs.items():
            input["widget"].setText("{:g}".format(float(text) / base * input["base"]))
        self.is_updating = False

    def update_for_bit(self, text):
        self.update(text, 8796093022208)

    def update_for_byte(self, text):
        self.update(text, 1099511627776)

    def update_for_kilobyte(self, text):
        self.update(text, 1073741824)

    def update_for_megabyte(self, text):
        self.update(text, 1048576)

    def update_for_gigabyte(self, text):
        self.update(text, 1024)

    def update_for_terabyte(self, text):
        self.update(text, 1)

    def clear(self):
        for _, input in self.inputs.items():
            self.is_updating = True
            input["widget"].setText("0")
            self.is_updating = False
