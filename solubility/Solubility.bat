@echo off
mode con: cols=100 lines=20
Title Solubility - Solu
color A1
@echo on
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: PharmApp // Copyright 2023 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ Echo: Solubility
@ echo: THANKS FOR USING
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ echo: KEY SEACH SAMPLE!
@ echo: COSM: Kojic Acid Dipalmitate
@ echo: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@ECHO OFF
set /p key_search=ENTER KEY SEARCH NOW ?:

start "" "https://pubchem.ncbi.nlm.nih.gov/compound/%key_search%#section=Solubility&fullscreen=true"

Solubility.bat