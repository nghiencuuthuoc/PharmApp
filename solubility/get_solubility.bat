@echo off
mode con: cols=95 lines=20
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@echo off
Title libgen_search (libgs)

REM set py=%LocalAppData%\Programs\Python\Python312\python.exe

set path=%~dp0
set py="%~dp0\..\Python312\python.exe"

%py% "%path%\get_solubility.py" 

pause
cls
get_solubility.bat
