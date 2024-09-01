
import sys
import time
 
def progressbar(it, tittle="", size=50, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write(f"{tittle} [{'='*x}>{' '*(size-x)}] {int(j/count*100)}%\r" )  # sys.stdout.write = print无换行
        file.flush()   # 刷新         
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
 
     
for _ in progressbar(range(100), "Computing: ", 40):
    # doSomething
    time.sleep(0.1)