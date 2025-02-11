import unittest
import asyncio
from database import Database

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_tasks.db")
        asyncio.get_event_loop().run_until_complete(self.db.create_tables())
        
    def test_complete_task(self):
        # Test için bir görev ekleyelim
        task_id = asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Tamamlanacak test görevi")
        )
        
        # Görevi tamamlayalım
        result = asyncio.get_event_loop().run_until_complete(
            self.db.complete_task(task_id)
        )
        self.assertTrue(result)
        
        # Görevin tamamlandığını kontrol edelim
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 1)
        self.assertTrue(tasks[0][2])  # completed durumu True olmalı
        
    def test_complete_nonexistent_task(self):
        # Var olmayan bir görevi tamamlamayı deneyelim
        result = asyncio.get_event_loop().run_until_complete(
            self.db.complete_task(999)
        )
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main() 