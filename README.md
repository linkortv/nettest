# nettest
GUI application for auto test network connection
We use python and open license package PySide for GUI, and os possibility, and speedtest-cli

Вам понадобится добавить свой .env файл в корень с проектом, где  будут указаны все ваши envirenment переменные
Для проекта используется python 3.8+, PySide6, speedtest-cli и python-dotenv.
1. Через pip установить все необходимые пакеты
2. Далее в папки pyside можно найти qtdesigner при необходимости изменить оформление
3. После нужно перевести .ui файл в .py pyside6-uic design.ui > form.py
4. Скрипты тестов изменяются для каждой ОС отдельно в соответствующей папке
5. Для компиляции изменений нужно воспользоваться pyinstaller-ом, запускается для каждой ОС отдельно, на соответствующей ОС
