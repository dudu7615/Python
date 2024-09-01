import sys
from PySide6.QtWidgets import *

list1 = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', ',', '.', '/', ';', "'", '\\', '[', ']', '-', '=', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', '"', '|', '<', '>', '?', '\n']
list2 = ['F', '7', 'A', '*', 'p', 'x', '@', '\n', ']', 'R', "'", 'w', 't', 'j', '(', 'e', 'a', 'K', 'N', '.', 'X', '<', 'H', 'y', 'm', 'U', '[', 'L', '|', 'h', 'G', '%', '~', ':', 'n', 'J', '0', 'S', 'C', ' ', 'r', 'M', '#', '>', 's', '2', 'c', 'o', 'g', '{', 'u', '$', '/', 'Z', 'O', '^', 'D', '+', '-', 'W', ',', '6', '9', 'q', '}', 'T', '3', '&', 'b', 'Q', 'f', 'E', 'z', '?', '`', 'v', 'I', ';', '_', 'Y', 'B', '=', 'P', '\\', ')', '1', '"', 'd', '4', 'l', 'i', 'V', '5', '!', 'k', '8']
list3 = ['v', '9', 'L', '+', 'D', '5', '{', '0', '8', 'A', 's', '"', '&', '<', '\n', 'V', 'b', 'F', 'O', 'p', 'Z', ':', '$', '[', 'o', '7', 'W', ')', 'N', 'w', 'c', 'd', '.', 'f', 'm', 'H', 'n', 't', 'Q', '2', '(', '?', 'P', 'T', '!', 'R', 'K', '*', '-', '6', 'g', "'", '=', '^', 'Y', 'h', 'x', '/', 'G', 'E', ';', '#', 'M', 'J', 'e', '`', 'l', 'q', 'X', 'I', '_', '~', 'a', 'u', 'j', '3', '@', ',', ']', 'y', '%', '|', 'S', 'B', 'r', '1', 'i', 'k', 'C', '>', 'U', 'z', '\\', ' ', '4', '}']
list4 = ['E', '%', 'J', 'R', '_', 'W', 'b', 'u', '{', 'a', 'Z', '?', 'c', 'N', 'x', '9', '`', '*', "'", '~', '1', '&', '}', '2', '\\', 'j', 'w', '5', '>', ';', '7', 'F', '-', 'y', '+', 'G', 'h', ':', 'L', '<', '#', '8', 'U', 'X', 'g', 'q', '^', 'H', ']', 's', 'm', 'I', 'V', 'K', 'Q', '(', 'C', 'D', 'i', 'n', 'M', 'p', '"', 'v', 'S', '/', 'k', '.', 'B', '4', 'O', ')', '@', '0', '3', 'A', '!', ' ', 'o', 'z', 'd', 'l', 'e', '6', 't', '[', 'r', '=', 'P', ',', '|', '\n', '$', 'f', 'T', 'Y']
list5 = ['\n', 'z', 'y', '0', 'Z', 'l', '+', 'B', ']', 'w', '$', '%', '<', '}', 'Q', 'i', '`', 'N', 'r', 'A', '=', 'n', 'p', '[', '5', '6', 'o', 'O', '!', '@', '2', 'J', '~', 's', '>', 'W', 'h', '8', '"', 'U', '{', 'K', 'k', '(', '&', 'F', 'P', 'V', 'X', 'L', ' ', 'g', 'D', 'd', 'q', 'a', '\\', 'j', 'T', '-', ',', 'v', 'M', '^', '7', 'R', '_', '1', 'Y', ':', 'm', 'I', 'b', 'C', '|', 'c', '9', "'", '?', ';', '#', 'x', 'f', 'E', '.', 't', 'u', '3', 'H', '/', 'G', 'S', '*', 'e', '4', ')']

