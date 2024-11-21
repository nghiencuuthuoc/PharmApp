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
ECHO 1. View View PandasGui
ECHO 2. Retrieve SageRX with Drug Name in File
ECHO 3. Retrieve SageRX with Name
ECHO 4. Next ...
ECHO ===========================================================================================
set /p "Selection=Welcome^! Please Enter Your Selection: " || set "Selection=nothing"
if "%Selection%"=="nothing" ECHO "%Selection%" is not valid please try again
if "%Selection%"=="1" (cd "%~dp0\scripts" && start cmd.exe /c "%~dp0\scripts\view_iig_pdg.bat")
if "%Selection%"=="2" (cd "%~dp0\scripts" && start cmd.exe /c "%~dp0\scripts\iigs_input_file.bat")
if "%Selection%"=="3" (cd "%~dp0\scripts" && start cmd.exe /c "%~dp0\scripts\iigs.bat")
if "%Selection%"=="4" (cd "%~dp0\scripts" && start cmd.exe /c "%~dp0\scripts\PharmApp_CLI_1.bat")

REM pause
REM PharmApp_CLI.bat

