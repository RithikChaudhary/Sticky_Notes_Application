# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calenderwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calender(object):
    def setupUi(self, calender):
        calender.setObjectName("calender")
        calender.setFixedSize(492, 393)
        self.centralwidget = QtWidgets.QWidget(calender)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 491, 391))
        self.calendarWidget.setObjectName("calendarWidget")
        calender.setCentralWidget(self.centralwidget)

        self.retranslateUi(calender)
        QtCore.QMetaObject.connectSlotsByName(calender)

    def retranslateUi(self, calender):
        _translate = QtCore.QCoreApplication.translate
        calender.setWindowTitle(_translate("calender", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calender = QtWidgets.QMainWindow()
    ui = Ui_calender()
    ui.setupUi(calender)
    calender.show()
    sys.exit(app.exec_())
