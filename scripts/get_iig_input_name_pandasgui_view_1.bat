@echo off
mode con: cols=95 lines=20
cls
Title get_iig_input_name_pandagui_view
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
Title get_iig_input_name_pandagui_view // iign // %path% // %py%
%py% "%path%\get_iig_input_name_pandasgui_view_1.py" 

pause
cls
call get_iig_input_name_pandasgui_view_1.bat
