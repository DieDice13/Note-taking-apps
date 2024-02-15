import json
import datetime
import uuid


# Определение класса Note, который представляет отдельную заметку
class Note:
    def __init__(self, id, title, body_text, created_at=None, updated_at=None):
        self.id = id  # Уникальный идентификатор заметки
        self.title = title  # Заголовок заметки
        self.body_text = body_text  # Тело заметки
        # Время создания заметки. Если не предоставлено, используется текущее время
        self.created_at = created_at if created_at else datetime.datetime.now()
        # Время последнего обновления заметки. Если не предоставлено, используется текущее время
        self.updated_at = updated_at if updated_at else datetime.datetime.now()

    # Метод для преобразования объекта заметки в словарь
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body_text,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }