@echo off
mode con: cols=95 lines=20
cls
Title get_iig_input_name_dtale_view_inactive
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

REM set /p file_name=input file name (not end py) ?:

%py% "%path%\get_iig_input_name_dtale_view_inactive.py" 

pause
cls
get_iig_input_name_dtale_view_inactive.bat
