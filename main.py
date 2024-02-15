import datetime
from functional import Functional

# Создаем экземпляр приложения
app = Functional()

# Запускаем бесконечный цикл для взаимодействия с пользователем
while True:
    command = input("Введите команду: ")  # Запрашиваем команду у пользователя
    if command == "list":  # Если команда "list", то выводим список заметок
        app.list()
    elif command == "add":  # Если команда "add", то создаем новую заметку
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        app.create(title, body)
        print("Заметка успешно сохранена")
    elif command == "delete":  # Если команда "delete", то удаляем заметку
        id = input("Введите ID заметки: ")
        app.delete(id)
    elif command == "update":  # Если команда "update", то обновляем заметку
        id = input("Введите ID заметки: ")
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новое тело заметки: ")
        app.update(id, title, body)
    elif command == "list_by_date":  # Если команда "list_by_date", то выводим список заметок по дате
        date_str = input("Введите дату (гггг-мм-дд): ")
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        app.list_by_date(date)
    elif command == "exit":  # Если команда "exit", то выходим из цикла
        break
