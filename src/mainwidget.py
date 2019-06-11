from PyQt5.QtWidgets import QWidget, QGridLayout

from objectiveswidget import ObjectivesWidget, HelpObjectiveWidget
from planningwidget import PlanningWidget


class MainWidget(QWidget):
    def __init__(self, parent, username: str, token: str):
        QWidget.__init__(self, parent)
        self.__layout = QGridLayout()
        self.__obj_widget = ObjectivesWidget(self, username, token)
        self.__plan_widget = PlanningWidget(self, username, token)
        self.__help_widget = HelpObjectiveWidget(self)

        self.__conf_ui()

    def __conf_ui(self):
        self.setLayout(self.__layout)
        self.__layout.addWidget(self.__obj_widget, 0, 0)
        self.__layout.addWidget(self.__plan_widget, 0, 1, 2, 1)
        self.__layout.addWidget(self.__help_widget, 1, 0)


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys

    with open("../log.txt") as file:
        lines = file.readlines()
    app = QtWidgets.QApplication(sys.argv)
    thing = MainWidget(None, username=lines[0][:-1], token=lines[1][:-1])
    thing.show()
    sys.exit(app.exec_())
