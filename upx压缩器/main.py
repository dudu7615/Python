r"""
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def showFiles(rootPath:str, files:list[str]=[]):
    fileList: list[str] = os.listdir(rootPath)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in fileList:
        # 利用os.path.join()方法取得路径全名，并存入path变量，否则每次只能遍历一层目录
        path = os.path.join(rootPath, file)
        # 判断是否是文件夹
        if os.path.isdir(path):
            showFiles(path, files)
        else:
            files.append(path)
    return files


def main(path: str):
    if isDir := os.path.isdir(path):
        files = showFiles(path)
        for i in range(len(files) // 10 + 1):
            try:
                command = files[10 * (i - 1) : 10 * i]
            except:
                command = files[10 * (i - 1) :]

            command = [f'"{i}"' for i in command]
            os.system(rf"@{ROOT}/upx.exe -9 {' '.join(command)}")
            os.system("cls")

    else:
        path = f'"{path}"'
        os.system(rf"@upx.exe -9 {path}")

if __name__ == "__main__":
    path = input("请输入文件或文件夹路径：")
    main(path)
    os.system("pause")
    