
import time
 
def show(prog:int,tittle=""):
    num = prog//2
    print(f"\r{tittle} [{'='*num}>{' '*(50-num)}] {prog}%",end="")  # sys.stdout.write = print无换行
        
for i in range(101):
    # doSomething
    show(i,tittle="Running... ")
    time.sleep(0.1)