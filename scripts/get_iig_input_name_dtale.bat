@echo off
mode con: cols=95 lines=20
cls
Title get_iig_input_name_dtale
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@ECHO off
set path=%~dp0
REM set py=%LocalAppData%\Programs\Python\Python312\python.exe
set py="%~dp0\..\Python312\python.exe"

REM set /p file_name=input file name (not end py) ?:
Title get_iig_input_name_dtale // iignt // %path% // %py%
%py% "%path%\get_iig_input_name_dtale.py"

pause
cls
get_iig_input_name_dtale.bat
