from pathlib import Path
import yaml

import base64

# file = Path(__file__).parent.parent / "names.yml"
# yml: list = yaml.load(file.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
# code = base64.encodebytes(str(yml).encode("utf-8"))
# print(code.decode("utf-8"))
# print(base64.decodebytes(code).decode("utf-8"))

# output = Path(__file__).parent.parent / "names"
# output.write_text(code.decode("utf-8"), encoding="utf-8")

inputPath = Path(__file__).parent.parent / "data" / "yaml"
outputPath = Path(__file__).parent.parent / "data" / "base64"

for file in inputPath.iterdir():
    yml: list = yaml.load(file.read_text(encoding="utf-8"), Loader=yaml.FullLoader)
    code = base64.encodebytes(str(yml).encode("utf-8"))
    output = outputPath / file.name.replace(".yml", "")
    output.write_text(code.decode("utf-8"), encoding="utf-8")