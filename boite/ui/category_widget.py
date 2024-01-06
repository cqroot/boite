#!/usr/bin/env python3

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QAbstractItemView, QListView

from boite.tools.tools import Tools


class CategoryWidget(QListView):
    def __init__(self):
        super().__init__()

        self.string_list_model = QStringListModel()
        self.string_list_model.setStringList(Tools.string_list())
        self.setModel(self.string_list_model)

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
