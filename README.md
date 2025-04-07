# Игра "Виселица" (Gallows Game)

Простая консольная реализация классической игры "Виселица" на Python.

## Описание

Игроку нужно угадать загаданное слово по буквам, прежде чем будет нарисована полная виселица.

## Особенности

- Случайный выбор слова из словаря
- Подсказка-описание для загаданного слова
- Визуализация текущего состояния (отгаданные буквы, ошибки)
- Возможность сыграть повторно

## Требования

- Python 3.x

## Установка

1. Склонируйте репозиторий или скачайте файлы:

## Зависимости

Проект использует только стандартные библиотеки Python (`random`, `os`, `sys`).  
Установка дополнительных пакетов не требуется.

## Сборка приложения

Создание виртуального окружения

```bash
python -m venv venv
```

Установка PyInstaller

```bash
pip install -r requirements.txt
```

Сборка

```bash
release\make.bat
```

Готовый EXE-файл появится в папке **release\dist\**