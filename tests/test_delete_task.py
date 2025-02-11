import unittest
import asyncio
from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_tasks.db")
        asyncio.get_event_loop().run_until_complete(self.db.create_tables())
        
    def test_delete_task(self):
       
        task_id = asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Silinecek test görevi")
        )
        
       
        result = asyncio.get_event_loop().run_until_complete(
            self.db.delete_task(task_id)
        )
        self.assertTrue(result)
        
        
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 0)
        
    def test_delete_nonexistent_task(self):
        
        result = asyncio.get_event_loop().run_until_complete(
            self.db.delete_task(999)
        )
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main() 
