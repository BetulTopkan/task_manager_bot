import unittest
import asyncio
from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_tasks.db")
        asyncio.get_event_loop().run_until_complete(self.db.create_tables())
        
    def test_delete_task(self):
        # Önce test için bir görev ekleyelim
        task_id = asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Silinecek test görevi")
        )
        
        # Görevi silelim
        result = asyncio.get_event_loop().run_until_complete(
            self.db.delete_task(task_id)
        )
        self.assertTrue(result)
        
        # Görevin silindiğini kontrol edelim
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 0)
        
    def test_delete_nonexistent_task(self):
        # Var olmayan bir görevi silmeyi deneyelim
        result = asyncio.get_event_loop().run_until_complete(
            self.db.delete_task(999)
        )
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main() 