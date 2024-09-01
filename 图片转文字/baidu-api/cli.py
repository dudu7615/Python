from aip import AipOcr
from pathlib import Path


APP_ID = "30347098"
API_KEY = "uCCdCzL9aQQYf6wDF9KlVmzm"
SECRET_KEY = "VnaP7543j3Xr13d5WATcbl8q6I8rsIWa"

ROOT = Path(__file__).parent
INPUT = ROOT / "img"
OUTPUT = ROOT / "txt"

INPUT.mkdir(exist_ok=True)
OUTPUT.mkdir(exist_ok=True)

options = {
    "language_type": "CHN_ENG",
    "detect_direction": "true",
    "detect_language": "true",
    "probability": "false",
}

ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
for file in INPUT.iterdir():
    with open(file, "rb") as f:
        result:dict = ocr.basicGeneral(f.read(), options)
        print(result)
        with open(OUTPUT / f"{file.name}.txt", "w", encoding="utf-8") as f:
            for text in result["words_result"]:
                f.write(text["words"])
                f.write("\n")
            # f.write(result["words_result"]["words"])
            

