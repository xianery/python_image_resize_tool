@echo off

echo . 
echo Building
echo .
pyinstaller --hide-console hide-early --onefile main.py
echo .
echo Completed
timeout 3 > NUL
