# 程序功能

1. 在电脑桌面显示时间、日期、天气
2. 显示中考倒计时（吓唬同学用的）

## 预览

![效果展示](./img/show.png)

# 相关技术

1. `PIL`绘制图片
2. `pywin32`设置桌面背景
3. `requests`、`lxml`获取网页数据
4. `loguru`记录日志
5. `pyside6(pyqt6)`设置任务栏图标

# 具体实现

## 日志模块

在单独的文件中配置 `loguru` 所有地方统一使用

```python
from loguru import logger
from pathlib import Path
import datetime


LOG = Path(__file__).parent.parent / "log"
LOG.mkdir(exist_ok=True)

logDir = LOG / f"{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}"
logDir.mkdir(exist_ok=True)

logger.add(
    f"{logDir}/DEBUG.log",
    level="DEBUG",
)

logger.add(
    f"{logDir}/INFO.log",
    level="INFO",
)
logger.add(
    f"{logDir}/WARNING.log",
    level="WARNING",
)
logger.add(
    f"{logDir}/ERROR.log",
    level="ERROR",
)
logger.add(
    f"{logDir}/CRITICAL.log",
    level="CRITICAL",
)

```

1. 将日志文件储存在根目录下的 `log` 目录内
2. 分别为不同等级创建文件
   1. `logger.add()` 用法
      1. 第一个参数为保存位置
      2. `level` 为级别，只保存此级别及以上日志内容
      3. `formet` 参数用来自定义格式（未用到）
      4. 详见<[酷炫的python日志库-loguru_with logger.contextualize-CSDN博客](https://blog.csdn.net/seanyang_/article/details/132237651?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171172522416800215050773%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=171172522416800215050773&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-132237651-null-null.142^v100^pc_search_result_base4&utm_term=loguru%20%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B&spm=1018.2226.3001.4187)>
   2. `datatime` 格式化日期：`%Y-%m-%d_%H-%M-%S` 表示 年-月-日_时-分-秒

## 天气模块

```python
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

```

1. 获取网页源码并返回
2. [https://www.tianqi.com/lanzhou/15/](https://www.tianqi.com/lanzhou/15/%E2%80%B8) 为兰州的天气预报，请根据需要选择自己所在城市

```python
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
```

1. 解析网页源码
2. 根据实际情况返回天气值，形如 `小雨  3~12 ℃`

## PIL绘制图片

### 天气图片

```python
def weatherImg(
    path: Path,
    size: tuple[int, int],
    place: tuple[float, float],
    weather: str,
    font: tuple[str, int],
    fill: tuple[int, int, int],
):
    """绘制天气图片保存到path"""
    textFont = ImageFont.truetype(*font)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(img).text(place, weather, font=textFont, fill=fill)
    img.save(path / "weather.png")
    logger.debug("绘制天气图片成功")
```

1. `ImageFont.truetype()` 接受2个参数，分别为字体名称和字号
2. `Image.new("RGBA", size, (0, 0, 0, 0))` 创建空白图片，使用rgba颜色，大小为 `size` 背景颜色为透明
3. `ImageDraw.Draw(img)` 创建了新的绘制对象 `.text(place, weather, font=textFont, fill=fill)` 绘制在 `place` 位置，`weather` 文字，`font` 字体，`fill` 颜色(rgb) 的文字
4. 保存为 `weather.png`

### 中考剩余天数

类似于天气图片生成，仅限更改文字

### 最终背景组合

```python
def BgImg(path: Path, size: tuple[int, int], *imgs: str):
    """合成背景图片"""
    logger.debug("开始合成背景图片")
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    for imgPath in imgs:
        logger.debug(f"正在合成背景图片{imgPath}")
        new = Image.open(path / imgPath).convert("RGBA")
        img.alpha_composite(new)
    img.save(path / "result.png")
    logger.debug("合成背景图片成功")
```

1. 创建大小为 `size` 的空白图片
2. 把所有 `imgs` 中的元素以 `alpha_composite()` 混合，保留透明的（此处不能直接粘贴，那样会使透明设置失效）
3. 保存

## 设置桌面背景

```python
def setBackGroundImg(imgPath: Path):
    """设置壁纸"""
    logger.debug("开始设置壁纸")
    win32gui.SystemParametersInfo(
        win32con.SPI_SETDESKWALLPAPER, 
        str(imgPath), 
        win32con.SPIF_SENDWININICHANGE
    )

```

1. `win32gui.SystemParametersInfo()` 用来设置系统信息接受3个参数
   1. `Action`：执行的操作类型，`win32con.SPI_SETDESKWALLPAPER` 表示设置桌面背景，即 `set desk wall paper`
   2. `Param`：操作具体参数，为str类型，在本程序中是桌面背景的路径
   3. `WinIni`：操作标志，`win32con.SPIF_SENDWININICHANGE` 表示在完成后传递系统设置更改的信息，以通知其他依赖于系统设置的程序进行更改，即 `send WinIni(系统设置) change`

## 主程序

### 加载配置

```python
config = yaml.load(
    (IMGS_PATH / "config.yml").read_text(encoding="utf-8"), Loader=yaml.FullLoader
)
```

从配置文件中加载壁纸设置，`config,yml` 内容如下

```yaml
name: 金榜题名
size: [1680, 1050]
font: ["msyh.ttc", 60]
color: [255, 255, 255]  # 绘制文字的颜色
place: 
  weather: [435, 540]
  exam: [900, 540]
```

### 合成图片并设置背景(线程)

```python
class ImgThread(Thread):
    def __init__(self, path: Path, config: dict):
        super().__init__()
        self.path = path
        self.config = config
        self.daemon = True

        self.start()

    @logger.catch
    def run(self):
        logger.info("开始运行图片模块运行")
        # 中考剩余天数
        makeImg.examDaysImg(
            self.path,
            tuple(self.config["size"]),
            tuple(self.config["place"]["exam"]),
            str((datetime(year=2024, month=6, day=16) - datetime.today()).days),  # 中考剩余天数
            tuple(self.config["font"]),
            tuple(self.config["color"]),
        )

        i = True  # 是否是第一次
        nowTime = datetime.now()
        while True:
            if datetime.now().minute != nowTime.minute or i:
                nowTime = datetime.now()
                makeImg.BgImg(
                    self.path,
                    tuple(self.config["size"]),
                    "bg.jpg",
                    "weather.png",
                    "exam.png",
                    f"month{nowTime.month}.png",
                    f"day{nowTime.day}.png",
                    f"hour{nowTime.hour}.png",
                    f"minute{nowTime.minute}.png",
                    f"weekday{nowTime.weekday()+1}.png",
                )
                setBg.setBackGroundImg(self.path / "result.png")

                if i:
                    i = False
            time.sleep(10)

```

1. `__init__()`
   1. `self.daemon = True` 表示设置为守护线程，即：在主线程结束时自动关闭
   2. `self.start()` 实例化后自动开始执行
2. `run()`
   1. `makeImg.examDaysImg()` 计算中考倒计时
      1. `datetime(year=2024, month=6, day=16) - datetime.today()).days` 中考日期与当前日期作差，取差值天数
   2. 无限循环合成图片
      1. 为了节约系统资源，进当时间(分钟)变化或第一次运行时执行
      2. 重设当前时间(上次设置壁纸的时间)
      3. 合成图片
      4. 等待10秒再次执行

### 合成天气图片(线程)

```python
class WeatherThread(Thread):
    def __init__(self, path: Path, config: dict):
        super().__init__()
        self.path = path
        self.config = config
        self.daemon = True

        self.start()

    @logger.catch
    def run(self):
        logger.info("开始运行天气模块")
        i = True  # 是否是第一次
        while True:
            if datetime.now().minute == 0 or i:
                makeImg.weatherImg(
                    self.path,
                    tuple(self.config["size"]),
                    tuple(self.config["place"]["weather"]),
                    weather.getweather(),
                    tuple(self.config["font"]),
                    tuple(self.config["color"]),
                )
                if i:
                    i = False
            time.sleep(50)

```

1. 每小时执行一次
2. 间隔50秒再次执行

### 任务栏右下角图标

```python
class TrayIcon(QSystemTrayIcon):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(str(ROOT / "icon.ico")))
        self.initUI()

    def initUI(self):
        self.menu = QMenu()
        # self.menu.addAction("显示主窗口")
        self.menu.addAction("退出")
        self.setContextMenu(self.menu)
        self.menu.triggered.connect(self.clickEvent)

    def clickEvent(self, action: QAction):
        sys.exit()
```

1. `__init__()`
   1. 设置图标
2. `initUI()`
   1. 设置右键菜单
   2. 点击右键菜单中的项目后退出程序
3. `clickEvent()`
   1. 点击时推出程序(菜单中只有一个按钮，否则得用 `action.text()` 匹配项目)

### 启动

```python
@logger.catch
def main():
    logger.info("程序启动")
    ImgThread(IMGS_PATH, config)
    WeatherThread(IMGS_PATH, config)
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    tray = TrayIcon()
    tray.show()
    sys.exit(app.exec())
```

1. `@logger.catch` 捕获程序运行产生的报错，正常情况下不会存在
2. 启动图片、天气线程
3. 打开任务栏图标

# GITEE

1. 程序用到的代码、资源图片(clock目录内)均上传到gitee
2. 开源地址：<[电脑壁纸设置 · 李昊轩/Python - 码云 - 开源中国 (gitee.com)](https://gitee.com/dudu7615/python/tree/master/%E7%94%B5%E8%84%91%E5%A3%81%E7%BA%B8%E8%AE%BE%E7%BD%AE)>
