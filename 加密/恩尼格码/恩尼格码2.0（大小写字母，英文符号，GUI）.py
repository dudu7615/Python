from tkinter import *
from tkinter import filedialog

app = Tk()
app.title('恩尼格码加密')
app.geometry('400x200')

def opentxt():
    name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])
    txt = open(name,encoding='utf8').read()
    text.insert(1.0,txt)

def savetxt():
    fileSave = filedialog.asksaveasfilename(defaultextension='.txt',filetypes = [("文本文件",".txt")])
    save = open(fileSave,'a',encoding='utf8')
    save.write(f'密码为{a1} {a2} {a3} {a4} {a5} {a6}\n###---以下是正文---###\n'+text.get("1.0","end"))

list1 = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', ',', '.', '/', ';', "'", '\\', '[', ']', '-', '=', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', '"', '|', '<', '>', '?', '\n']
list2 = ['F', '7', 'A', '*', 'p', 'x', '@', '\n', ']', 'R', "'", 'w', 't', 'j', '(', 'e', 'a', 'K', 'N', '.', 'X', '<', 'H', 'y', 'm', 'U', '[', 'L', '|', 'h', 'G', '%', '~', ':', 'n', 'J', '0', 'S', 'C', ' ', 'r', 'M', '#', '>', 's', '2', 'c', 'o', 'g', '{', 'u', '$', '/', 'Z', 'O', '^', 'D', '+', '-', 'W', ',', '6', '9', 'q', '}', 'T', '3', '&', 'b', 'Q', 'f', 'E', 'z', '?', '`', 'v', 'I', ';', '_', 'Y', 'B', '=', 'P', '\\', ')', '1', '"', 'd', '4', 'l', 'i', 'V', '5', '!', 'k', '8']
list3 = ['v', '9', 'L', '+', 'D', '5', '{', '0', '8', 'A', 's', '"', '&', '<', '\n', 'V', 'b', 'F', 'O', 'p', 'Z', ':', '$', '[', 'o', '7', 'W', ')', 'N', 'w', 'c', 'd', '.', 'f', 'm', 'H', 'n', 't', 'Q', '2', '(', '?', 'P', 'T', '!', 'R', 'K', '*', '-', '6', 'g', "'", '=', '^', 'Y', 'h', 'x', '/', 'G', 'E', ';', '#', 'M', 'J', 'e', '`', 'l', 'q', 'X', 'I', '_', '~', 'a', 'u', 'j', '3', '@', ',', ']', 'y', '%', '|', 'S', 'B', 'r', '1', 'i', 'k', 'C', '>', 'U', 'z', '\\', ' ', '4', '}']
list4 = ['E', '%', 'J', 'R', '_', 'W', 'b', 'u', '{', 'a', 'Z', '?', 'c', 'N', 'x', '9', '`', '*', "'", '~', '1', '&', '}', '2', '\\', 'j', 'w', '5', '>', ';', '7', 'F', '-', 'y', '+', 'G', 'h', ':', 'L', '<', '#', '8', 'U', 'X', 'g', 'q', '^', 'H', ']', 's', 'm', 'I', 'V', 'K', 'Q', '(', 'C', 'D', 'i', 'n', 'M', 'p', '"', 'v', 'S', '/', 'k', '.', 'B', '4', 'O', ')', '@', '0', '3', 'A', '!', ' ', 'o', 'z', 'd', 'l', 'e', '6', 't', '[', 'r', '=', 'P', ',', '|', '\n', '$', 'f', 'T', 'Y']
list5 = ['\n', 'z', 'y', '0', 'Z', 'l', '+', 'B', ']', 'w', '$', '%', '<', '}', 'Q', 'i', '`', 'N', 'r', 'A', '=', 'n', 'p', '[', '5', '6', 'o', 'O', '!', '@', '2', 'J', '~', 's', '>', 'W', 'h', '8', '"', 'U', '{', 'K', 'k', '(', '&', 'F', 'P', 'V', 'X', 'L', ' ', 'g', 'D', 'd', 'q', 'a', '\\', 'j', 'T', '-', ',', 'v', 'M', '^', '7', 'R', '_', '1', 'Y', ':', 'm', 'I', 'b', 'C', '|', 'c', '9', "'", '?', ';', '#', 'x', 'f', 'E', '.', 't', 'u', '3', 'H', '/', 'G', 'S', '*', 'e', '4', ')']

