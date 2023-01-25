from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
import sys

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('calc.ui', self)

        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)
        self.div.clicked.connect(self.div_num)
        self.mult.clicked.connect(self.mult_num)

        

    def add_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        self.result.setText(str(int(num1) + int(num2)))

    def sub_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        self.result.setText(str(int(num1) - int(num2)))
    
    def mult_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        self.result.setText(str(int(num1) * int(num2)))
        
    def div_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        try:
            self.result.setText(str(int(num1) / int(num2)))
        except ZeroDivisionError:
            self.result.setText("не делится")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()