import sqlite3
from typing import List, Tuple

class Database:
    def __init__(self, db_name: str = "tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_task(self, description: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        self.conn.commit()
        return cursor.lastrowid

    def delete_task(self, task_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def get_all_tasks(self) -> List[Tuple]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, description, completed FROM tasks")
        return cursor.fetchall()

    def complete_task(self, task_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def __del__(self):
        self.conn.close() 