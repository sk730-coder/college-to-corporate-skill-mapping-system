@echo off
echo Starting College to Corporate Skill Mapper...
echo.

REM Change to the correct directory
cd /d "%~dp0"

REM Check if app.py exists
if not exist "app.py" (
    echo Error: app.py not found in current directory!
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo Found app.py in: %CD%
echo.

REM Run the application
python app.py

pause
