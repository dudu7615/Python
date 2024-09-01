import asyncio
import datetime
import time
from pathlib import Path
from queue import Queue

import aiohttp
import requests
from PySide6.QtCore import QThread, Signal


def makeNum(num: int):
    if num < 1024:
        return f"{num}B"
    elif num < 1024**2:
        return f"{num/1024:.2f}KB"
    elif num < 1024**3:
        return f"{num/1024**2:.2f}MB"
    else:
        return f"{num/1024**3:.2f}GB"


class downloader(QThread):
    finished = Signal()
    info = Signal(str)

    def __init__(
        self,
        url: str,
        basePath: Path,
        bitSize: int,
    ):
        super().__init__()
        self.url = url
        self.basePath = basePath
        self.filePath = self.basePath / Path(url).name
        self.tmpPath = self.basePath / "tmp"
        self.bitSize = bitSize
        self.tmpPath.mkdir(exist_ok=True)

    def run(self):
        start = time.time()
        size = self.getSize()
        self.info.emit(f"{datetime.datetime.now():%H:%M:%S} [开始下载] 总大小{makeNum(size)}")
        bytes = Queue()
        self.cutFile(bytes, size)
        self.allBits = bytes.qsize()
        self.info.emit(
            f"{datetime.datetime.now():%H:%M:%S} [文件分割完成] 共{bytes.qsize()}块 块大小{makeNum(self.bitSize)}"
        )
        asyncio.run(self.download(bytes))
        # 合并文件
        self.info.emit(f"{datetime.datetime.now():%H:%M:%S} [开始合并文件]")
        files = (self.tmpPath).iterdir()
        with open(self.filePath, "ab") as f:
            for i in files:
                if i.name == self.filePath.name:
                    continue
                with open(self.tmpPath / i, "rb") as tmp:
                    f.write(tmp.read())

                i.unlink()
        self.info.emit(f"{datetime.datetime.now():%H:%M:%S} [文件合并完成]")
        end = time.time()
        self.info.emit(f"{datetime.datetime.now():%H:%M:%S} [下载完成] 用时{end-start:.2f}s")
        # print(f"Time: {end-start}")

    def getSize(self) -> int:
        response = requests.head(self.url)
        return int(response.headers["Content-Length"])

    def cutFile(self, bytes: Queue, size: int):
        if size <= self.bitSize:
            bytes.put([0, f"0-{size}"])
        else:
            bits = list(range(0, size, self.bitSize))
            bits.append(
                (size % self.bitSize) + ((size // self.bitSize - 1) * self.bitSize)
            )  # 最后一块,len从1开始，而所需数据从0开始，所以-1
            for i in bits:
                if i + self.bitSize > size:
                    bytes.put([i // self.bitSize, f"{i}-{size}"])
                else:
                    bytes.put([i // self.bitSize, f"{i}-{i+self.bitSize-1}"])

    async def download(self, bytes: Queue):
        async with aiohttp.ClientSession() as session:
            tasks = [self.getter(session, bytes) for _ in range(32)]
            await asyncio.gather(*tasks)

    async def getter(self, session: aiohttp.ClientSession, bytes: Queue):
        while not bytes.empty():
            byte = bytes.get()
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
                "Range": f"bytes={byte[1]}",
            }
            async with session.get(self.url, headers=headers) as response:
                with open(self.tmpPath / f"{byte[0]}.tmp", "wb") as f:
                    f.write(await response.read())
                    self.info.emit(
                        f"{datetime.datetime.now():%H:%M:%S} [已下载] {int(100-((bytes.qsize()/self.allBits)*100)):03d}%  ({byte[0]:0{len(str(self.allBits))}}/{self.allBits})",
                    )


if __name__ == "__main__":
    ROOT = Path(__file__).parent
    (ROOT / "tmp").mkdir(exist_ok=True)
    url = "https://cdimage.deepin.com/live-system/deepin-live-system-2.0-amd64.iso"
    filePath = ROOT / Path(url).name
    BIT_SIZE = 1 * 1024**2

    a = downloader(url, ROOT, BIT_SIZE)
    a.info.connect(print)
    a.run()
