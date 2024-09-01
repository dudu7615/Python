from pathlib import Path
import time
import os
import sys


outputDir = Path(
    Path(os.environ["USERPROFILE"]) / "AppData" / "Local" / "点名器" / "data"
    if getattr(sys, "frozen", False)
    else Path(__file__).parent.parent
)

if not outputDir.exists():
    outputDir.mkdir(exist_ok=True, parents=True)

inputPath = Path(__file__).parent / "names"
outputPath = outputDir / "names"

for i in range(5, 0, -1):
    print(f"\r将在{i}秒后重置名单，关闭此窗口可取消", end="")
    time.sleep(1)

print("\n正在重置名单")
outputPath.write_text(inputPath.read_text(encoding="utf-8"))

print("重置完成")
input("按回车键退出")
