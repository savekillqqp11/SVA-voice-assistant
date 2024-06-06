@echo off

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