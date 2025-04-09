from database import Database
import os

def test_complete_task():
    # Test veritabanı oluştur
    db = Database("test_tasks.db")
    
    # Görev ekle
    task_id = db.add_task("Tamamlanacak görev")
    
    # Görevi tamamla
    result = db.complete_task(task_id)
    
    # Tamamlama işleminin başarılı olduğunu kontrol et
    assert result is True
    
    # Görevin tamamlandığını kontrol et
    tasks = db.get_all_tasks()
    assert tasks[0][2] == 1  # completed = True
    
    # Test veritabanını temizle
    os.remove("test_tasks.db") 