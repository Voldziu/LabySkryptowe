from PySide6.QtGui import QStandardItemModel, QStandardItem
from regexes import log_date_regex
from datetime import datetime
from PySide6.QtCore import Qt


def load_logs(path, model):
    model.clear()
    with open(path, 'r') as file:
        for line in file:
            item = QStandardItem(line)
            date_match = log_date_regex.search(line)
            if date_match:
                date_str = date_match.group(1)
                date_obj = datetime.strptime(date_str, "%d/%b/%Y")
                item.setData(date_obj, Qt.UserRole + 1)

            model.appendRow(item)