class Main(QMainWindow):
    """ gui界面 """
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 305, 180)
        self.setWindowTitle('恩尼格码加密')
        self.initUI()

    def initUI(self):
        """ 定义控件 """
        # 运行按钮
        self.run = QPushButton('运行', self)
        self.run.clicked.connect(self.main)
        self.run.resize(70,30)
        self.run.move(230, 40)

        # 文本框
        self.text = QTextEdit(self)
        self.text.resize(295,100)
        self.text.move(5, 75)

        # 选择框
        self.ChooseLockUnluck = QComboBox(self)
        self.ChooseLockUnluck.addItems(["加密","解密"])
        self.ChooseLockUnluck.resize(70,30)
        self.ChooseLockUnluck.move(230, 5)

        self.choose1 = QComboBox(self)
        self.choose1.addItems(['1','2','3','4','5'])
        self.choose1.resize(70,30)
        self.choose1.move(5, 5)

        self.choose2 = QComboBox(self)
        self.choose2.addItems(['1','2','3','4','5'])
        self.choose2.resize(70,30)
        self.choose2.move(80, 5)

        self.choose3 = QComboBox(self)
        self.choose3.addItems(['1','2','3','4','5'])
        self.choose3.resize(70,30)
        self.choose3.move(155, 5)

        self.choose1st = QComboBox(self)
        self.choose1st.addItems(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95'])
        self.choose1st.resize(70,30)
        self.choose1st.move(5, 40)

        self.choose2st = QComboBox(self)
        self.choose2st.addItems(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95'])
        self.choose2st.resize(70,30)
        self.choose2st.move(80, 40)

        self.choose3st = QComboBox(self)
        self.choose3st.addItems(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95'])
        self.choose3st.resize(70,30)
        self.choose3st.move(155, 40)

        self.show()


    def main(self):
        b = self.text.toPlainText()
        ok = ''  # 最终输出结果
        c0=self.ChooseLockUnluck.currentText()
        c1=self.choose1.currentText()
        c2=self.choose2.currentText()
        c3=self.choose3.currentText()
        c4=int(self.choose1st.currentText())
        c5=int(self.choose2st.currentText())
        c6=int(self.choose3st.currentText())
        if c1 == '1':
            find1 = list1
        elif c1 == '2':
            find1 = list2
        elif c1 == '3':
            find1 = list3
        elif c1 == '4':
            find1 = list4
        elif c1 == '5':
            find1 = list5

        if c2 == '1':
            find2 = list1
        elif c2 == '2':
            find2 = list2
        elif c2 == '3':
            find2 = list3
        elif c2 == '4':
            find2 = list4
        elif c2 == '5':
            find2 = list5

        if c3 == '1':
            find3 = list1
        elif c3 == '2':
            find3 = list2
        elif c3 == '3':
            find3 = list3
        elif c3 == '4':
            find3 = list4
        elif c3 == '5':
            find3 = list5

        if c0 == '加密':  # 加密
            for f in b:
                try:  # 避免其他字符
                    #第一个转子
                    d = find1.index(f)
                    d += c4
                    if d > 95:  # 前置参数超过总数后还原
                        d -= 96
                    f = find1[d]
                    # 第二个转子
                    d = find2.index(f)
                    d += c5
                    if d > 95:
                        d -= 96
                    f = find2[d]
                    # 第三个转子
                    d = find3.index(f)
                    d += c6
                    if d > 95:
                        d -= 96
                    f = find3[d]

                    ok += f

                    #转子旋转
                    if c4 == 95:
                        c4 = 0  # 第一个旋转归零
                        if c5 == 95:
                            c5 = 0  # 第二个旋转归零
                            if c6 == 95:
                                c6 = 0  # 第三个旋转归零
                            else:
                                c6 += 1 
                        else:
                            c5 += 1
                    else:
                        c4 += 1

                except:
                    ok += f

        if c0 == '解密':  # 解密
            for f in b:
                try:  # 同上
                    d = find3.index(f)
                    d -= c6
                    if d < 0:
                        d += 96
                    f = find3[d]

                    d = find2.index(f)
                    d -= c5
                    if d < 0:
                        d += 96
                    f = find2[d]

                    d = find1.index(f)
                    d -= c4
                    if d < 0:
                        d += 96
                    f = find1[d]

                    ok += f

                    #转子旋转
                    if c4 == 95:
                        c4 = 0  # 第一个旋转归零
                        if c5 == 95:
                            c5 = 0  # 第二个旋转归零
                            if c6 == 95:
                                c6 = 0  # 第三个旋转归零
                            else:
                                c6 += 1 
                        else:
                            c5 += 1
                    else:
                        c4 += 1

                except:
                    ok += f

        # ok=ok[0:-1]  # 会莫名其妙多一项，删掉就行
        print(ok)
        self.text.setPlainText(ok)

app = QApplication(sys.argv)
ui=Main()
sys.exit(app.exec())
