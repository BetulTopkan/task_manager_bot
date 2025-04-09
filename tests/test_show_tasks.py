from database import Database
import os

def test_show_tasks():
    
    db = Database("test_tasks.db")
    
    
    db.add_task("Görev 1")
    db.add_task("Görev 2")
    
    
    tasks = db.get_all_tasks()
    
   
    assert len(tasks) == 2
    assert tasks[0][1] == "Görev 1"
    assert tasks[1][1] == "Görev 2"
    
   
    os.remove("test_tasks.db") 