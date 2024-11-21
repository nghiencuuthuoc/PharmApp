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



set /p env=ENTER CONDA ENV:
set py="%userprofile%\anaconda3\envs\%env%\python.exe"
set nbopenpy="%userprofile%\anaconda3\envs\%env%\Lib\site-packages\nbopen\nbopen.py"

REM set py=%LocalAppData%\Programs\Python\Python312\python.exe

REM set path=%~dp0
REM set py="%~dp0Python312\python.exe"
REM set nbopen="%~dp0Python312\Scripts\nbopen.exe"
REM set nbopenpy="%~dp0Python312\Lib\site-packages\nbopen\nbopen.py"

REM set /p path=ENTER PATH:

REM dir /b %path%\*.ipynb*

REM set /p file_name=ENTER file name (not end ipynb) ?:

set /p full_path=ENTER FULL PATH IPYNB FILE:


cls
Title nbopen_mldd_2023 // %nbopen% 
%py% %nbopenpy% "%full_path%"

REM %nbopen% "%path%\%file_name%.ipynb"
REM %py% "%~dp0Python312\Lib\site-packages\nbopen\nbopen.py" "%path%\%file_name%.ipynb"

pause
cls

nbopen_mldd_2023_full_path.bat