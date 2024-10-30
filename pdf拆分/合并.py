from PIL import Image
from loguru import logger
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
IMG = ROOT / "images"
OUTPUT = ROOT / "output"

def sort(imgs:list[Path]) -> list[Path]:
    # 按照名称数字顺序排序
    return sorted(imgs, key=lambda x: int(x.stem))

def savePdf(pdf_path: Path, img_dir: Path):
    # 删除原文件
    shutil.rmtree(pdf_path, ignore_errors=True)

    imgList: list[Path] = sort(list(img_dir.glob("*.png")))
    imgs = [Image.open(f) for f in imgList]
    imgs[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=imgs[1:])

for img_dir in IMG.glob("*"):
    logger.info(f"Saving {img_dir}")
    savePdf(OUTPUT / f"{img_dir.stem}.pdf", img_dir)