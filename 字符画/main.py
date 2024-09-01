from PIL import Image
import getFontSize

# 将图像加载为像素数组
image = Image.open(r"D:\dudu\Documents\dudu\python\###\0 (3).jpg")
image = image.resize((64, 64))
pixels = image.load()

# 定义字符画中的字符
CHARS = getFontSize.main(step=5)

# 将像素数组转换为一个字符数组
char_array = []
for y in range(image.height):
    for x in range(image.width):
        r, g, b = pixels[x, y]
        # 将像素值映射到字符
        index = int((r + g + b) / 3 / 255 * (len(CHARS) - 1))
        char_array.append(CHARS[index])
    char_array.append("\n")

# 将字符数组转换为字符串并打印
text = " " + " ".join(char_array)
print(text)

with open(r"D:\dudu\Documents\dudu\python\###\0 (3).txt", "w") as f:
    f.write(text)
