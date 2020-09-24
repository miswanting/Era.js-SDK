@echo off
echo NOTICE!
echo If the anti-virus software reports, please allow.
echo If you have security concerns, you can view the source code in advance.
echo .
echo Press ANY Button to Continue.
pause
cls
echo Extract: Prebuilts
PowerShell Expand-Archive -LiteralPath prebuilt/prebuilt.zip -DestinationPath prebuilt -Force
REM rm prebuilt/prebuilt.zip
echo Dependence: Python Requirements
pip install -r requirements.txt 
echo Dependence: Era.js Game Engine
mklink /j "erajs" "..\Era.js\Next\BackEnd\erajs"
echo Done!
pause