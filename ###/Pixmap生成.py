import yaml, os, sys

ymlFile = R"D:\Admin\Documents\dudu\python\游戏\坦克大战\data\files.yml"


def filesToBytes(files: list[dict | str], rootPath: str, bytes: dict[str,bytes] = {}):
    for file in files:
        if isinstance(file, str):
            with open(os.path.join(rootPath, file), "rb") as f:
                bytes[
                    os.path.join(
                        rootPath.split(os.path.dirname(ymlFile))[1], file
                    ).replace("\\", "/")
                ] = f.read()
        elif isinstance(file, dict):
            for key in list(file.keys()):
                filesToBytes(file[key], os.path.join(f"{rootPath}\\{key}"), bytes)
    return bytes


with open(ymlFile, "r", encoding="utf-8") as f:
    files: list = yaml.load(f, Loader=yaml.FullLoader)

    yml = filesToBytes(files, os.path.dirname(os.path.abspath(ymlFile)))

    dirName = os.path.dirname(ymlFile)
    fileName = os.path.basename(ymlFile).split(".")[0] + ".py"
    newFile = os.path.join(dirName, fileName)
    with open(newFile, "w", encoding="utf-8") as f:
        f.write(
            f"""
import os
import __main__
import shutil

fileList = {yml}

usedFiles = []
class PixMap(str):
    def __new__(cls, path: str):
        path = path.split(":")[1]
        filePath: str = (
            str(os.path.dirname(__main__.__file__)).replace("\\\\", "/") + path
        )
        return super().__new__(cls, filePath)

    def __init__(self, path: str) -> None:
        usedFiles.append(self)
        self.path = path.split(":")[1]
        self.filePath: str = (
            str(os.path.dirname(__main__.__file__)).replace("\\\\", "/") + self.path
        )
        self.getBytes()
        self.writeFile()

    def __del__(self):
        try:
            dirs = (
                os.path.dirname(self.filePath)
                .split(os.path.dirname(__main__.__file__).replace("\\\\", "/"))[1]
                .split("/")[1]
            )
            shutil.rmtree(os.path.join(os.path.dirname(__main__.__file__), dirs))
        except:
            ...

    def writeFile(self):
        fileBytes = self.getBytes()
        os.makedirs(os.path.dirname(self.filePath), exist_ok=True)
        with open(self.filePath, "wb") as f:
            f.write(fileBytes)

    def getBytes(self):
        return fileList[self.path]

"""
        )
