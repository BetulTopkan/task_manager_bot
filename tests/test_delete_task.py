from database import Database
import os

def test_delete_task():
    
    db = Database("test_tasks.db")
    

    task_id = db.add_task("Silinecek görev")
    
 
    result = db.delete_task(task_id)
    
   
    assert result is True
    

    tasks = db.get_all_tasks()
    assert len(tasks) == 0
    
 
    os.remove("test_tasks.db") 