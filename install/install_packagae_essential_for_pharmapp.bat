@echo off
mode con: cols=95 lines=20
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@echo off
Title install_packagae_essential_for_pharmapp

python.exe -m pip install --upgrade pip
python -m pip install --upgrade pip
pause
pip install pandagui
pause

pip install dtale flask

pip install pubchempy

pip install nbopen psycopg2 numpy bs4
pause
REM pip install pandas
pip install numpy
pause
pip install bs4
pip install psycopg2

pip install chembl_webresource_client
pip install bioservices

REM winget install --id Git.Git -e --source winget
REM pip install git+https://github.com/adamerose/pandasgui.git

pause

