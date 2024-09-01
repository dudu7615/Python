@echo off
:: git配置
git config --global user.name "李昊轩"
git config --global user.email "dudu7615@qq.com"
git config --global http.postBuffer 102400000

:: conda
:: 镜像源
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mro/
:: 缓存
call conda config --add pkgs_dirs D:/Conda/pkgs
call conda config --add envs_dirs D:/Conda/envs
pause
