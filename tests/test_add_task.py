import unittest
import asyncio
from database import Database

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_tasks.db")
        asyncio.get_event_loop().run_until_complete(self.db.create_tables())

    def test_add_task(self):
        task_id = asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Test görevi")
        )
        self.assertIsNotNone(task_id)
        
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test görevi")

if __name__ == '__main__':
    unittest.main() 