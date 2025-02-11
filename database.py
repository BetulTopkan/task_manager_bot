import aiosqlite

class Database:
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name

    async def create_tables(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    completed BOOLEAN NOT NULL DEFAULT 0
                )
            ''')
            await db.commit()

    async def add_task(self, description):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute(
                'INSERT INTO tasks (description) VALUES (?)',
                (description,)
            )
            await db.commit()
            return cursor.lastrowid

    async def delete_task(self, task_id):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute(
                'DELETE FROM tasks WHERE id = ?',
                (task_id,)
            )
            await db.commit()
            return cursor.rowcount > 0

    async def get_tasks(self):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute('SELECT id, description, completed FROM tasks')
            return await cursor.fetchall()

    async def complete_task(self, task_id):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute(
                'UPDATE tasks SET completed = 1 WHERE id = ?',
                (task_id,)
            )
            await db.commit()
            return cursor.rowcount > 0 