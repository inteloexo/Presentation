import sys
import os
from PyQt4 import QtGui, QtCore


class EntryGui(QtGui.QDialog):

    def __init__(self, date):
        super(EntryGui, self).__init__()
        self.date = date.toString()
        self.initUI()

    def return_clicked(self):
        text = self.textEdit.toPlainText()

        file = open(self.date + '.txt', 'w')
        file.write(text)
        file.close()

        self.close()

    def initUI(self):

        label = QtGui.QLabel("<b>"+self.date+"</b>")

        self.buffer = ''

        if os.path.exists(self.date + '.txt'):
            file = open(self.date + '.txt', 'r')
            self.buffer = file.read()
            file.close()

        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setText(self.buffer)

        returnButton = QtGui.QPushButton('Grįžti', self)
        returnButton.clicked.connect(self.return_clicked)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(label, 3, 0)
        grid.addWidget(self.textEdit, 3, 1, 5, 1)
        grid.addWidget(returnButton, 4, 0)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Dienoraštis")
        self.show()


class Gui(QtGui.QDialog):
    
    def __init__(self):
        super(Gui, self).__init__()
        self.initUI()

    def popup(self, date):
        self.dialog = EntryGui(date)

    def initUI(self):      

        self.text = QtGui.QLabel(self)
        self.text.setText('Pasirinkite norimą dieną:')
        self.text.move(20, 10)

        cal = QtGui.QCalendarWidget(self)
        cal.setFirstDayOfWeek(1)
        cal.setVerticalHeaderFormat(0)
        cal.setGridVisible(True)
        cal.move(20, 30)
        cal.clicked[QtCore.QDate].connect(self.popup)

        self.setGeometry(300, 300, 230, 220)
        self.setWindowTitle('Dienoraštis')
        self.setFixedSize(230, 220)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()