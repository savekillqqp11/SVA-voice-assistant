@echo off
setlocal

rem Get the directory of the batch file
set "batch_dir=%~dp0"

rem Navigate to the directory of the batch file
cd /d "%batch_dir%"

rem Check if the script is running with administrator privileges
NET SESSION >NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Running script without admin privileges...
    powershell -Command "Start-Process -FilePath '%~dpnx0' -Verb RunAs"
    exit /b
)

rem Check if PowerShell is installed
where powershell >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo PowerShell not found. Installing PowerShell...
    curl -o PowerShell-7.1.3-win-x64.msi https://github.com/PowerShell/PowerShell/releases/download/v7.1.3/PowerShell-7.1.3-win-x64.msi
    start /wait msiexec /i PowerShell-7.1.3-win-x64.msi /quiet
    del PowerShell-7.1.3-win-x64.msi
)

rem Install Python if not installed
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing Python...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python-installer.exe
)

rem Install required Python packages
python -m pip install --upgrade pip
pip install pyttsx3 wikipedia SpeechRecognition DateTime pydub pyjokes googletrans translate pyautogui elevate pyaudio

rem Ensure Python script uses the correct path for FFmpeg
rem Note: This step is only necessary if your Python script relies on FFmpeg

cls

rem Run the Main.py script and capture output to error.log
python MainEN.py %* 2> error.log

rem Check the exit code of the Python script
set "exit_code=%ERRORLEVEL%"

if %exit_code% NEQ 0 (
    echo The script encountered some errors. Check error.log for details.
    type error.log
) else (
    echo The script ran successfully.
)

pause
