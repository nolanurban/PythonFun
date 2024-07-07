import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

program_name = "Heather's Compensation Application"
program_run_button = "Run Compensation Script"
program_status_run = "Running"

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        # Set up the basic window
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle(program_name)
        self.init_ui()
    
    def init_ui(self):
        # this is where the window lives
        self.label = QtWidgets.QLabel(self)
        self.label.setText(program_name)
        self.label.move(50, 50)
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText(program_run_button)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText(program_status_run)
        self.label.update()
    def update(self):
        self.label.adjustSize("adjusted size")
def window():
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec_())

# run it
window()