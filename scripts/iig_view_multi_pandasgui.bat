@echo off
mode con: cols=93 lines=20
cls
color A1
@echo on
@ echo: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com or info@nghiencuuthuoc.com
@ Echo: https://twitter.com/nghiencuuthuoc // https://facebook.com/nghiencuuthuoc
@ echo: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@ECHO off
set path=%~dp0
REM set py=%LocalAppData%\Programs\Python\Python312\python.exe
set py="%~dp0\..\Python312\python.exe"

REM set /p file_name=ENTER file name (not end py) ?:
Title iig_view_multi_pandasgui // iigm
%py% "%path%\iig_view_multi_pandasgui.py"
@REM pause
REM timeout /t 300

iig_view_multi_pandasgui.bat
