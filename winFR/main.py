import os
ROOT = os.path.dirname(os.path.abspath(__file__))
runNum =  os.system(f'{ROOT}\\winFR.exe')
if runNum == 0:
    args = input("winFR> ")
    os.system(f'{ROOT}\\winFR.exe {args}')
else:
    print("请以管理员身份运行本程序！")
os.system("pause")