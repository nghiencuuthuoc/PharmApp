@echo off
mode con: cols=95 lines=20
Title nbopen_currdir_test
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ECHO off
set path=%~dp0
REM set py=%LocalAppData%\Programs\Python\Python312\python.exe
set py="%~dp0Python312\python.exe"
set nbopen="%~dp0Python312\Scripts\nbopen.exe"
set nbopenpy="%~dp0Python312\Lib\site-packages\nbopen\nbopen.py"

%py% %nbopenpy% "%path%\test.ipynb"

REM dir /b %path%\*.ipynb*

REM set /p file_name=ENTER file name (not end ipynb) ?:

cls
REM %nbopen% "%path%\%file_name%.ipynb"
REM %py% "%~dp0Python312\Lib\site-packages\nbopen\nbopen.py" "%path%\%file_name%.ipynb"


 
nbopen_currdir_test.bat