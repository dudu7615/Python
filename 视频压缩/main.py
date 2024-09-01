import cv2
from pathlib import Path
from rich.progress import Progress
from rich import print
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip


from multiprocessing import Process


ROOT = Path(__file__).parent

inputPath = ROOT / "data" / "input"
outputPath = ROOT / "data" / "output"


class ReSize(Process):
    def __init__(self, inputPath: Path, outputPath: Path, size):
        super().__init__()
        self.inputPath = str(inputPath)
        self.outputPath = str(outputPath)
        self.size = size

    def run(self):
        cap = cv2.VideoCapture(self.inputPath)
        # # 获取视频总帧数
        # frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        # 获取视频的帧率和编码信息
        # fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        # 创建一个VideoWriter对象
        out = cv2.VideoWriter(self.outputPath, fourcc, 30, self.size)

        while cap.isOpened():
            ret, frame = cap.read()
            if ret != True:
                break

            # 调整帧的大小
            resized_frame = cv2.resize(frame, self.size)
            # 写入到VideoWriter对象中
            out.write(resized_frame)

        cap.release()
        out.release()
        cv2.destroyAllWindows()

class SetVoice(Process):
    def __init__(self, inputPath: Path, outputPath: Path, size):
        super().__init__()
        self.inputPath = str(inputPath)
        self.outputPath = str(outputPath)
        self.size = size

    def run(self):
        # 打开视频
        video = VideoFileClip(self.outputPath)

        # 提取原视频的音频
        audio = AudioFileClip(self.inputPath)

        # 将音频的长度调整为与视频的长度相同
        audio = audio.subclip(0, video.duration)

        video_with_audio = CompositeVideoClip([video.set_audio(audio)])


        video_with_audio.write_videofile(self.outputPath, codec="libx264", logger=None)



def setSize(files:list[Path],porg: Progress):
    processes = []
    task = porg.add_task("[cyan]压缩视频 ...", total=len(files))

    while True:
        if len(processes) < 12:
            if files:
                file = files[0]
                output = outputPath / file.name
                input = inputPath / file

                main = ReSize(input, output, (1280, 720))
                main.start()
                processes.append(main)
                files.pop(0)

                print(f"[blue]开始任务:[/blue] {file.name}")
            else:
                break
        else:
            process: ReSize
            for process in processes:
                if not process.is_alive():
                    print(f"[green]完成任务:[/green] {Path(process.inputPath).name}")
                    processes.remove(process)
                    porg.update(task, advance=1)

    porg.update(task, advance=100)


def setVoice(files:list[Path],porg: Progress):
    processes = []
    task = porg.add_task("[cyan]添加音频 ...", total=len(files))

    # while True:
    #     if len(processes) < 12:
    #         if files:
    #             file = files[0]
    #             output = outputPath / file.name

    #             main = SetVoice(inputPath / file, output, (1280, 720))
    #             main.start()
    #             processes.append(main)
    #             files.pop(0)

    #             print(f"[blue]开始任务:[/blue] {file.name}")
    #         else:
    #             break
    #     else:
    #         process: SetVoice
    #         for process in processes:
    #             if not process.is_alive():
    #                 print(f"[green]完成任务:[/green] {Path(process.inputPath).name}")
    #                 processes.remove(process)
    #                 porg.update(task, advance=1)

    file = files[0]
    input = inputPath / file
    output = outputPath / file.name
    SetVoice(input, output, (1280, 720)).start()

    porg.update(task, advance=100)

if __name__ == "__main__":
    files = list(inputPath.glob("*.mp4"))
    with Progress() as progress:
        # setSize(files,progress)
        setVoice(files,progress)

