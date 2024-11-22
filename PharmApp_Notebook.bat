@echo off
mode con: cols=95 lines=20
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@echo off
Title PharmApp Suite
@ECHO off

title PharmApp_Notebook     
@ECHO off
REM cd "%~dp0\scripts" && start cmd.exe /c "%~dp0\scripts\PharmApp_Notebook_1.bat"

set path=%~dp0
REM set py=%LocalAppData%\Programs\Python\Python312\python.exe
set py="%~dp0Python312\python.exe"
set nbopen="%~dp0Python312\Scripts\nbopen.exe"
set nbopenpy="%~dp0Python312\Lib\site-packages\nbopen\nbopen.py"

REM %py% %nbopenpy% "%path%\notebook\PharmApp.ipynb"

%py% %nbopenpy% "%~dp0\notebook\PharmApp.ipynb"

REM dir /b %path%\*.ipynb*

REM set /p file_name=ENTER file name (not end ipynb) ?:
pause
cls
REM %nbopen% "%path%\%file_name%.ipynb"
REM %py% "%~dp0Python312\Lib\site-packages\nbopen\nbopen.py" "%path%\%file_name%.ipynb"


