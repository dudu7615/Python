from PIL import Image
from pathlib import Path

def saveAsPDF(imgFiles: list[Path], fileName: Path):
    imgs = [Image.open(f) for f in imgFiles]
    for i in imgs:
        if i.mode != 'RGB':
            imgs[imgs.index(i)] = i.convert('RGB')

    imgs[0].save(fileName, 'PDF', resolution=100.0, save_all=True, append_images=imgs[1:])


if __name__ == '__main__':
    Root = Path(__file__).parent
    # saveAsPDF(Root/"imgs", Root/"book.pdf")