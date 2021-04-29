from PyQt5.QtCore import Qt
from PyQt5.QtGui import*

from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QLineEdit)


calc_app = QApplication([])
calc_main_win = QWidget()
calc_main_win.setWindowTitle("Калькулятор")
calc_main_win.resize(500,500)
calc_main_win.setStyleSheet('QWidget {background-color: #202040; }')
#поле ввода
line_input = QLineEdit() 
line_input.setAlignment(Qt.AlignRight)
line_input.setFont(QFont("Arial",20))
line_input.setStyleSheet('QLineEdit { background-color: white; color: #ffbd69; font-weight: bold}')

#создаем групбокс для цифр
numeral_group = QGroupBox("")
btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
btn4 = QPushButton("4")
btn5 = QPushButton("5")
btn6 = QPushButton("6")
btn9 = QPushButton("9")
btnzero = QPushButton("0")
btn7 = QPushButton("7")
btn8 = QPushButton("8")


ng_line1 = QHBoxLayout()
ng_line2 = QHBoxLayout()
ng_line3 = QHBoxLayout()
ng_line4 = QHBoxLayout()
ng_main_line = QVBoxLayout()

ng_line1.addWidget(btn1)
ng_line1.addWidget(btn2)
ng_line1.addWidget(btn3)

ng_line2.addWidget(btn4)
ng_line2.addWidget(btn5)
ng_line2.addWidget(btn6)

ng_line3.addWidget(btn7)
ng_line3.addWidget(btn8)
ng_line3.addWidget(btn9)

ng_line4.addWidget(btnzero)

ng_main_line.addLayout(ng_line1)
ng_main_line.addLayout(ng_line2)
ng_main_line.addLayout(ng_line3)
ng_main_line.addLayout(ng_line4)

numeral_group.setLayout(ng_main_line)

#закончили рисовать кнопки для цифр

btn_op1 = QPushButton("*")
btn_op2 = QPushButton("+")
btn_op3 = QPushButton("-")
btn_op4 = QPushButton("/")
btn_op5 = QPushButton("=")
btn_op6 = QPushButton("С")


op_line = QVBoxLayout()
op_line.addWidget(btn_op1)
op_line.addWidget(btn_op2)
op_line.addWidget(btn_op3)
op_line.addWidget(btn_op4)
op_line.addWidget(btn_op5)
op_line.addWidget(btn_op6)


main_layout1 = QVBoxLayout()
main_layout2 = QHBoxLayout()

main_layout1.addWidget(line_input)
main_layout1.addWidget(numeral_group)

main_layout2.addLayout(main_layout1)
main_layout2.addLayout(op_line)

calc_main_win.setLayout(main_layout2)
calc_main_win.show()

# задаем стили для кнопок
btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btnzero, btn_op1, btn_op2, btn_op3, btn_op4, btn_op5, btn_op6]
for b in btn_list:
    b.setStyleSheet('QPushButton {background-color:#543864; color: #ffbd69;  font-weight: bold; height:30px; width:20px; font-size:20px;}')

'''Функционал приложения'''

def but1_click():
    old_value = line_input.displayText() 
    new_value = old_value + "1"   
    line_input.setText(new_value)

def but2_click():
    old_value = line_input.displayText() 
    new_value = old_value + "2"   
    line_input.setText(new_value)    
    
def but3_click():
    old_value = line_input.displayText() 
    new_value = old_value + "3"   
    line_input.setText(new_value)

def but4_click():
    old_value = line_input.displayText() 
    new_value = old_value + "4"   
    line_input.setText(new_value)

def but5_click():
    old_value = line_input.displayText() 
    new_value = old_value + "5"   
    line_input.setText(new_value)

def but6_click():
    old_value = line_input.displayText() 
    new_value = old_value + "6"   
    line_input.setText(new_value)

def but7_click():
    old_value = line_input.displayText() 
    new_value = old_value + "7"   
    line_input.setText(new_value)

def but8_click():
    old_value = line_input.displayText() 
    new_value = old_value + "8"   
    line_input.setText(new_value)

def but9_click():
    old_value = line_input.displayText() 
    new_value = old_value + "9"   
    line_input.setText(new_value)

def but_zero_click():
    old_value = line_input.displayText() 
    new_value = old_value + "0"   
    line_input.setText(new_value)

global first_value

def btn_op1_click():#операция умножения
    global first_value
    first_value = line_input.displayText()
    line_input.setText(first_value + "*")

def btn_op2_click():#операция умножения
    global first_value
    first_value = line_input.displayText()
    line_input.setText(first_value + "+")

def btn_op3_click():#операция умножения
    global first_value
    first_value = line_input.displayText()
    line_input.setText(first_value + "-")

def btn_op4_click():#операция умножения
    global first_value
    first_value = line_input.displayText()
    line_input.setText(first_value + "/")


def line_input_clear():
    line_input.clear()

def btn_op5_click():#кнопка равно
    global first_value
    
    total_value = line_input.displayText()
    find_op = total_value.find("*")
    find_op = total_value.find("-")
    find_op = total_value.find("+")
    find_op = total_value.find("/")

    if "/" in total_value:
        find_op_value = total_value[find_op]
        second_value = total_value[find_op+1:len(total_value)]
    else:
        find_op_value = total_value[find_op-1]
        second_value = total_value[find_op:len(total_value)] 

    print(find_op_value)
    if find_op_value == "*":
        result = int(first_value) * int(second_value) 
    elif find_op_value == "-":
        result = int(first_value) - int(second_value) 
    elif find_op_value == "+":
        result = int(first_value) + int(second_value)
    elif find_op_value == "/":
        result = int(first_value) / int(second_value)

    line_input.setText(str(result))




btn1.clicked.connect(but1_click)
btn2.clicked.connect(but2_click)
btn3.clicked.connect(but3_click)
btn4.clicked.connect(but4_click)
btn5.clicked.connect(but5_click)
btn6.clicked.connect(but6_click)
btn7.clicked.connect(but7_click)
btn8.clicked.connect(but8_click)
btn9.clicked.connect(but9_click)
btnzero.clicked.connect(but_zero_click)

btn_op1.clicked.connect(btn_op1_click)
btn_op5.clicked.connect(btn_op5_click)
btn_op2.clicked.connect(btn_op2_click)
btn_op3.clicked.connect(btn_op3_click)
btn_op4.clicked.connect(btn_op4_click)

btn_op6.clicked.connect(line_input_clear)

calc_main_win.show()
calc_app.exec_()