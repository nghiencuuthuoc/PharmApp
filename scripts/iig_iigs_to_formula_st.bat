@echo off
mode con: cols=95 lines=20
cls
Title iigt
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@ECHO off
set path=%~dp0

@REM run with env conda
@REM set /p env=ENTER CONDA ENV:
@REM set py="%userprofile%\anaconda3\envs\%env%\python.exe"

@REM set py="%userprofile%\anaconda3\envs\mldd_2023\python.exe"

@REM set py=%LocalAppData%\Programs\Python\Python312\python.exe

set py="%~dp0..\Python312\python.exe"

REM set /p file_name=input file name (not end py) ?:
Title PharmApp Web // %path% // %py%


@REM %py% "%path%\test.py"


%py% -m streamlit run "%path%\iig_iigs_to_formula_st.py"

pause
cls
REM iig_iigs_to_formula_st.bat
