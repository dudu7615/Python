list0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list1 = ['b', 'z', 'x', 'q', 'k', 'd', 'c', 'l', 'm', 'e', 'n', 's', 'y', 'a', 'w', 'u', 'f', 'o', 'r', 'v', 't', 'p', 'j', 'h', 'i', 'g']
list2 = ['q', 'u', 'b', 'z', 'x', 'k', 'd', 'n', 'c', 'l', 'm', 'e', 's', 'y', 'a', 'w', 'f', 'o', 'r', 'v', 't', 'p', 'j', 'h', 'i', 'g']
list3 = ['i', 'v', 't', 'e', 's', 'l', 'm', 'z', 'c', 'h', 'y', 'p', 'u', 'q', 'w', 'g', 'b', 'a', 'r', 'k', 'f', 'x', 'j', 'o', 'd', 'n']
list4 = ['z', 'k', 'i', 'x', 'y', 's', 'l', 'q', 'p', 'e', 'd', 'o', 'g', 'w', 'h', 'c', 'n', 'f', 'j', 'b', 'v', 'm', 'a', 't', 'u', 'r']
list5 = ['k', 'g', 'f', 'u', 'm', 't', 'e', 'r', 'j', 'x', 'q', 'n', 'h', 'l', 'p', 'o', 'c', 'w', 'd', 'a', 's', 'i', 'z', 'v', 'b', 'y']

a = input("请输入配置<[0加密/1解密]>,<组合<第一个><第二个><第三个>>,<开始值<第一个> <第二个> <第三个>>：")
b = input("请输入目标内容：")

x = a.split(',')
x1,x2,x3 = x
y1,y2,y3 = x2

o = x3.split(' ')
o1,o2,o3 = o
z1 = int(o1)
z2 = int(o2)
z3 = int(o3)

if y1 == '1':
    find1 = list1
elif y1 == '2':
    find1 = list2
elif y1 == '3':
    find1 = list3
elif y1 == '4':
    find1 = list4
elif y1 == '5':
    find1 = list5

if y2 == '1':
    find2 = list1
elif y2 == '2':
    find2 = list2
elif y2 == '3':
    find2 = list3
elif y2 == '4':
    find2 = list4
elif y2 == '5':
    find2 = list5

if y3 == '1':
    find3 = list1
elif y3 == '2':
    find3 = list2
elif y3 == '3':
    find3 = list3
elif y3 == '4':
    find3 = list4
elif y3 == '5':
    find3 = list5

ok = ''

if x1 == '0':
    for f in b:
        d = find1.index(f)
        d += z1
        if d > 25:
            d -= 26
        f = find1[d]

        d = find2.index(f)
        d += z2
        if d > 25:
            d -= 26
        f = find2[d]

        d = find3.index(f)
        d += z3
        if d > 25:
            d -= 26
        f = find3[d]

        ok += f

        #转子旋转
        if z1 == 25:
            z1 = 0
        
            if z2 == 25:
                z2 = 0
            
                if z3 == 25:
                    z3 = 0
                else:
                    z3 += 1
                
            else:
                z2 += 1

        else:
            z1 += 1



if x1 == '1':
    for f in b:
        d = find3.index(f)
        d -= z3
        if d < 0:
            d += 26
        f = find3[d]

        d = find2.index(f)
        d -= z2
        if d < 0:
            d += 26
        f = find2[d]

        d = find1.index(f)
        d -= z1
        if d < 0:
            d += 26
        f = find1[d]

        ok += f

        #转子旋转
        if z1 == 25:
            z1 = 0
        
            if z2 == 25:
                z2 = 0
            
                if z3 == 25:
                    z3 = 0
                else:
                    z3 += 1
                
            else:
                z2 += 1

        else:
            z1 += 1

print(ok)
input()
