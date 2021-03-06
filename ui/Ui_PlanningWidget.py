# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/PlanningWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_PlanningWidget(object):
    def setupUi(self, PlanningWidget):
        PlanningWidget.setObjectName("PlanningWidget")
        PlanningWidget.resize(250, 282)
        PlanningWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(PlanningWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_arrow_button = QtWidgets.QToolButton(PlanningWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_arrow_button.sizePolicy().hasHeightForWidth())
        self.left_arrow_button.setSizePolicy(sizePolicy)
        self.left_arrow_button.setMinimumSize(QtCore.QSize(30, 30))
        self.left_arrow_button.setAutoRaise(True)
        self.left_arrow_button.setArrowType(QtCore.Qt.LeftArrow)
        self.left_arrow_button.setObjectName("left_arrow_button")
        self.horizontalLayout.addWidget(self.left_arrow_button)
        self.date_lbl = QtWidgets.QLabel(PlanningWidget)
        self.date_lbl.setMinimumSize(QtCore.QSize(35, 35))
        self.date_lbl.setWhatsThis("")
        self.date_lbl.setObjectName("date_lbl")
        self.horizontalLayout.addWidget(self.date_lbl, 0, QtCore.Qt.AlignHCenter)
        self.right_arrow_button = QtWidgets.QToolButton(PlanningWidget)
        self.right_arrow_button.setMinimumSize(QtCore.QSize(30, 30))
        self.right_arrow_button.setAutoRaise(True)
        self.right_arrow_button.setArrowType(QtCore.Qt.RightArrow)
        self.right_arrow_button.setObjectName("right_arrow_button")
        self.horizontalLayout.addWidget(self.right_arrow_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(PlanningWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.events_layout = QtWidgets.QVBoxLayout()
        self.events_layout.setObjectName("events_layout")
        self.verticalLayout.addLayout(self.events_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(PlanningWidget)
        QtCore.QMetaObject.connectSlotsByName(PlanningWidget)

    def retranslateUi(self, PlanningWidget):
        _translate = QtCore.QCoreApplication.translate
        PlanningWidget.setWindowTitle(_translate("PlanningWidget", "Form"))
        self.left_arrow_button.setText(_translate("PlanningWidget", "..."))
        self.left_arrow_button.setShortcut(_translate("PlanningWidget", "Left"))
        self.date_lbl.setText(_translate("PlanningWidget", "Today"))
        self.right_arrow_button.setText(_translate("PlanningWidget", "..."))
        self.right_arrow_button.setShortcut(_translate("PlanningWidget", "Right"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlanningWidget = QtWidgets.QWidget()
    ui = Ui_PlanningWidget()
    ui.setupUi(PlanningWidget)
    PlanningWidget.show()
    sys.exit(app.exec_())
