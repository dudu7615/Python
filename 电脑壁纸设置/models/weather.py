import requests
from lxml import etree
from .log import logger


def resqPage():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0"
    }
    resq = requests.get("https://www.tianqi.com/lanzhou/15/", headers=headers)
    if resq.status_code != 200:
        logger.error("获取天气失败")
    else:
        logger.debug("天气网页获取成功")
    return resq.text


def getweather():
    page = resqPage()
    html = etree.HTML(page, etree.HTMLParser())
    weather = html.xpath("/html/body/div[6]/div[4]/div[1]/div[1]/div/h3/text()")[0]
    temperature = (
        f"{html.xpath('/html/body/div[6]/div[4]/div[1]/div[1]/div/p/span[1]/text()')[0]}~"
        f"{html.xpath('/html/body/div[6]/div[4]/div[1]/div[1]/div/p/span[2]/text()')[0]} ℃"
    )
    logger.debug(f"天气：{weather}，温度：{temperature}")
    return (
        f"{weather}  {temperature}"
        if weather and temperature != "~ ℃" # 判断是否获取到天气
        else "获取天气失败"
    )

@logger.catch
def test():
    print(getweather())


if __name__ == "__main__":
    test()
