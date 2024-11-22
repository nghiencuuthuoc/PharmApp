@echo off
mode con: cols=93 lines=10
Title NDC WEBBROWSER - ndcw
color A1
@echo on
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ Echo: Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
@ echo:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: NDC WEBBROWSER - ndcw
@ echo: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@ECHO off

set /p ndc_code=ENTER NDC CODE (EXAMP: 69379-285)?:

REM start "" "https://ndclist.com/ndc/%ndc_code%"
start "" "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=%ndc_code%"

cls
REM ndc_webbrowser.bat
ndc_webbrowser.bat