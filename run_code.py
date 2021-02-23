"""
The files main_ui.py, intro.py, pop.py and cal.py need to be in the same directory
for the following python file to execute properly
"""

import sys
import webbrowser
from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow
from intro import Ui_HelpWindow
from pop import Ui_pop_windows
from cal import Ui_calender


class IntroWindow(QtWidgets.QMainWindow, Ui_HelpWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(IntroWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class CalenderWindow(QtWidgets.QMainWindow, Ui_calender):
    def __init__(self, *args, obj=None, **kwargs):
        super(CalenderWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class PopUpWindow(QtWidgets.QMainWindow, Ui_pop_windows):
    def __init__(self, *args, obj=None, **kwargs):
        super(PopUpWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

# The buttons "Save", "Save as" and "Clear" are connected to function within
# the pop file within this directory. The associated functions are also defined
# within that window.

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.all_buttons()

    def all_buttons(self):
        self.pushButton.clicked.connect(self.intro_window)
        self.pushButton_3.clicked.connect(self.helps)
        self.pushButton_5.clicked.connect(self.learn)
        self.pushButton_4.clicked.connect(self.calender_win)
        self.pushButton_6.clicked.connect(self.works)
        self.pushButton_7.clicked.connect(self.new_window)
        self.pushButton_8.clicked.connect(self.new_window_1)
        self.pushButton_9.clicked.connect(self.new_window_2)
        self.pushButton_10.clicked.connect(self.new_window_3)
        self.pushButton_11.clicked.connect(self.new_window_4)


    def learn(self):
        webbrowser.open('https://learn.uwaterloo.ca/')

    def works(self):
        webbrowser.open('http://waterlooworks.uwaterloo.ca/')

    def helps(self):
        webbrowser.open('https://uwaterloo.ca/')

    def new_window(self, v):
        self.window = QtWidgets.QMainWindow()
        self.label_text_1 = self.v
        self.ui = Ui_pop_windows(self.label_text_1)

        self.ui.setupUi(self.window)
        self.window.show()

    def new_window_1(self, w):
        self.window = QtWidgets.QMainWindow()

        self.label_text_2 = self.w
        self.ui = Ui_pop_windows(self.label_text_2)

        self.ui.setupUi(self.window)
        self.window.show()

    def new_window_2(self, x):
        self.window = QtWidgets.QMainWindow()

        self.label_text_3 = self.x
        self.ui = Ui_pop_windows(self.label_text_3)

        self.ui.setupUi(self.window)
        self.window.show()

    def new_window_3(self, y):
        self.window = QtWidgets.QMainWindow()

        self.label_text_4 = self.y
        self.ui = Ui_pop_windows(self.label_text_4)

        self.ui.setupUi(self.window)
        self.window.show()

    def new_window_4(self, z):
        self.window = QtWidgets.QMainWindow()

        self.label_text_5 = self.z
        self.ui = Ui_pop_windows(self.label_text_5)

        self.ui.setupUi(self.window)
        self.window.show()

    def calender_win(self):
        self.calwin = QtWidgets.QMainWindow()
        self.ui = Ui_calender()
        self.ui.setupUi(self.calwin)
        self.calwin.show()

    def intro_window(self):
        self.intro_win = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.intro_win)
        self.intro_win.show()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
