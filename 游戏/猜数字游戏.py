import random
a = 0  #a,数字和位置
b = 0  #b，仅数字
index = random.sample(range(10), 4)
c1,c2,c3,c4 = index
m1=str(c1)
m2=str(c2)
m3=str(c3)
m4=str(c4)

while a!=4:
    a = 0
    b = 0
    math = input("请输入你的答案:")
    if math == '0000':
        print(index)
    d1,d2,d3,d4 = math

    if d1 == m1:
        a+=1
        b+=1
    if d2 == m2:
        a+=1
        b+=1
    if d3 == m3:
        a+=1
        b+=1
    if d4 == m4:
        a+=1
        b+=1

    if d1 in [m2, m3, m4]:
        b+=1
    if d2 in [m1, m3, m4]:
        b+=1
    if d3 in [m1, m2, m4]:
        b+=1
    if d4 in [m1, m2, m3]:
        b+=1

    print(f"{a}个数字位置对；{b}个数字对")

print("恭喜过关！！！")
input()
    