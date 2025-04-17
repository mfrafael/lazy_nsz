@echo off
setlocal

REM Path to the engine folder where all tools live
set ENGINE_DIR=%~dp0engine

REM Create venv if it doesn't exist
if not exist "%ENGINE_DIR%\venv" (
    echo Creating Python virtual environment...
    "%ENGINE_DIR%\python-embed\python.exe" -m venv "%ENGINE_DIR%\venv"
    call "%ENGINE_DIR%\venv\Scripts\activate.bat"
    pip install --upgrade pip
    pip install nsz[tqdm]
) else (
    call "%ENGINE_DIR%\venv\Scripts\activate.bat"
)

REM Run the Python script inside engine
python "%ENGINE_DIR%\NSZ_Uncompresser.py" "%~1"

pause
endlocal
