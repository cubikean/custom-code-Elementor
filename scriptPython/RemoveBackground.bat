@echo off
setlocal

:: Change this path to your Python executable and the location of your script
set PYTHON_PATH=C:\Python310\python.exe
set SCRIPT_PATH=C:\Users\Beekom\Desktop\dev\DEV\scriptPython\removebg.py

:: Loop over all the selected files
:loop
if "%~1"=="" goto endloop
%PYTHON_PATH% %SCRIPT_PATH% "%~1"
shift
goto loop
:endloop

endlocal
