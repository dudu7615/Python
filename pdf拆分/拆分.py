from PIL import Image
from loguru import logger
import fitz
import io
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
IMG = ROOT / "images"
INPUT = ROOT / "input"
# OUTPUT = ROOT / "output"


def splitPdf(pdf_path: Path):
    # 确保输出目录存在
    imgs_dir = IMG / pdf_path.stem
    shutil.rmtree(imgs_dir, ignore_errors=True)
    imgs_dir.mkdir(exist_ok=True)

    # 读取PDF文件
    pdf = fitz.open(pdf_path)
    for page_num in range(pdf.page_count):
        page = pdf[page_num]
        image_list = page.get_images(full=True)
        for image_index, img in enumerate(image_list):
            if image_index %2 == 0:
                continue  # 只保存奇数页
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(imgs_dir / f"{page_num}.png")


# 示例调用
for pdf_file in INPUT.glob("*.pdf"):
    logger.info(f"Splitting {pdf_file}")
    splitPdf(pdf_file)
