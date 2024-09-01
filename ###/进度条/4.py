from rich.progress import track
import  time
 
for step in track(range(100),"downloading... "):
    for step1 in track(range(100),"downloading... "):
        print(step,step1)
        time.sleep(0.001)
