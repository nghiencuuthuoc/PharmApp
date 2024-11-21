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

title PharmApp_CLI     
ECHO ===========================================================================================
ECHO 1. Retrieve IIG DailyMed with Drug Name in iig_daily.txt 
ECHO 2. Retrieve IIG DailyMed with Drug Name in File
ECHO 3. View IIG DailyMed View Dtale
ECHO 4. Next ...
ECHO ===========================================================================================
set /p "Selection=Welcome^! Please Enter Your Selection: " || set "Selection=nothing"
if "%Selection%"=="1" (start cmd.exe /c iig_daily.txt.bat)
if "%Selection%"=="2" (start cmd.exe /c iig_input_file_name.bat)
if "%Selection%"=="3" (start cmd.exe /c view_iig_dt.bat)
if "%Selection%"=="4" (cd "%~dp0\scripts" && start cmd.exe /c "%~dp0\scripts\PharmApp_CLI_1.bat")

REM pause
REM PharmApp_CLI_1.bat

