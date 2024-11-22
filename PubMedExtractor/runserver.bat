@echo off
mode con: cols=95 lines=20
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@echo off
@ Echo: PharmApp // PubMedExtractor
@ echo: THANKS FOR USING
@ echo: Enter: python manage.py runserver
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@ECHO OFF
Title PharmApp // PubMedExtractor
start "" "http://127.0.0.1:80"

python manage.py runserver 127.0.0.1:80
pause

runserver.bat