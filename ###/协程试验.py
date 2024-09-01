import asyncio
import time

# 协程函数

async def func(x:int):
    print('doing: ', x)
    await asyncio.sleep(200000)
    return f'done {x}'


# 将协程转成task，并组成list
tasks = [asyncio.ensure_future(func(i)) for i in range(10000)]


start = time.time()

# for x in range(100):
#     c = func(x)
#     tasks.append(asyncio.ensure_future(c))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for i in tasks:
    print(i.result())

print(time.time()-start)