lock_unlock_list = ['加/解','加密','解密']
lock_unlock = StringVar()
lock_unlock.set(lock_unlock_list[0])

first_list = ['一','1','2','3','4','5']
first = StringVar()
first.set(first_list[0])

second_list = ['二','1','2','3','4','5']
second = StringVar()
second.set(second_list[0])

third_list = ['三','1','2','3','4','5']
third = StringVar()
third.set(third_list[0])

fouth_list = ['一始','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95']
fouth = StringVar()
fouth.set(fouth_list[0])

fifth_list = ['二始','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95']
fifth = StringVar()
fifth.set(fifth_list[0])

sixth_list = ['三始','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95']
sixth = StringVar()
sixth.set(sixth_list[0])
if True:  #选择
    def chose0(*args):
        global a0
        a0=lock_unlock.get()  
        print(a0)
    lock_unlock.trace("w", chose0)
    def chose1(*args):
        global a1
        a1=first.get()  
        print(a1)
    first.trace("w", chose1)
    def chose2(*args):
        global a2
        a2=second.get()  
        print(a2)
    second.trace("w", chose2)
    def chose3(*args):
        global a3
        a3=third.get()  
        print(a3)
    third.trace("w", chose3)
    def chose4(*args):
        global a4
        a4=int(fouth.get())
        print(a4)
    fouth.trace("w", chose4)
    def chose5(*args):
        global a5
        a5=int(fifth.get())
        print(a5)
    fifth.trace("w", chose5)
    def chose6(*args):
        global a6
        a6=int(sixth.get())
        print(a6)
    sixth.trace("w", chose6)

def main():
    b = text.get("1.0","end")
    ok = ''  # 最终输出结果
    c0=a0
    c1=a1
    c2=a2
    c3=a3
    c4=a4
    c5=a5
    c6=a6
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
                # 第一个转子
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

                ok = ok+f

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
                pass

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

                ok = ok+f

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
                pass
    ok = ok[:-1]
    print(ok)
    text.delete("1.0","end")
    text.insert(INSERT,ok)

choose_first = OptionMenu(app,first,*first_list) 
choose_second = OptionMenu(app,second,*second_list) 
choose_third = OptionMenu(app,third,*third_list) 
choose_fouth = OptionMenu(app,fouth,*fouth_list) 
choose_fifth = OptionMenu(app,fifth,*fifth_list) 
choose_sixth = OptionMenu(app,sixth,*sixth_list) 
open_txt = Button(app,text='打开文件',command=opentxt)
save_txt = Button(app,text='保存文件',command=savetxt)
choose_lock_unlock = OptionMenu(app,lock_unlock,*lock_unlock_list) 
start = Button(app,text='运行',command=main)
text = Text(app)

choose_first.place(x=5,y=5,height=30,width=70)
choose_second.place(x=80,y=5,height=30,width=70)
choose_third.place(x=155,y=5,height=30,width=70)
choose_fouth.place(x=5,y=35,height=30,width=70)
choose_fifth.place(x=80,y=35,height=30,width=70)
choose_sixth.place(x=155,y=35,height=30,width=70)
open_txt.place(x=305,y=7,height=26,width=66)
save_txt.place(x=305,y=37,height=26,width=66)
choose_lock_unlock.place(x=230,y=5,height=30,width=70)
start.place(x=232,y=37,height=26,width=66)
text.place(x=5,y=70,height=120,width=390)
app.mainloop()

print(f'{a0}{a1}{a2}{a3}{a4}{a5}{a6}')