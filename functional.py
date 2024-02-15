import datetime
import json
import uuid
from note import Note


# Определение класса Functional, который представляет весь функционал приложения для заметок
class Functional:
    def __init__(self):
        self.notes = []  # Список для хранения заметок

    # Метод для вывода списка заметок
    def list(self):
        self.load_notes()  # Загружаем заметки
        for note in self.notes:  # Выводим информацию о каждой заметке
            print(f"---\nID: {note.id}\nTitle: {note.title}\nBody: {
                  note.body_text}\nCreated at: {note.created_at}\nUpdated at: {note.updated_at}\n---")


    # Метод для создания новой заметки
    def create(self, title, body_text):
        # ID заметки теперь является уникальным идентификатором
        id = str(uuid.uuid4())[:5]  # Берем только первые 8 символов UUID
        note = Note(id, title, body_text)  # Создаем новую заметку
        self.notes.append(note)  # Добавляем заметку в список
        self.save_notes()  # Сохраняем заметки


    # Метод для удаления заметки
    def delete(self, id):
        # Проверяем, существует ли заметка с указанным ID
        if any(note.id == id for note in self.notes):
            self.notes = [note for note in self.notes if note.id != id]  # Удаляем заметку из списка
            self.save_notes()  # Сохраняем заметки
            print(f"Заметка с ID {id} успешно удалена.")  # Выводим сообщение об успешном удалении
        else:
            print(f"Заметка с ID {id} не найдена.")  # Выводим сообщение, если заметка не найдена
 
    
    # Метод для обновления заметки
    def update(self, id, title, body_text):
        for note in self.notes:  # Ищем заметку по ID
            if note.id == id:  # Если нашли, то обновляем информацию
                note.title = title
                note.body_text = body_text
                note.updated_at = datetime.datetime.now()  # Обновляем время последнего изменения
                self.save_notes()  # Сохраняем заметки
                return
        # Если заметка не найдена, то выводим сообщение об ошибке
        print("Заметка не найдена")



    # Метод для вывода списка заметок по дате
    def list_by_date(self, date):
        self.load_notes()  # Загружаем заметки из файла
        for note in self.notes:  # Проходим по каждой заметке в списке
            # Если дата создания или последнего обновления заметки совпадает с указанной датой
            if note.created_at.date() == date or note.updated_at.date() == date:
                # Выводим информацию о заметке
                print(f"---\nID: {note.id}\nTitle: {note.title}\nBody: {note.body_text}\nCreated at: {note.created_at}\nUpdated at: {note.updated_at}\n---")


    # Метод для загрузки заметок из файла
    def load_notes(self):
        try:
            with open('notes.json', 'r') as f:  # Открываем файл для чтения
                if f.read().strip():  # Проверяем, не пуст ли файл
                    f.seek(0)  # Возвращаем указатель в начало файла
                    notes_dict = json.load(f)  # Загружаем заметки из файла
                    self.notes = [Note(note['id'], note['title'], note['body'], 
                                    datetime.datetime.strptime(note['created_at'], '%Y-%m-%d %H:%M:%S'),
                                    datetime.datetime.strptime(note['updated_at'], '%Y-%m-%d %H:%M:%S'))
                                for note in notes_dict]
                else:
                    self.notes = []
        except FileNotFoundError:  # Если файл не найден, то список заметок остается пустым
            self.notes = []



    # Метод для сохранения заметок в файл
    def save_notes(self):
        with open('notes.json', 'w') as f:  # Открываем файл для записи
            # Сохраняем заметки в файл в формате JSON
            json.dump([note.to_dict() for note in self.notes], f)
