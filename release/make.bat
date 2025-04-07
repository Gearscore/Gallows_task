@echo off
REM Активация виртуального окружения
call ..\venv\Scripts\activate.bat

REM Проверка установленных зависимостей
python.exe -m pip list
pause

REM Сборка exe-файла через PyInstaller
pyinstaller -F --icon=app.ico --name=GameGallows ..\main.py

REM Пауза для просмотра результатов
pause