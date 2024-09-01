import requests
from lxml import etree
import asyncio
from loguru import logger
from pathlib import Path
import saveAsPDF
import aiohttp
import time
import sys
import shutil

formater = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

logger.remove()
logger.add(sys.stdout, format=formater, level=0)

ROOT = Path(__file__).parent
imgDir = ROOT / "imgs"
resultDir = ROOT / "result"
imgDir.mkdir(exist_ok=True)
resultDir.mkdir(exist_ok=True)

config = {
    "main": "http://www.xuebajia.com",
    "books": "/html/body/div[4]/ul/li/a/@href",
    # "title": "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/h1/text()",  # 获取标题
    "title": "/html/head/title/text()",  # 获取标题
    "list": "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/ul/li/a/@href",
    "pages": "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[3]/div/a/@href",  # [:-2]
    "img": "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/p[1]/a/@href",  # 应该是在爬取时p[1]的空文本框不加载，所以原本的p[2]要用p[1]
}


def getBooks(url: str):
    html = requests.get(url).text
    page = etree.HTML(html, parser=etree.HTMLParser(encoding="utf-8"))
    return [config["main"] + i for i in page.xpath(config["books"])]


def getBookList(url: str):
    html = requests.get(url)
    html.encoding = "utf-8"
    page = etree.HTML(html.text, parser=etree.HTMLParser(encoding="utf-8"))
    # logger.info("获取图片列表成功")

    bookList = page.xpath(config["list"])
    return [config["main"] + i for i in bookList]


def getTitle(url: str):
    html = requests.get(url)
    html.encoding = "utf-8"
    page = etree.HTML(html.text, parser=etree.HTMLParser(encoding="utf-8"))
    return page.xpath(config["title"])[0][:-2]


async def getImgList(urls: list[str], session: aiohttp.ClientSession):
    # logger.info("开始获取图片列表")

    tasks = [getPageList(url, session) for url in urls]
    result: list = await asyncio.gather(*tasks)
    pages = [j for i in result for j in i]
    # pages = result
    # logger.info("获取页面列表成功")
    imgLingTasks = [getImgLink(url, session) for url in pages]
    imgLinks_ = await asyncio.gather(*imgLingTasks)
    return [i for i in imgLinks_ if i is not None]


async def getPageList(url: str, session: aiohttp.ClientSession):
    return [url, *[f"{url[:-5]}_{i}.html" for i in range(2, 30)]]


async def getImgLink(url: str, session: aiohttp.ClientSession):
    for i in range(3):
        try:
            html = await session.get(url)
            if html.status != 200:
                if i == 2:
                    logger.error(f"{url}获取失败")
                return None
            page = etree.HTML((await html.text()).replace("\r\n", ""), parser=etree.HTMLParser(encoding="utf-8"))
            return page.xpath(config["img"])[0]
        except Exception as e:
            logger.error(e)


async def getter(url: str, session: aiohttp.ClientSession):
    async with await session.get(url) as page:
        return await page.read()


async def main(url: str):
    logger.info("开始执行")
    async with aiohttp.ClientSession() as session:
        bookList = getBookList(url)
        title = getTitle(url)
        imgLinks = await getImgList(bookList, session)
        tasks = [getter(url, session) for url in imgLinks]
        result = await asyncio.gather(*tasks)
        imgFiles = []
        for i, img in enumerate(result):
            imgFiles.append(Path(imgDir / f"{i}.jpg"))
            with open(imgDir / f"{i}.jpg", "wb") as f:
                f.write(img)
        pdfPath = resultDir / f"{title}.pdf"
        # logger.info("开始转换pdf")
        saveAsPDF.saveAsPDF(imgFiles, pdfPath)


def clean():
    shutil.rmtree(imgDir)

    imgDir.mkdir(exist_ok=True)
    # logger.info("清理完成")


if __name__ == "__main__":
    statr = time.time()
    for url in getBooks("http://www.xuebajia.com/renjiaoban/"):
        asyncio.run(main(url=url))
        logger.info(f"执行完成{url}")
        clean()
    logger.info(f"执行时间{(time.time()-statr):.2f}")
