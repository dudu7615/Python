@echo off
:: 挂载目录到 x:\
subst /D x:
subst x: %1
:: 设置环境变量
set "VS=C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\VsDevCmd.bat"
set "ENV=Python"
:: 激活环境
call conda activate %ENV%
call %VS%
:: 运行 nuitka
python -m EasyNuitka
:: 取消挂载
subst /D x:
