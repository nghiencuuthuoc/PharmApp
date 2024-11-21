@echo off
mode con: cols=100 lines=20
cls
Title run_py_file_currdir // rpfcd
color A1
@echo on
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com or info@nghiencuuthuoc.com
@ Echo: https://twitter.com/nghiencuuthuoc // https://facebook.com/nghiencuuthuoc
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: run py file (rpyf)
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ echo: THANKS FOR USING
@ echo: KEY SEACH!
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ECHO off
set path=%~dp0
set py=%LocalAppData%\Programs\Python\Python312\python.exe
REM set py="%~dp0\..\Python312\python.exe"

dir /b %path%\*.py*

set /p file_name=ENTER file name (not end py) ?:
cls
Title run_py_file_currdir // rpfcd // %file%

%py% "%path%\%file_name%.py" 

pause
cls
run_py_file_currdir.bat
