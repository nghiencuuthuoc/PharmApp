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
ECHO 1. View IIG DailyMed Inactive Column
ECHO 2. View IIG DailyMed and Web NDC
ECHO 3. View IIG DailyMed View Dtale
ECHO 4. IIG DailyMe to Formulation
ECHO ===========================================================================================
set /p "Selection=Welcome^! Please Enter Your Selection: " || set "Selection=nothing"
if "%Selection%"=="1" (start cmd.exe /c view_col_inactive.bat)
if "%Selection%"=="2" (start cmd.exe /c view_iig_ndc.bat)
if "%Selection%"=="3" (start cmd.exe /c view_iig_dt.bat)
if "%Selection%"=="4"  (start cmd.exe /c iig2formula.bat)

REM pause
REM PharmApp_CLI_1.bat

