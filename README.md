# nettest
GUI application for auto test network connection
We use python and open license package PySide for GUI, and os possibility, and speedtest-cli

Вы можете добавить свой .env файл в папку для вашей системы, где  будут указаны все ваши envirenment переменные, но тогда при сборке их нужно указывать отдельно, что бы включить в сборку
Для проекта используется python 3.8+, PySide6, speedtest-cli(кроме linux) и python-dotenv(если есть env переменные).
1. Через pip установить все необходимые пакеты
2. Далее в папки pyside можно найти qtdesigner при необходимости изменить оформление
3. После нужно перевести .ui файл в .py pyside6-uic design.ui > form.py, под линукс прийдется запустить python скрипт из директории пакета с указанием полного пути до него
4. Скрипты тестов изменяются для каждой ОС отдельно в соответствующей папке
5. Для компиляции изменений нужно воспользоваться pyinstaller-ом, запускается для каждой ОС отдельно, на соответствующей ОС
5.1. Под windows для иконки нужно добавить --icon [относительный путь до иконки]
5.2. В моем случаи команда выглядит так pyinstaller -w -F -i "icon.ico" main.py
6. Для иконки нужно создать файл ресурсов pyside6-rcc icon.qrc -o resources.py
7. Для корректной сборки sppedtest, необходимо в пакете speedtest заменить все __builten__ на builtens
