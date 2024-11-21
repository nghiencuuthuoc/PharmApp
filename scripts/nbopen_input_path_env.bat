@echo off
mode con: cols=95 lines=20
cls
Title nbopen_input_path
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ECHO off
set path=%~dp0
set /p path=ENTER PATH:

set /p env=ENTER CONDA ENV:
set py="%userprofile%\anaconda3\envs\%env%\python.exe"
set nbopenpy="%userprofile%\anaconda3\envs\%env%\Lib\site-packages\nbopen\nbopen.py"

REM set py=%LocalAppData%\Programs\Python\Python312\python.exe

REM set py="%~dp0Python312\python.exe"
REM set nbopen="%~dp0Python312\Scripts\nbopen.exe"
REM set nbopenpy="%~dp0Python312\Lib\site-packages\nbopen\nbopen.py"


dir /b %path%\*.ipynb*

set /p file_name=ENTER file name (not end ipynb) ?:

cls
Title nbopen_full_path // %nbopen% 
%py% %nbopenpy% "%path%\%file_name%.ipynb"

REM %nbopen% "%path%\%file_name%.ipynb"
REM %py% "%~dp0Python312\Lib\site-packages\nbopen\nbopen.py" "%path%\%file_name%.ipynb"

pause
cls

nbopen_mldd_2023_input_path.bat