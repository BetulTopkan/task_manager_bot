import unittest
import asyncio
from database import Database

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_tasks.db")
        asyncio.get_event_loop().run_until_complete(self.db.create_tables())
        
    def test_show_tasks(self):
        # Test için birkaç görev ekleyelim
        asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Birinci test görevi")
        )
        asyncio.get_event_loop().run_until_complete(
            self.db.add_task("İkinci test görevi")
        )
        
        # Görevleri alalım
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        
        # Kontroller
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], "Birinci test görevi")
        self.assertEqual(tasks[1][1], "İkinci test görevi")
        self.assertFalse(tasks[0][2])  # completed durumu False olmalı
        
    def test_show_empty_tasks(self):
        # Boş görev listesini kontrol edelim
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main() 