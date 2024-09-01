from PIL import Image, ImageDraw, ImageFont
text = """  """

def makeImg(
    text: str,
):
    """生成天气图片"""
    font = ImageFont.truetype("C:\\Windows\\Fonts\\msyh.ttc", 100)
    img = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    drawImg = ImageDraw.Draw(img)
    drawImg.text((0.0, 0.0), text, font=font, fill=(255, 255, 255))
    img.save("font.png")


def getFontSize(imgPath: str):
    """获取字体大小"""
    size = 0
    img = Image.open(imgPath)
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x, y)) != (0, 0, 0, 0):
                size += 1

    return size


def bubble_sort(arr: list[int]):
    """冒泡算法"""
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n - i - 1):
            # 当前元素大于下一个元素，交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

r"01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}[]\|;':,./<>?`~",
def main(
    texts: str = r"01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}[]\|;':,./<>?`~",
    step: int = 3,
):
    sizes = {}
    for text in texts:
        makeImg(text)
        sizes[getFontSize("font.png")] = text

    intSizes = bubble_sort(list(sizes.keys()))
    textlist = [sizes[size] for size in intSizes]

    return [textlist[i] for i in range(0, len(textlist), step)]


if __name__ == "__main__":
    print(main())
