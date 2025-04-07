call ..\venv\Scripts\activate.bat
python.exe -m pip list
pause
pyinstaller -F --icon=app.ico --name=GameGallows ..\main.py
pause